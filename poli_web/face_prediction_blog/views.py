# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import PictureForm
from .models import Picture

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Picture(picfile=request.FILES['picturefile'])
            newdoc.save()

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
