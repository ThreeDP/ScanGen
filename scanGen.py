from manageFiles import create_table, insert_data
from compress import compress
from flask import Flask

app = Flask(__name__) 

@app.route('/')
def scangen():     


    return 'teste'

app.run(host='0.0.0.0')