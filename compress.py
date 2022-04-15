from iosActions import find_files
import zipfile

def compress(path):
    patterns = zipfile.ZipFile(path + 'patterns.zip', 'w' )
    for file in find_files(path):
        patterns.write(path + file, compress_type=zipfile.ZIP_DEFLATED)

    patterns.close()
