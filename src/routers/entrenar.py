# Planos de flask
from flask import Blueprint, jsonify
import face_recognition
from datetime import datetime
import os
import json

from utils.cronometer import Cronometer

main = Blueprint('entrenar_blueprint', __name__)


@main.route('/')
def train_data():
    
    # hora_inicio = datetime.now()
    # imageFacesPath = "./utils/base_imgs_pry"
    # data = {}
    # num_data_train = 0
    # print("Entrenando ...")
    # for file_name in os.listdir(imageFacesPath):
    #     known_image = face_recognition.load_image_file(imageFacesPath + "/" + file_name)
    #     encoding = face_recognition.face_encodings(known_image)[0]
    #     data[file_name.split(".")[0]] = encoding.tolist()
    #     num_data_train = num_data_train + 1 

    # # Generar ficheros db
    # print("Generando data base ...")
    # with open('./utils/base_datos_encoding.json', 'w') as outfile:
    #     json.dump(data, outfile)

    # tiempo = Cronometer.obtener_tiempo_transcurrido_formateado(hora_inicio)
    # print(tiempo)

    # return jsonify({
    #     "msg": str(num_data_train) + " datos entrenados.",
    #     "time": str(tiempo)
    # })

    return jsonify({
        "msg":"El ambiente de prod no e entrenaara",
        "time": 0
    })