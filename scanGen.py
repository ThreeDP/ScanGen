from manageFiles import create_table, insert_data
from compress import compress
from flask import Flask, jsonify
from iosActions import make_dir, remove_dir

app = Flask(__name__)

@app.route('/')
def scangen():    
    path = "./Arquivos/"
    path_patterns ="./Patterns/" 
    
    make_dir(path) # Cria uma pasta ou deleta os arquivos de uma existente.
    make_dir(path_patterns)

    name_index = 0
    ## Função para import os arquivos
    table = create_table(path)

    while name_index < len(table):
        name_index = insert_data(name_index, table, path_patterns)

    compress('./')

    # Função para download dos arquivos.
    remove_dir(path) # Deleta os arquivos de uma existente e a pasta.
    remove_dir(path_patterns)

    return 'teste'

if __name__ == "__main__":
    app.run(host='0.0.0.0')