from django.shortcuts import render
from .forms import ExcelUploadForm
from .logic import match_excel_files

def match_excel_view(request):
    """View to handle file upload and matching process."""

    form = ExcelUploadForm()
    result = None  # Store match result

    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file1 = request.FILES["file1"]
            file2 = request.FILES["file2"]

            # Call function from logic.py
            result = match_excel_files(file1, file2)

    return render(request, "match_excel.html", {"form": form, "result": result})
