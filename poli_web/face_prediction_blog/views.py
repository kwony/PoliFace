# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import PictureForm
from .models import Picture

def resemble(request):
    # Handle file upload
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            newpic = Picture(picfile=request.FILES['picfile'])
            newpic.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('resemble'))
    else:
        form = PictureForm()  # A empty, unbound form

    # Load documents for the list page
    pictures = Picture.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'face_prediction_blog/resemble.html',
        { 'pictures': pictures, 'form': form }
    )

def rank(request):
    return render(request, 'face_prediction_blog/rank.html', {})

def info(request):
    return render(request, 'face_prediction_blog/info.html', {})

def home(request):
    return render(request, 'face_prediction_blog/home.html', {})