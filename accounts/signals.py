from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from core.models import TutorProfile, StudentProfile


@receiver(post_save, sender=get_user_model())
def create_profiles_for_user(sender, instance, created, **kwargs):
    if not created:
        return
    # Create profiles depending on role
    if getattr(instance, 'is_tutor', False):
        TutorProfile.objects.get_or_create(user=instance)
    if getattr(instance, 'is_student', False):
        StudentProfile.objects.get_or_create(user=instance)
