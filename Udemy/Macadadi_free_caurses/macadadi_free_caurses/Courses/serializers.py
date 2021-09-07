from rest_framework import serializers
from .models import FreeCourses


class FreeCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeCourses
        fields = '__all__'
