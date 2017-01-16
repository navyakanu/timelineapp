from flask import  Flask
app =Flask(__name__)

@app.route('/todoapp')
def page_entry():
    return 'Todo Application'
