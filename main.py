import os, shutil

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

print(list_of_files1)


# os.rename("/home/rinoreinz/example/ковер_белый_1.txt", "/home/rinoreinz/example/1/ковер_белый_1.txt")

# def sort_files(folder_path):
#     file_paths = get_file_paths(folder_path)
#     ext_list = list(extensions.items())
#
#     for file_path in file_paths:
#         extension = file_path.split('.')[-1]
#         file_name = file_path.split('\\')[-1]
#
#         for dict_key_int in range(len(ext_list)):
#             if extension in ext_list[dict_key_int][1]:
#                 print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
#                 os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')








# if __name__ == '__main__':

