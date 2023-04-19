from flask import Blueprint, request, jsonify, make_response,  current_app
import json
from src import db


curators = Blueprint('curators', __name__)

# Get all curators from the BookBank
@curators.route('/curators', methods=['GET'])
def get_bookreaders():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT CuratorID,\
       first, last, email, username FROM Curator')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get curator detail for curator with particular curatorid
@curators.route('/curators/<curatorid>', methods=['GET'])
def get_curator(curatorid):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Curator where CuratorID = {0}'.format(curatorid))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



@curators.route('/newcurators', methods = ['POST'])
def add_curator():

    the_data = request.json
    current_app.logger.info(the_data)

    curatorid = the_data['curator_id']
    first = the_data['curator_first']
    last = the_data['curator_last']
    email = the_data['curator_email']
    username = the_data['curator_username']
    password = the_data['curator_password']
    city = the_data['curator_city']
    state = the_data['curator_state']
    zip = the_data['curator_zip']

    query = 'Insert into Curator (CuratorID, first, last, email, username, password, city, state, zip) values(" '
    query += str(curatorid)  + ' " , " ' 
    query += first  + ' " , " ' 
    query += last + ' " , " ' 
    query += email + ' " , " ' 
    query += username + ' " , " '
    query += password + ' " , " '  
    query += city + ' " , " ' 
    query += state + ' " , " ' 
    query += zip +  ' ")'

    current_app.logger.info(query)


    # executing and commitimg the insert statement
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(query)

    #send commit command to database
    db.get_db().commit()

    return 'Success'



#delete curator
@curators.route("/curatordelete/<curatorid>", methods=["DELETE"])
def curator_delete(curatorid):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE from Curator where CuratorID = {0}'.format(curatorid))
    #send commit command to database
    db.get_db().commit()
    return "Curator was successfully deleted"




# update curator username and password
@curators.route("/curatorupdate/<curatorid>", methods=["PUT"])
def curator_update(curatorid):
    curator = Curator.query.get(curatorid)
    password = request.json['password']

    curator.password = password

    db.session.commit()
    return curator_schema.jsonify(curator)