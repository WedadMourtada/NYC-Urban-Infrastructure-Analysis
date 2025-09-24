import zipfile
import os

# Define paths: where the zip files are located and where the extracted CSV files will go
zip_dir = "data/raw/nyiso/zip"
csv_dir = "data/raw/nyiso/csv"

# Make sure the CSV output folder exists (creates it if it doesn’t)
os.makedirs(csv_dir, exist_ok=True)

# Loop through all files in the zip folder
for filename in os.listdir(zip_dir):  # look at every file in the zip directory
    if filename.endswith(".zip"):  # only process files that end with ".zip"
        zip_path = os.path.join(zip_dir, filename)  # get the full path to the zip file

        with zipfile.ZipFile(zip_path, "r") as z:  # open the zip file
            for member in z.namelist():  # go through each item inside the zip
                # Only extract CSV files (ignore other file types, if any)
                if member.endswith(".csv"):
                    out_path = os.path.join(csv_dir, member)  # create output path for CSV
                    print(f"Extracting {member} -> {out_path}")  # show what’s being extracted
                    z.extract(member, csv_dir)  # extract the CSV into the csv directory

print("All NYISO zips extracted to data/raw/nyiso/csv/")
