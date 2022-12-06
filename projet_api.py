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

# fonction pour créer l'url à partir d'un individu(donné dans une liste)
def Create_url(i):
    return f'http://127.0.0.1:5000/search?ptn={i[0]}&time={i[1]}&numm={i[2]}&numd={i[3]}&nbp={i[4]}&nbpa={i[5]}&nbe={i[6]}&racee={i[7]}&gendee={i[8]}&agee={i[9]}&maxe={i[10]}&A1Cresulte={i[11]}&metf={i[12]}&glipe={i[13]}&glybe={i[14]}&piogle={i[15]}&rosige={i[16]}&inse={i[17]}&changee={i[18]}&diabe={i[19]}'


# fonction principale, recupère les paramètres de l'url, charge puis entraine le modèle avec et renvoie un json sur la page avec le résultat du modèle 
@app.route('/search', methods=['GET'])
def search():
    args = request.args
    # récupération des paramètres
    patient_nbr = args.get('ptn')
    time_in_hospital = args.get('time')
    num_medications = args.get('numm')
    number_diagnoses = args.get('numd')
    nb_procedures = args.get('nbp')
    nb_patients = args.get('nbpa')
    nb_encounter = args.get('nbe')
    race_enc = args.get('racee')
    gender_enc = args.get('gendee')
    age_enc = args.get('agee')
    max_glu_serum_enc = args.get('maxe')
    A1Cresult_enc = args.get('A1Cresulte')
    metformin_enc = args.get('metf')
    glipizide_enc = args.get('glipe')
    glyburide_enc = args.get('glybe')
    pioglitazone_enc = args.get('piogle')
    rosiglitazone_enc = args.get('rosige')
    insulin_enc = args.get('inse')
    #http://127.0.0.1:5000/search?ptn=135&time=3&numm=14&numd=5&nbp=32&racee=1&gender_enc=0&agee=5&maxe=2&A1Cresulte=2&inse=1
    change_enc = args.get('changee')
    diabetesMed_enc = args.get('diabe')
    PredictionMade = model.predict([[time_in_hospital, num_medications, number_diagnoses, nb_procedures,nb_patients,nb_encounter,race_enc,gender_enc,age_enc,max_glu_serum_enc,A1Cresult_enc,metformin_enc,glipizide_enc,glyburide_enc,pioglitazone_enc,rosiglitazone_enc,insulin_enc,change_enc,diabetesMed_enc]])
    return jsonify({'Resultat':str(PredictionMade[0])})
    #return jsonify({'patient_nbr':patient_nbr,'time_in_hospital':time_in_hospital,'num_medications':num_medications,'number_diagnoses' : number_diagnoses,'nb_procedures':nb_procedures,'nb_patients':nb_patients,'nb_encounter':nb_encounter,'race_enc':race_enc,'gender_enc':gender_enc,'age_enc':age_enc,'max_glu_serum_enc':max_glu_serum_enc,'A1Cresult_enc':A1Cresult_enc,'metformin_enc':metformin_enc,'glipizide_enc':glipizide_enc,'glyburide_enc':glyburide_enc, 'pioglitazone_enc':pioglitazone_enc,'rosiglitazone_enc': rosiglitazone_enc,'insulin_enc':insulin_enc,'change_enc':change_enc,'diabetesMed_enc':diabetesMed_enc})

if __name__ == '__main__':
    app.run()