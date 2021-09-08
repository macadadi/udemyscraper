from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import FreeCourses
import requests
from django.core.files.base import ContentFile


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FreeCoursesSerializer
from .pageurldata import urls_data



from celery import shared_task










def get_course_detail(course_link,upload_date,image_url,image_name,course_name,course_status,category):
    try:
        if course_status == 'Active':
            html_doc = requests.get(course_link).text
            c_soup = BeautifulSoup(html_doc, 'html.parser')
            course_title = c_soup.find('h1',
                                       attrs={'class': 'udlite-heading-xl clp-lead__title clp-lead__title--small'}).text
            course_description = c_soup.find('div', attrs={'class': 'udlite-text-md clp-lead__headline'}).text
            # course_price = c_soup.find('button',attrs={'class':'udlite-btn udlite-btn-large udlite-btn-brand udlite-heading-md add-to-cart'})
            objectives = c_soup.find_all('span', attrs={'class': 'what-you-will-learn--objective-item--ECarc'})
            course_outcome=''
            for objective in objectives:
                course_outcome += objective.text + ","
            store_in_db = FreeCourses(name=course_name, description=course_description, outcome=course_outcome,
                                      status=course_status, headline=course_title, uploaded=upload_date,
                                      link=course_link,
                                      category=category, image_name=image_name, image_url=image_url
                                      )
            response = requests.get(image_url)
            if response.status_code == 200:
                store_in_db.image_file.save(image_name, ContentFile(response.content), save=False)
            store_in_db.save()
        else:
            print('Expired')
            return
    except:
        print(f'Error two occure with {course_name}')
        return


def get_free_course(base_url,category):
    try:
        html_doc = requests.get(base_url).text
        c_soup = BeautifulSoup(html_doc, 'html.parser')
        block = c_soup.find_all('div', attrs={'class': 'theme-block'})
        for element in block:
            upload_date = element.find('small').text
            image_url = element.find('img')['src']
            image_name = image_url[42:-4].replace('/', '_') + '.jpg'
            course_name = element.find('h4').text
            url_link = element.find('h4').find('a')['href']
            html_c = requests.get(url_link).text
            s_soup = BeautifulSoup(html_c, 'html.parser')
            course_state = s_soup.find('a', attrs={'class': 'button-icon button-icon-orange'})
            if course_state is None:
                course_status = 'Active'
                course_link = s_soup.find('div', attrs={'class': 'text-center'}
                                          ).find('a',attrs={'class': 'button-icon'})['href']
                # get_course_detail(course_link, upload_date, image_url, image_name, course_name, course_status, category)



    except:
        print(f"an error occured with {base_url}")
        return


# @shared_task(bind=True)
def create_random_user_accounts(self):
    for Link in urls_data:
        for key in Link:
            category = key
            for i in range(5):
                if i == 0:
                    base_url = Link[key]
                else:
                    base_url = Link[key] + '/' + str(i)
                get_free_course(base_url,category)



@shared_task(bind=True)
def add(self):
    for i in range(10):
        print("I am makadadi the boss")






