# -*- coding: utf-8 -*-

from django.shortcuts import render
from .forms import PhotoForm

def home(request):
    return render(request, 'face_prediction_blog/home.html', {})

def upload_pic(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PhotoForm()

    return render(request, 'face_prediction_blog/home.html', {
        'form': form
    })