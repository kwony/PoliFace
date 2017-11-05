# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import PictureForm, PoliticianListForm
from .models import Picture, Politician, Politician_List_File
from .facepredict import predict

import xlrd

def resemble(request):
    # Handle file upload
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            newpic = Picture(picfile=request.FILES['picfile'])
            newpic.save()

            # Predict image in politician list.
            predict(newpic.picfile.name)

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

    politicians = Politician.objects.all()

    form = PoliticianListForm()

    return render(request, 'face_prediction_blog/info.html', {'politicians': politicians, 'form':form})

def info_detail(request):

    return render(request, 'face_prediction_blog/info.html', {})

def info_upload_politician_list(request):
    if request.method == 'POST':
        form = PoliticianListForm(request.POST, request.FILES)
        if form.is_valid():
            new_list = Politician_List_File(excelfile=request.FILES['excelfile'])
            new_list.save()

            politician_list = xlrd.open_workbook('face_prediction_blog/media/excel/' + request.FILES['excelfile'].name).sheet_by_index(0)

            num_rows = politician_list.nrows

            current_row = 1

            while current_row < num_rows:
                col_data = politician_list.row_values(current_row)
                
                politician = Politician(name=col_data[1], eng_name=col_data[2], born_year=col_data[3], party=col_data[4], job=col_data[5], political_preference=col_data[6], region=col_data[7], namu_link=col_data[8], short_history=col_data[9])
                politician.save()

                current_row += 1
            
            return render(request, 'face_prediction_blog/info.html', {})



def home(request):
    return render(request, 'face_prediction_blog/home.html', {})