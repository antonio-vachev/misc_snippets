import os
import glob
import pandas as pd

# Add the directory for the single .CSV files
single_files_dir = r"T:\02.PRELIMINARY\_templates\DYNAMO LOG FILE DUMP\01_Combined\2022\2022_05_May\01_Single_Files"

# Add the directory for the combined file
combined_files_dir = r"T:\02.PRELIMINARY\_templates\DYNAMO LOG FILE DUMP\01_Combined\2022\2022_05_May\02_Combined_File"

# Add naming for combined .csv and .xlsx files
combined_csv_dir = combined_files_dir + r"\Data.csv"
combined_xlsx_dir = combined_files_dir + r"\Combined_Logs.xlsx"

# Look for .csv files in directory
os.chdir(single_files_dir)
extension = "csv"
all_filenames = [i for i in glob.glob("*.{}".format(extension))]

# Combine single .csv files to one .csv file
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv(combined_csv_dir, index=False, encoding="utf-8-sig")

# Add .csv file to .xlsx
read_file = pd.read_csv(combined_csv_dir)
read_file.to_excel(combined_xlsx_dir, index=None, header=True)
