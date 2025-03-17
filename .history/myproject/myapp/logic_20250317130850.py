import pandas as pd

def match_excel_files(file1, file2):
    """Function to match two Excel files and count matching rows."""
    try:
        # Read the Excel files into Pandas DataFrames
        df1 = pd.read_excel(file1)
        df2 = pd.read_excel(file2)

        # Find common rows between both DataFrames
        common_rows = df1.merge(df2, how='inner')

        return len(common_rows)  # Return number of matching rows
    except Exception as e:
        return str(e)  # Return error message if something goes wrong
