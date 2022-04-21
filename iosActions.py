import os

def find_files(path): # Encontra os arquivos existentes dentro de uma diretorio especifica.
    try:
        return os.listdir(path)
    except Exception as e:
        pass

def del_files(local, files): # Remove todos os arquivos dentro de umas diretorio especifica.
    if files:
        for file in files:
            os.remove(local + file)

def make_dir(local): # Cria uma diretorio se não existir.
    if not os.path.isdir(local):
        os.makedirs(local)
        return
    else:
        files = find_files(local)
        del_files(local, files)

def remove_dir(local): # Deleta todos os aqueivos da diretorio e deleta o diretorio
    files = find_files(local)
    del_files(local, files)
    os.rmdir(local)
