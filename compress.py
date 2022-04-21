from iosActions import find_files
import zipfile

def compress(path):
    file_name = 'patterns.zip'
    patterns = zipfile.ZipFile('./' + file_name, 'w' ) # Salva o Arquivo no diretorio raiz

    for file in find_files(path):
        patterns.write(path + file, compress_type=zipfile.ZIP_DEFLATED)

    patterns.close()
    return file_name
