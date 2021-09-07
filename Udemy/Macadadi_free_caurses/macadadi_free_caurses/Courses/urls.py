
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/',views.home_api,name='apihome'),
    path('api/development',views.get_development_courses,name='apihome'),
    path('api/design',views.get_design_courses,name='deign'),
    path('api/software',views.get_software_and_it_courses,name='software'),
    path('api/finance',views.get_finance_and_accounting_courses,name='finance'),
    path('api/fitness',views.get_health_and_fitness_courses,name='fitness'),
    path('api/marketing',views.get_marketing_courses,name='marketing'),
    path('api/business',views.get_business_courses,name='business'),
    path('api/<str:pk>',views.course_detail,name='details'),
    path('add/',views.add_course,name='add'),
    path('update/<str:pk>',views.update_course,name='update'),
    path('delete/<str:pk>',views.delete_course,name="delete")


]