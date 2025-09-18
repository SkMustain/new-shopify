from rest_framework import viewsets, permissions

from .models import Subject, TutorProfile, StudentProfile, Availability, Lesson
from .serializers import (
    SubjectSerializer,
    TutorProfileSerializer,
    StudentProfileSerializer,
    AvailabilitySerializer,
    LessonSerializer,
)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by("name")
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny]


class TutorProfileViewSet(viewsets.ModelViewSet):
    queryset = TutorProfile.objects.select_related("user").prefetch_related("subjects").all()
    serializer_class = TutorProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.select_related("user").all()
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.select_related("tutor", "tutor__user").all()
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.select_related(
        "tutor",
        "tutor__user",
        "student",
        "student__user",
        "subject",
    ).all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
