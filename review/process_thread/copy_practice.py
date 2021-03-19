import os
import multiprocessing


def copy_file(file_name, src, dest):
    src_path = src + "/" + file_name
    dest_path = dest + "/" + file_name
    with open(src_path, mode='rb') as src_f:
        with open(dest_path, mode='wb') as dest_f:
            while True:
                data = src_f.read(1024)
                if data:
                    dest_f.write(data)
                else:
                    break

    print('a over')


if __name__ == '__main__':
    src = "./src"
    dest = "./dest"

    try:
        os.mkdir(dest)

    except:
        print("dest already exists!")

    file_list = os.listdir(src)

    for file in file_list:
        # copy_file(file, src, dest)
        cp_p = multiprocessing.Process(target=copy_file, args=(file, src, dest))
        cp_p.start()


    print('main over')




