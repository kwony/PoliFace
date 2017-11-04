# -*- coding: utf-8 -*-

from django import forms

# 정치인 사진 업로드 용
class PictureForm(forms.Form):
    picfile = forms.FileField(
        label='Select a file'
    )

# 정치인 대량 업로드 시 필요
class PoliticianListForm(forms.Form):
    excelfile = forms.FileField(
        label='excel file'
    )