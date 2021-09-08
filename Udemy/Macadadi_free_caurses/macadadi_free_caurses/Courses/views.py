from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import FreeCourses
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FreeCoursesSerializer
from .pageurldata import urls_data


from django.core.files.base import ContentFile
#
from .tasks import create_random_user_accounts





# this is the main funtion in this applicatio.
# it extends the get_causes function
def index(request):



    create_random_user_accounts()

    # get_free_course('https://www.udemyfreebies.com/course-category/development')
    name = FreeCourses.objects.all()
   


    return render(request, 'index.html', {'name':name})


""""This section is  for the api
that is use in mobile and web.
the api provide CRUD functionality but only the GET method that is exposed
"""

#retrieve all requests from the database
@api_view(['GET'])
def home_api(request):
    data = FreeCourses.objects.all()
    serialized_data = FreeCoursesSerializer(data,many=True)
    return Response(serialized_data.data,status=status.HTTP_200_OK)


# endpoint for development
@api_view(['GET'])
def get_development_courses(request):
    query = FreeCourses.objects.all().filter(category__exact="Development")
    serialize_data = FreeCoursesSerializer(query,many=True)
    return Response(serialize_data.data,status=status.HTTP_200_OK)


@api_view(["GET"])
def get_design_courses(request):
    data = FreeCourses.objects.all().filter(category__exact="Design")
    serialize_data = FreeCoursesSerializer(data,many=True)
    return Response(serialize_data.data,status=status.HTTP_200_OK)


@api_view(["GET"])
def get_software_and_it_courses(request):
    data = FreeCourses.objects.all().filter(category__exact="IT and Software")
    serialize_data = FreeCoursesSerializer(data,many=True)
    return Response(serialize_data.data,status=status.HTTP_200_OK)


@api_view(["GET"])
def get_finance_and_accounting_courses(request):
    data = FreeCourses.objects.all().filter(category__exact="Finance and Accounting")
    serialize_data = FreeCoursesSerializer(data,many=True)
    return Response(serialize_data.data,status=status.HTTP_200_OK)


@api_view(["GET"])
def get_health_and_fitness_courses(request):
    data = FreeCourses.objects.all().filter(category__exact="Health and Fitness")
    serialize_data = FreeCoursesSerializer(data,many=True)
    return Response(serialize_data.data,status=status.HTTP_200_OK)

@api_view(["GET"])
def get_marketing_courses(request):
    data = FreeCourses.objects.all().filter(category__exact="Marketing")
    serialize_data = FreeCoursesSerializer(data,many=True)
    return Response(serialize_data.data,status=status.HTTP_200_OK)


@api_view(["GET"])
def get_business_courses(request):
    data = FreeCourses.objects.all().filter(category__exact="Business")
    serialize_data = FreeCoursesSerializer(data,many=True)
    return Response(serialize_data.data,status=status.HTTP_200_OK)


# an extra api query
# we did not implement the following on our front end
# Add course to the database using
# retrieve a single requests from the database using the id
#
#
#
#
@api_view(['GET'])
def course_detail(request,pk):
    course =FreeCourses.objects.get(id=pk)
    serialize_course = FreeCoursesSerializer(course,many=False)
    return Response(serialize_course.data)


# Add course to the database using
@api_view(['POST'])
def add_course(request):
    course = request.data
    serialized_course = FreeCoursesSerializer(data=course)

    if serialized_course.is_valid():
        serialized_course.save()
        return Response({"message":"successfully added"})


# update course details
@api_view(['PUT'])
def update_course(request,pk):
    course = FreeCourses.objects.get(id=pk)
    serialized_course = FreeCoursesSerializer(instance=course,data=request.data)
    if serialized_course.is_valid():
        serialized_course.save()
        return Response({"message":"successfully updated"})
    return Response({"message": "something went wrong"})


# delete a single course
@api_view(['DELETE'])
def delete_course(request,pk):
    course = FreeCourses.objects.get(id=pk)
    course.delete()
    return Response({"message":"successfully deleted"})
