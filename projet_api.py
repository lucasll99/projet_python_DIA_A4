import flask
import io
import string
import time
import os
from pathlib import Path
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, jsonify, request  
import joblib

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
MODELS = os.path.join(BASE_DIR)
MODEL_FILE = os.path.join(MODELS, "LogisticRegression.joblib")
model = joblib.load(MODEL_FILE)
 

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    patient_nbr = args.get('ptn')
    time_in_hospital = args.get('time')
    num_medications = args.get('numm')
    number_diagnoses = args.get('numd')
    nb_procedures = args.get('nbp')
    race_enc = args.get('racee')
    gender_enc = args.get('gender_enc')
    age_enc = args.get('agee')
    max_glu_serum_enc = args.get('maxe')
    A1Cresult_enc = args.get('A1Cresulte')
    insulin_enc = args.get('inse')
    #http://127.0.0.1:5000/search?ptn=135&time=3&numm=14&numd=5&nbp=32&racee=1&gender_enc=0&agee=5&maxe=2&A1Cresulte=2&inse=1
    change_enc = args.get('changee')
    diabetesMed_enc = args.get('diabe')
    PredictionMade = model.predict([[patient_nbr, time_in_hospital, num_medications, number_diagnoses, nb_procedures,race_enc,gender_enc,age_enc,max_glu_serum_enc,A1Cresult_enc,insulin_enc,change_enc,diabetesMed_enc]])
    print(PredictionMade[0])
    print(type(number_diagnoses))
    #return jsonify({'result':PredictionMade})
    return jsonify({'Resultat':str(PredictionMade[0])})
    # return jsonify({'patient_nbr':patient_nbr,'time_in_hospital':time_in_hospital,'num_medications':num_medications,'number_diagnoses' : number_diagnoses,'nb_procedures':nb_procedures,'race_enc':race_enc,'gender_enc':gender_enc,'age_enc':age_enc,'max_glu_serum_enc':max_glu_serum_enc,'A1Cresult_enc':A1Cresult_enc,'insulin_enc':insulin_enc,'change_enc':change_enc,'diabetesMed_enc':diabetesMed_enc})


if __name__ == '__main__':
    app.run()