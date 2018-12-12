from flask import Flask, render_template
from db.dbConfig import *
import json
app = Flask(__name__) 

@app.route('/')
def root():
    conexion = ConnectDb()
    query = 'SELECT `imageUrl` FROM image;'
    result = conexion.Execute(query)
    conexion.CloseConnection()
    
    data = []
    for item in result:
        data.append({'imageUrl':item[0]})

    return render_template('index.html', times=data)

@app.route('/addMovie', methods=['GET', 'POST'])
def addMovie():
    pass


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
