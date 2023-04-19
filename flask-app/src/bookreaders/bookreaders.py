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



@ookreaders.route('/newbookreaders', methods = ['POST'])
def add_bookreader():

    the_data = request.json
    current_app.logger.info(the_data)

    first = the_data['bookreader_first']
    last = the_data['bookreader_last']
    email = the_data['bookreader_email']
    username = the_data['bookreader_username']
    password = the_data['bookreader_password']
    city = the data['bookreader_city']
    state = the data['bookreader_state']
    zip = the data['bookreader_zip']

    query = 'Insert into bookreader (first, last, email, username, password, city, state, zip) values(" '
    query += first  + ' " , " ' 
    query += last + ' " , ' 
    query += email + ' " , ' 
    query += username + ' " , '
    query += password + ' " , '  
    query += city + ' " , ' 
    query += state + ' " , ' 
    query += zip +  ')'

    current_app.logger.info(query)


    # executing and commitimg the insert statement
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(query)

    #send commit command to database
    db.get_db().commit()

    return 'Success'



#delete bookreader
@app.route("/bookreaders/<bookid>", methods=["DELETE"])
def bookreader_delete(userid):
    bookreader = BookReader.query.get(userid)
    db.session.delete(bookreader)
    db.session.commit()
    return "BookReader was successfully deleted"