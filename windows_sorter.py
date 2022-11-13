import os, shutil, sys


def moving_files(path):

    folder_list = ["alina", "anis liberica", "berne", "cleo", "dual", "elza", "finesse", "line", "monza", "nero", "olvi", "optima", "relax", "rizo", "snow", "time", "ungaro", "riona bella", "sola blanca"]
    list_of_files1 = []
    for root, dirs, files in os.walk(path):
        if root == path:
            list_of_files1 += files


    for file in list_of_files1:
        for set_name in folder_list:
            _file = file.lower()
            if set_name in _file and os.path.exists(f"{path}/{file}") :
             shutil.copyfile(f"{path}/{file}", f"{path}/{set_name}/{file}")
             if os.path.exists(f"{path}/{file}") and os.path.basename(f"{path}/{file}") != 'windows_sorter.exe':
                 os.remove(f"{path}/{file}")

    # for file in list_of_files1:
    #     print(os.path.basename(f"{path}/{file}"))
    #     if os.path.exists(f"{path}/{file}") and os.path.basename(f"{path}/{file}") != 'windows_sorter.exe':
    #         os.remove(f"{path}/{file}")
    #



if __name__ == '__main__':

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    moving_files(application_path)

