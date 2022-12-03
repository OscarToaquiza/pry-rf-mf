from flask import Flask,jsonify,request
import face_recognition
from datetime import datetime
import numpy as np
from PIL import Image
import base64
import json

from utils.cronometer import Cronometer

app = Flask(__name__)

@app.route('/')
def get_movies():
    return "<h1>Page MashkaSoft MashkaFutbol 1.0.0</h1>" , 404

@app.route('/api/person/recognition', methods=['POST'])
def post_data():
    try:
        print("Reconociendo ...")

        hora_inicio = datetime.now()
        file = request.files['foto']
        img = Image.open(file.stream)

        data = file.stream.read()
        #data = base64.encodebytes(data)
        # print(data)
        data = base64.b64encode(data).decode()
        #print(data)

        unknown_image = face_recognition.load_image_file(file)
        unknown_encoding = face_recognition.face_encodings(unknown_image)

        if( len(unknown_encoding) == 0 ):
            print(unknown_encoding)
            return jsonify({
                'msg': 'error - no se encontro rostros en la img',
                'name': 'No data',
                'time': 0,
                'size': [img.width, img.height], 
                'format': img.format,
                #'img': data
           })

        unknown_encoding = unknown_encoding[0]

        with open('./utils/base_datos_encoding.json') as file:
            dataJson = json.load(file)
            nombre = "Desconocido_0000000000"
            for d in dataJson:
                encoding = np.array(dataJson[d])
                results = face_recognition.compare_faces(
                    [encoding], unknown_encoding, tolerance=0.5)
                if (results[0]):
                    nombre = d

        tiempo = Cronometer.obtener_tiempo_transcurrido_formateado(hora_inicio)

        return jsonify({
                'msg': 'success',
                'name': nombre,
                'time': tiempo,
                'size': [img.width, img.height], 
                'format': img.format,
                'img': data
           })

    except Exception as ex:
        print( str(ex) )
        return jsonify({'msg': str(ex)}), 500


if __name__ == '__main__':
    app.run(debug=True)

