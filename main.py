from flask import Flask, render_template, request
from db.dbConfig import *
from db import storage
import json
app = Flask(__name__) 

def upload_image_file(file):

    if not file:
        return None

    public_url = storage.upload_file(
        file.read(),
        file.filename,
        file.content_type
    )
    return public_url

@app.route('/')
def root():
    conexion = ConnectDb()
    query = 'SELECT `imageUrl`,`nameMovie`,movie.`id` FROM image right join movie on movie.id = image.idMovie;'
    result = conexion.Execute(query, False)
    conexion.CloseConnection()
    
    data = []
    for item in result:
        data.append({'imageUrl':item[0],'nameMovie':item[1], 'id':item[2]})

    return render_template('index.html', items=data)

@app.route('/addMovie', methods=['GET', 'POST'])
def addMovie():
    if request.method == 'POST':
        codeMovie = request.form['codeMovie']
        nameMovie = request.form['nameMovie']
        description = request.form['description']
        gender = request.form['gender']

        conexion = ConnectDb()
        query = "INSERT INTO cinema.`movie` (codeMovie,nameMovie,description,gender) VALUES ('{}','{}','{}','{}');".format(codeMovie,nameMovie,description,gender)
        # return query
        result = conexion.Execute(query,True)
        conexion.CloseConnection()

        return render_template('index.html', status=result)

@app.route('/addImage', methods=['GET', 'POST'])
def addImage():
    if request.method == 'POST':

        data = request.form.to_dict(flat=True)
        # [START image_url]
        image_url = upload_image_file(request.files.get('image'))
        # [END image_url]
        idMovie = data['idMovie']
        conexion = ConnectDb()
        query = "INSERT INTO cinema.`image` (idMovie,imageUrl) VALUES ('{}','{}');".format(idMovie,image_url)
        # return query
        result = conexion.Execute(query,True)
        conexion.CloseConnection()
        return render_template('index.html', images=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
