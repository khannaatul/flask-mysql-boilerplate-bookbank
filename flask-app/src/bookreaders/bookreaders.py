from flask import Blueprint, request, jsonify, make_response
import json
from src import db


bookreaders = Blueprint('bookreaders', __name__)

# Get all bookreaders from the BookBank
@bookreaders.route('/bookreaders', methods=['GET'])
def get_bookreaders():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT userid,\
       first, last, email, username FROM BookReader')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get bookreader detail for bookreader with particular userid
@bookreaders.route('/bookreaders/<userid>', methods=['GET'])
def get_bookreader(userid):
    cursor = db.get_db().cursor()
    cursor.execute('select * from BookReader where id = {0}'.format(userid))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response