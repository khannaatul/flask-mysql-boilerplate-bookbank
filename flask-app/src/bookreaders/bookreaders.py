from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


bookreaders = Blueprint('bookreaders', __name__)

#Get all bookreaders from the BookBank
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

#Get bookreader detail for bookreader with particular userid
@bookreaders.route('/bookreaders/<userid>', methods=['GET'])
def get_bookreader(userid):
    cursor = db.get_db().cursor()
    cursor.execute('select * from BookReader where userid = {0}'.format(userid))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



@bookreaders.route('/newbookreaders', methods = ['POST'])
def add_bookreader():

    the_data = request.json
    current_app.logger.info(the_data)

    userid = the_data['bookreader_id']
    first = the_data['bookreader_first']
    last = the_data['bookreader_last']
    email = the_data['bookreader_email']
    username = the_data['bookreader_username']
    password = the_data['bookreader_password']
    city = the_data['bookreader_city']
    state = the_data['bookreader_state']
    zip = the_data['bookreader_zip']

    query = 'Insert into BookReader (userID, first, last, email, username, password, city, state, zip) values(" '
    query += str(userid)  + ' " , " '
    query += first  + ' " , " ' 
    query += last + ' " , " ' 
    query += email + ' " , " ' 
    query += username + ' " , " '
    query += password + ' " , " '  
    query += city + ' " , " ' 
    query += state + ' " , " ' 
    query += zip +  ' ")'

    current_app.logger.info(query)


    #executing and commitimg the insert statement
    #get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(query)

    #send commit command to database
    db.get_db().commit()

    return 'Success'



#delete bookreader
@bookreaders.route("/bookreadersdelete/<userid>", methods=["DELETE"])
def bookreader_delete(userid):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE from BookReader where userid = {0}'.format(userid))
    #send commit command to database
    db.get_db().commit()
    return "BookReader was successfully deleted"


 #update bookreader password
@bookreaders.route("/bookreadersupdate/<userid>", methods=["PUT"])
def bookreader_update(userid):
    newpassword = request.json['password']
    cursor = db.get_db().cursor()

    query = "UPDATE BookReader SET password = '%s' WHERE userid = '%s'"%(newpassword,userid)

    cursor.execute(query)
    #send commit command to database
    db.get_db().commit()
    return  "BookReader password was successfully updated"

#get first 5 bookreaders
@bookreaders.route('/first5')
def get_first_bookreaders():
    cursor = db.get_db().cursor()
    query = '''
        SELECT first, last, username, email
        FROM BookReader
        ORDER BY userid 
        LIMIT 5
    '''
    cursor.execute(query)
    #grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    #create an empty dictionary object to use in 
    #putting column headers together with data
    json_data = []

    #fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    #the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)




#get first all usernames and passwords
@bookreaders.route('/accounts')
def get_accounts():
    cursor = db.get_db().cursor()
    query = = '''
        SELECT username, password
        FROM BookReader
    '''
    cursor.execute(query)
   