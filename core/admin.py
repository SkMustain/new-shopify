from django.contrib import admin

from .models import Subject, TutorProfile, StudentProfile, Availability, Lesson


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(TutorProfile)
class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "hourly_rate")
    search_fields = ("user__username", "user__email")
    filter_horizontal = ("subjects",)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "grade_level")
    search_fields = ("user__username", "user__email")


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("tutor", "day_of_week", "start_time", "end_time")
    list_filter = ("day_of_week",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("tutor", "student", "subject", "start_at", "status", "price")
    list_filter = ("status", "subject")
