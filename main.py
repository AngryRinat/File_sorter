import os

list_of_files = []
folder_set = set()
for root, dirs, files in os.walk("/home/rinoreinz/example"):
    list_of_files += files

for el in list_of_files:
    folder_name = ('_').join(el.split('_')[:-1])
    if folder_name not in folder_set:
        folder_set.add(folder_name)

for el in folder_set:
    os.mkdir("/" + str(el))










# if __name__ == '__main__':

