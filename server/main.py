import glob
import shutil
import os
import zipfile
import subprocess

source_path = "..\source\*"
destination_path = "..\destination"
post_fix = [1, 2, 3]


source_obj = glob.glob(source_path)
source_files = os.listdir('../source/')
source_obj_path=None
for file in source_obj:
    if file.endswith('.py'):
      # exec(file)
        subprocess.call(["python",file])
        os.remove(file)
    elif file.endswith('.txt'):
        source_obj_path =file


shutil.copy(source_obj_path, '.')
obj_name = source_obj_path.split('\\')[-1].split('.')  # something.txt #sudhu split e backslash
prefix = obj_name[0]  # something
postfix = obj_name[1]  # txt

zipping=zipfile.ZipFile("Zip_file.zip","a")
for item in range(1, len(postfix)+1):
  filename = prefix + '_' + str(item) + '.' + postfix                 

  with open(source_obj_path, 'r') as f:
    lines = f.readlines()
    if item==1:                        
     lines = lines[:item*10]
    elif item==2:
      lines = lines[10:20]
    elif item==3:
      lines = lines[20:30]
    with open(f"./{filename}", 'w') as f:
      f.writelines(lines)
    zipping.write(filename)
zipping.close()  
Zip_file_path="Zip_file.zip"


shutil.copy(Zip_file_path,destination_path)
destination_obj = glob.glob(f"{destination_path}\*")

destination_obj_path=destination_obj[0]




with zipfile.ZipFile("../destination/Zip_file.zip", 'r') as zObj:
            zObj.extractall(path='../destination')
          
os.remove("../destination/Zip_file.zip")
server='./*'
server_obj=glob.glob(server)
for file in server_obj:
    if file.endswith('.txt') or file.endswith('.zip'):
      os.remove(file)



  

