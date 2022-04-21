from manageFiles import create_table, insert_data, import_files
from compress import compress
from flask import Flask, send_from_directory
from iosActions import make_dir, remove_dir

app = Flask(__name__)
@app.route('/', methods=["POST"])
def scangen():    
    path = "./Arquivos/"
    path_patterns ="./Patterns/" 
    
    make_dir(path) # Cria uma pasta ou deleta os arquivos de uma existente.
    make_dir(path_patterns)

    ## Função para import os arquivos
    import_files(path)

    name_index = 0
    # Gera uma tabela com dos os valores dos arquivos importados.
    table = create_table(path)

    # Agrupa os dados gerados em arquivos de 10 em 10.
    while name_index < len(table):
        name_index = insert_data(name_index, table, path_patterns)

    # Realiza a compressão dos arquivos Gerados em um zip
    zip_file = compress(path_patterns)

    remove_dir(path) # Deleta os arquivos de uma existente e a pasta.
    remove_dir(path_patterns)

    # Retorna o arquivo .zip para o usuário.
    return send_from_directory('./', zip_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)