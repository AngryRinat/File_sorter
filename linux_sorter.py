import os, shutil, sys


def moving_files():
    path = "/home/rinoreinz/example"
    list_of_files = []
    folder_set = set()
    for root, dirs, files in os.walk(path):
        list_of_files += files

    for el in list_of_files:
        folder_name = ('_').join(el.split('_')[:-1])
        if folder_name not in folder_set:
            folder_set.add(folder_name)


    for el in folder_set:
        if not os.path.exists(f"{path}/{str(el)}"):
             os.mkdir(f"{path}/{str(el)}")




    list_of_files1 = []
    for root, dirs, files in os.walk(path):
        list_of_files1 += files

    for file in list_of_files1:
        for set_name in folder_set:
            if set_name in file and os.path.exists(f"{path}/{file}"):
             shutil.copyfile(f"{path}/{file}", f"{path}/{set_name}/{file}")

    for file in list_of_files1:
        if os.path.exists(f"{path}/{file}"):
            os.remove(f"{path}/{file}")




if __name__ == '__main__':

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    moving_files()

