from flask import Flask, jsonify, request, render_template
from Domain.intervention import Intervention
from Domain.technicien import Technicien

app = Flask(__name__)

""" add inter """
@app.route('/api/inter/add', methods=['POST'])
def add_inter():

    """get json post"""
    new_inter = request.get_json(force=True)

    """create intervention object with received datas"""
    inter = Intervention()
    inter.createFromJson(new_inter)

    """update database"""
    inter.putInDb()

    return ("OK", {"Content-type": "application/plaintext"})


@app.route('/api/user/<username>')
def ge_user_inters(username):

    list = []
    mytech = Technicien(username)
    mytech.getAllInter()

    for elt in mytech.interventions:
        dico = {}
        dico["libelle"] = elt.libelle
        dico["id_Client"] = elt.id_Client
        list.append(dico)

    return jsonify(list)


if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request, Response
from DataAccess.accessDatabase import AccessDatabase

app = Flask(__name__)

@app.route('/api/interventions')
def get_interventions():
    #Retrieve intervention from database via DataAccess file
    dico = AccessDatabase.select_interventions()
    return jsonify(dico);

@app.route('/api/interventions/add', methods=['POST'])
def post_intervention():
    #add intervention to database via DataAccess file
    intervention = None
    AccessDatabase.insert_intervention(intervention)
    return Response("OK", status= 201, mimetype='application/Json')


if __name__ == '__main__':
    app.run()

