import os
import zipfile

os.system("wget http://images.cocodataset.org/zips/train2017.zip")
os.system("wget http://images.cocodataset.org/zips/val2017.zip")
os.system("wget http://images.cocodataset.org/zips/test2017.zip")
os.system("wget http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip")
os.system("git clone https://github.com/open-mmlab/mmdetection.git")
os.system("cd mmdetection")
os.system("pip install -r requirements/build.txt")
os.system("pip install ""git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI""")
os.system("pip install -v -e .")
os.system("mkdir data")
os.system("ln -s ./img_data data")
# os.system("")

extract_folder_path = "img_data"

zip_paths = []
zip_paths.append("train2017.zip")
zip_paths.append("val2017.zip")
zip_paths.append("test2017.zip")
zip_paths.append("stuff_annotations_trainval2017.zip")

for path in zip_paths:
    with zipfile.ZipFile(path, 'r') as zip_file:
        zip_file.extractall(extract_folder_path)

# for git
# git config --global user.email "linh9920duy@gmail.com"
# git config --global user.name "duylinh55555"