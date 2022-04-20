import os

def find_files(local):
    try:
        return os.listdir(local)
    except Exception as e:
        print(e)

def del_files(local, files):
    if files:
        for file in files:
            os.remove(local + file)

def make_dir(local):
    if not os.path.isdir(local):
        os.makedirs(local)
        return
    else:
        files = find_files(local)
        del_files(local, files)

def remove_dir(local):
    files = find_files(local)
    del_files(local, files)
    os.rmdir(local)
