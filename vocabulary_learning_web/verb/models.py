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


class Verb(models.Model):
    infinitive = models.CharField(primary_key=True, max_length=30)
    translation = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.infinitive


class TenseCategory(models.Model):
    category = models.CharField(max_length=30)
    tense = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.category} {self.tense}'

class Conjugaison(models.Model):
    verb = models.ForeignKey('Verb', on_delete=models.CASCADE)
    state = models.PositiveSmallIntegerField()
    tense = models.ForeignKey('TenseCategory', on_delete=models.CASCADE)
    je = models.CharField(max_length=30, blank=True)
    tu = models.CharField(max_length=30, blank=True)
    il = models.CharField(max_length=30, blank=True)
    nous = models.CharField(max_length=30, blank=True)
    vous = models.CharField(max_length=30, blank=True)
    ils = models.CharField(max_length=30, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['verb', 'tense'], name='unique_conjugation')
        ]

    def __str__(self):
        return f'{self.verb} {self.tense}'