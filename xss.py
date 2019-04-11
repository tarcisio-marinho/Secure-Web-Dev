from flask import Flask, redirect, request
from flask import render_template, url_for, Response
import cgi
import html

app = Flask("Simple-Web-Server")

        
@app.route('/', methods=['GET', 'POST'])
def mnist():
    if request.method == 'GET':
        return render_template('template.html')

    elif request.method == 'POST':
        # if file not send
        text = request.form['file']
        return Response('Ola, ' + text, content_type='text/HTML', headers={'X-XSS-Protection':'0'})

@app.route('/safe-xss', methods=['GET', 'POST'])
def safe():
    if request.method == 'GET':
        return render_template('template.html')

    elif request.method == 'POST':
        # if file not send
        text = request.form['file']
        return Response('Ola, ' + html.escape(text), content_type='text/HTML', headers={'X-XSS-Protection':'0'})



if __name__ == '__main__':

    # Bind to PORT if defined, otherwise default to 5000.
    port = int(5000)
    app.run(host='127.0.0.1', port=port)