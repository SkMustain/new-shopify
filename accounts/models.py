from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TUTOR = "TUTOR", "Tutor"
        STUDENT = "STUDENT", "Student"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    phone_number = models.CharField(max_length=32, blank=True)

    @property
    def is_tutor(self) -> bool:
        return self.role == self.Role.TUTOR

    @property
    def is_student(self) -> bool:
        return self.role == self.Role.STUDENT

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"

    def save(self, *args, **kwargs):
        # Normalize role strings if provided in lowercase
        if isinstance(self.role, str):
            self.role = self.role.upper()
        super().save(*args, **kwargs)
