from django.contrib import admin
from .models import Vocabulary, Verb, TenseCategory, Conjugaison
# Register your models here.
admin.site.register(Vocabulary)
admin.site.register(Verb)
admin.site.register(TenseCategory)
admin.site.register(Conjugaison)
