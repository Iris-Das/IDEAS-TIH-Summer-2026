# Change directory to working directory where files are stored
from contextlib import chdir
chdir('C:/Users/idasi/Documents/IDEAS-TIH')

# Import libraries
import xarray as xr
import netCDF4 as nc
import pyarrow as pa
import zipfile
import glob
import os 

# extract netcd4 files from 120 zip files
output_folder = "Unzipped Data"
path = "C:/Users/idasi/Documents/IDEAS-TIH/*.zip"
os.makedirs(output_folder, exist_ok=True)   
zip_files = glob.glob(path)
print(f"Found {len(zip_files)} zip files.")
for zip_file in zip_files:
    zip_name = os.path.splitext(os.path.basename(zip_file))[0]
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for zip_eachfile in zip_ref.namelist():
            temp_path = zip_ref.extract(zip_eachfile, output_folder)
            new_name = f"{zip_name}_{zip_eachfile}"
            new_path = os.path.join(output_folder, new_name)
            os.rename(temp_path, new_path)
        zip_ref.extractall(output_folder)