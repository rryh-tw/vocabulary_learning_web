from django.contrib import messages
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.template import loader
from .models import Vocabulary



def index(request):
    vc_list = Vocabulary.objects.all()
    output = ', '.join([vc.word for vc in vc_list])
    template = loader.get_template('index.html')
    context = {
        'vc_list': vc_list,
    }
    return HttpResponse(template.render(context, request))


def autocomplete(request):
    """
    Creates a list of all infinitives and renders as JSON to be consumed by the
    the third party autocomplete feature (auto-complete.js).
    """
    autocomplete_list = list(Verb.objects.values_list('infinitive', flat=True))
    return JsonResponse(autocomplete_list, safe=False)