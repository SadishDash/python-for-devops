import os

files = input("Please enter the files with spaces -> ")
files_list = files.split() # Create a list with all the folder names

for i in files_list:
    try:
        file = os.listdir(i)
    except FileNotFoundError:
        print("Please enter a valid folder name. " + i + " doesnt exist")
        continue
    except PermissionError:
        print("No Access")
        continue
    print("THE FILES IN",i,"FOLDERS ARE")
    # print(file)
    a=0
    for j in file: # since file is alist, for better view printing the list 1 by 1
        a=a+1
        print(str(a) + ". " + j)
    print ("There are total "+ str(len(file)) +" number of files")
