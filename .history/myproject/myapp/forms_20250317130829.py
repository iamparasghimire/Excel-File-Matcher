from django import forms

class ExcelUploadForm(forms.Form):
    file1 = forms.FileField(label="Upload First Excel File")
    file2 = forms.FileField(label="Upload Second Excel File")
