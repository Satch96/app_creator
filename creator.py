import os
import shutil

name = input("Please enter project name:\n")
type = input("Please enter project type:\nA - Web App\nB - Python Script\n")

#place for project to go
parent_dir = "C:\\Users\\SatchinMistry\\projects"
#current directory
current_path = "C:\\Users\\SatchinMistry\\app_creator\\"

path = os.path.join(parent_dir, name)
os.mkdir(path)

if type == "A":
    project_type = "web_app"
elif type == "B":
    project_type = "python_app"

folder = current_path+project_type
file_list = os.listdir(folder)

for x in file_list:
    shutil.copy(folder+"\\"+x,path)

print("Your project has been created! Please click on the directory below to access!\n"+path)