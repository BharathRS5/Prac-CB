import os
folders = input("Please provide the folder_names: ").split()
# print(folders)

for folder in folders:
    # print(folder)
    os.listdir(folder)




