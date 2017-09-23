# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import PictureForm
from .models import Picture
from .facepredict import predict

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            newpic = Picture(picfile=request.FILES['picfile'])
            newpic.save()

            # Predict image in politician list.
            predict(newpic.picfile.name)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = PictureForm()  # A empty, unbound form

    # Load documents for the list page
    pictures = Picture.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'face_prediction_blog/index.html',
        { 'pictures': pictures, 'form': form }
    )
