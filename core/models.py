from django.db import models
from django.conf import settings


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class TutorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tutor_profile")
    bio = models.TextField(blank=True)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    subjects = models.ManyToManyField(Subject, related_name="tutors", blank=True)

    def __str__(self) -> str:
        return f"TutorProfile<{self.user.username}>"


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    grade_level = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return f"StudentProfile<{self.user.username}>"


class Availability(models.Model):
    class Weekday(models.IntegerChoices):
        MONDAY = 0, "Monday"
        TUESDAY = 1, "Tuesday"
        WEDNESDAY = 2, "Wednesday"
        THURSDAY = 3, "Thursday"
        FRIDAY = 4, "Friday"
        SATURDAY = 5, "Saturday"
        SUNDAY = 6, "Sunday"

    tutor = models.ForeignKey(TutorProfile, on_delete=models.CASCADE, related_name="availabilities")
    day_of_week = models.PositiveSmallIntegerField(choices=Weekday.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ["tutor", "day_of_week", "start_time"]
        unique_together = ("tutor", "day_of_week", "start_time", "end_time")

    def __str__(self) -> str:
        return f"{self.tutor.user.username} - {self.get_day_of_week_display()} {self.start_time}-{self.end_time}"


class Lesson(models.Model):
    class Status(models.TextChoices):
        REQUESTED = "REQUESTED", "Requested"
        CONFIRMED = "CONFIRMED", "Confirmed"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    tutor = models.ForeignKey(TutorProfile, on_delete=models.CASCADE, related_name="lessons")
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="lessons")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="lessons")
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.REQUESTED)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-start_at"]

    def __str__(self) -> str:
        return f"Lesson<{self.subject.name} {self.start_at} - {self.end_at}>"
