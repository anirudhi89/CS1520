import flask
from flask import request
# from google.cloud import datastore

app = flask.Flask(__name__)

#Constants:

#Datastore Constants:
ENTITY_TYPE = 'StickyNote'


@app.route('/')
@app.route('/index.html')
@app.route('/index')
def root():
    return flask.render_template("index.html", page_title='Sketched | Home')

@app.route('/upload/confirm', methods = ["POST"])
def upload_confirmation():
    # uploaded_file = flask.request.files.get('file')
    # content_type = uploaded_file.content_type
    # gcs_client = storage.Client()
    # storage_bucket = gcs_client.get_bucket('uploaded-stickies')
    # blob = storage_bucket.blob(uploaded_file.filename)
    # blob.upload_from_string(uploaded_file.read(), content_type=content_type)
    # url = blob.public_url
    return flask.render_template("confirm.html", value = "Upload Received!")

@app.route('/p/<requested_page>')
def templater(requested_page):
    return flask.render_template(requested_page)

@app.route('/submit/confirm', methods=['POST'])
def submit_confirm():
    request_json = request.get_json(force=True)
    url = request_json.get("url")
    tags = request_json.get("tags")
    if (tags != null):
        str1 = " "
        str1 = (str1.join(tags))
    if url != None:
        # kind = "StickyNote"
        # name = "sticky"+ random.randint(0, 200)
        # task_key = datastore.client.key(kind,name)
        # task = datastore.Entity(key=task_key)
        # task['url'] = url
        # datastore.put(task)
        return "Success! Image Uploaded" + str1
    else:
        return "Error. Unable to upload image."
    
@app.route('/submit/redirConfirm<message>', methods=["GET"])
def submit_confirmation(message):
    return flask.render_template("confirm.html", value = message)

# @app.route('/get/sketches')
# def get_sketches():
#     request_json = request.get_json(force=True)
#     url = request_json.get("id")
    

# if __name__ == '__main__':
#     app.debug = True
#     app.run()
    #JUST FOR DEBUGGING




#Helper Methods

def get_client():
    return datastore.Client()

def retrieve_item(id):
    client = get_client()
    key = client.key(ENTITY_TYPE, int(id))
    return client.get(key)

def update_item(item):
    client = get_client()
    client.put(item)

def delete_item(id):
    client = get_client()
    key = client.key(ENTITY_TYPE, int(id))
    client.delete(key)

def get_things():
    result = []
    client = get_client()
    query = client.query(kind=ENTITY_TYPE)
    for entity in query.fetch():
        result.append(entity)
    return result



    