from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Question, Answer


@receiver(post_save, sender=Question)
def create_answer(sender, instance, created, **kwargs):
    if created:
        Answer.objects.create(question=instance, user=instance.user)


@receiver(post_save, sender=Question)
def save_answer(sender, instance, **kwargs):
    instance.answer.save()
