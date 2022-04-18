from manageFiles import create_table, insert_data
from compress import compress
from flask import Flask

app = Flask(__name__) 

@app.route('/')
def scangen():     
    name_index = 0
    table = create_table()

    while name_index < len(table):
        name_index = insert_data(name_index, table)

    compress('./')

    return 'teste'

app.run(host='0.0.0.0')