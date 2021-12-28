from django.db import models

# Create your models here.

class Vocabulary(models.Model):
    word = models.CharField(max_length=50, blank=True)
  #  difficulty = models.PositiveSmallIntegerField()
    translation = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['word']

    def __str__(self):
        return self.word