import flask
from flask import request
import json

app = flask.Flask(__name__)




@app.route('/')
@app.route('/index.html')
@app.route('/index')
def root():
    return flask.render_template("index.html", page_title='Sketched | Home')

@app.route('/upload/confirm', methods = ["POST"])
def upload_confirmation():
    return flask.render_template("confirm.html", value = "Upload Received!")

@app.route('/p/<requested_page>')
def templater(requested_page):
    return flask.render_template(requested_page)

@app.route('/submit/confirm', methods=['POST'])
def submit_confirm():
    if request.args.get('url'):
        return "success"
    else:
        return "error"
    
@app.route('/submit/redirConfirm<message>', methods=["GET"])
def submit_confirmation(message):
    return flask.render_template("confirm.html", value = message)


if __name__ == '__main__':
    app.debug = True
    app.run()
    #JUST FOR DEBUGGING
