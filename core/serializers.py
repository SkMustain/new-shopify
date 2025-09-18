from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Subject, TutorProfile, StudentProfile, Availability, Lesson


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description']


class TutorProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=False, queryset=get_user_model().objects.all())
    subjects = serializers.PrimaryKeyRelatedField(many=True, queryset=Subject.objects.all(), required=False)

    class Meta:
        model = TutorProfile
        fields = ['id', 'user_id', 'bio', 'hourly_rate', 'subjects']


class StudentProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=False, queryset=get_user_model().objects.all())

    class Meta:
        model = StudentProfile
        fields = ['id', 'user_id', 'grade_level']


class AvailabilitySerializer(serializers.ModelSerializer):
    tutor_id = serializers.PrimaryKeyRelatedField(source='tutor', read_only=False, queryset=TutorProfile.objects.all())

    class Meta:
        model = Availability
        fields = ['id', 'tutor_id', 'day_of_week', 'start_time', 'end_time']


class LessonSerializer(serializers.ModelSerializer):
    tutor_id = serializers.PrimaryKeyRelatedField(source='tutor', read_only=False, queryset=TutorProfile.objects.all())
    student_id = serializers.PrimaryKeyRelatedField(source='student', read_only=False, queryset=StudentProfile.objects.all())
    subject_id = serializers.PrimaryKeyRelatedField(source='subject', read_only=False, queryset=Subject.objects.all())

    class Meta:
        model = Lesson
        fields = [
            'id',
            'tutor_id',
            'student_id',
            'subject_id',
            'start_at',
            'end_at',
            'status',
            'price',
            'notes',
            'created_at',
            'updated_at',
        ]
