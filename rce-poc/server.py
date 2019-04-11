from flask import Flask, redirect, request
from flask import render_template, url_for
import os
import time
import subprocess
from werkzeug.utils import secure_filename
import shutil


app = Flask("Simple-Web-Server")

@app.route('/', methods=['GET', 'POST'])
def imagenet():
    if request.method == 'GET':
        return render_template('pagina.html')

    elif request.method == 'POST':
        filename = request.form['text']
 
        process = subprocess.Popen('touch {}'.format(filename),\
                                                    shell=True, \
                                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                                    stderr=subprocess.PIPE)
                                                                
        prediction = process.stdout.read().decode("utf-8") 
        err = process.stderr.read()

        return '<h1>Arquivo {} criado!: <br></br>\
        {}<h1> <br></br>'.format(filename, prediction)





if __name__ == '__main__':

    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
