from app.model.makanan import Makanan

from app import response, app, db
from flask import request 

def index():
    try:
        makanan = Makanan.query.all()
        data = formatarray(makanan)
        return response.success(data, "success")
    except Exception as e:
        print(e)

def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i)) 
    
    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'name' : data.name,
        'kalori' : data.kalori
    }

    return data


 
def detail(id):
    try:
        makanan = Makanan.query.filter_by(id=id).first()
        if not makanan:
            return response.badRequest([], 'Tidak ada data makanan')

        data = singleObject(makanan)

        return response.success(data, "success")

    except Exception as e:
        print(e)
