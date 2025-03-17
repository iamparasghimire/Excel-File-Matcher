from django.shortcuts import render
from .forms import ExcelUploadForm
from .logic import match_excel_files

def match_excel_view(request):
    """View to handle file upload and display matching rows."""
    
    form = ExcelUploadForm()
    result = None  # Store match count
    matching_rows = None  # Store matching data as HTML

    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file1 = request.FILES["file1"]
            file2 = request.FILES["file2"]

            # Get match count and table from logic.py
            result, matching_rows = match_excel_files(file1, file2)

    return render(request, "myapp/match_excel.html", {"form": form, "result": result, "matching_rows": matching_rows})
