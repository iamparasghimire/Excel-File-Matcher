Django Excel File Matcher

📌 Project Overview

This Django web application allows users to upload two Excel files and check how many rows match between them. It displays both the matching row count and the matching rows in a table.

🛠 Technologies Used

Django (Python Web Framework)

Pandas (Data Processing)

OpenPyXL (Excel File Handling)

Bootstrap (For Styling, Optional)


🚀 Installation & Setup

1️⃣ Clone the Repository

git clone git@github.com:iamparasghimire/Excel-File-Matcher.git
cd django-excel-matcher

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate 

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run Migrations

python manage.py migrate

5️⃣ Start the Django Server

python manage.py runserver

Now, open http://127.0.0.1:8000/match/ in your browser.

📥 How to Use

Upload two Excel files (.xlsx)

Click Submit

View the count of matching rows and the matching rows in a table

📄 Key Files

File

Description

logic.py

Function to process and match Excel files

views.py

Handles file upload and renders output

match_excel.html

User interface for file upload and result display
