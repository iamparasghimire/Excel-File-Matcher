import pandas as pd

def match_excel_files(file1, file2):
    """Function to match two Excel files and return matching rows."""
    try:
        # Read the Excel files into Pandas DataFrames
        df1 = pd.read_excel(file1)
        df2 = pd.read_excel(file2)

        # Find matching rows
        common_rows = df1.merge(df2, how='inner')

        # Convert matching rows to HTML for display
        matching_html = common_rows.to_html(classes="table table-bordered", index=False)

        return len(common_rows), matching_html  # Return count and HTML table
    except Exception as e:
        return str(e), None  # Return error message if something goes wrong
