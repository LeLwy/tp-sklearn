from functools import partial

# serveur.py
from flask import Flask
from apiflask import APIFlask, Schema
from marshmallow.fields import String

class Personne(Schema):
    nom = String(required=True)
    prenom = String(required=False)

class Identifiant(Schema):
    identifiant = String()


# app = Flask("MonNomDeServeur")
app = APIFlask("MonNomDeServeur")

@app.get('/personne/<string:nom>')
@app.output(Identifiant)
def get_identifiant(nom):
    return {"identifiant": nom + "_007"}

@app.post('/personne')
@app.input(Personne(partial=False))
@app.output(Identifiant)
@app.doc(description="CRéation d'une personne",
    responses={200: 'La personne est créée',
               202: 'Une autre personne a déjà le même nom'}
)
def post_personne(json_data):
    p = Personne()
    p.nom = json_data["nom"]
    p.prenom = json_data["prenom"]
    return {"identifiant": p.nom + "_007"}

@app.route("/")
def hello():
    return "<p>Hello</p>"

app.run("0.0.0.0", 9090, True, True)
