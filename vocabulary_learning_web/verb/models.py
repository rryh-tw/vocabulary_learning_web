from django.db import models

# Create your models here.

class Vocabulary(models.Model):
    word = models.CharField(primary_key=True, max_length=30)
    difficulty = models.PositiveSmallIntegerField(unique=True)
    translation = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['difficulty']

    def __str__(self):
        return self.word