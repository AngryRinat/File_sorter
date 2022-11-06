import os, shutil


def moving_files():
    path =
    list_of_files = []
    folder_set = set()
    for root, dirs, files in os.walk("/home/rinoreinz/example"):
        list_of_files += files

    for el in list_of_files:
        folder_name = ('_').join(el.split('_')[:-1])
        if folder_name not in folder_set:
            folder_set.add(folder_name)


    for el in folder_set:
        if not os.path.exists(f"/home/rinoreinz/example/{str(el)}"):
             os.mkdir(f"/home/rinoreinz/example/{str(el)}")




    list_of_files1 = []
    for root, dirs, files in os.walk("/home/rinoreinz/example"):
        list_of_files1 += files

    for file in list_of_files1:
        for set_name in folder_set:
            if set_name in file and os.path.exists(f"/home/rinoreinz/example/{file}"):
             shutil.copyfile(f"/home/rinoreinz/example/{file}", f"/home/rinoreinz/example/{set_name}/{file}")

    for file in list_of_files1:
        if os.path.exists(f"/home/rinoreinz/example/{file}"):
            os.remove(f"/home/rinoreinz/example/{file}")




if __name__ == '__main__':
    moving_files()

