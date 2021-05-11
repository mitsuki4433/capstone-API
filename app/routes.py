from app import app
from app.controller import MakananController


@app.route('/')
def index():
    return "Hello"


@app.route('/makanan', methods=['GET'])
def makanans():
    return MakananController.index()


@app.route('/makanan/<id>', methods=['GET'])
def makanansDetail(id):
    return MakananController.detail(id)
