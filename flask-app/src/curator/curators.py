from flask import Blueprint, request, jsonify, make_response,  current_app
import json
from src import db


curators = Blueprint('curators', __name__)

# Get all curators from the BookBank
@curators.route('/curators', methods=['GET'])
def get_Curators():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT CuratorID,\
       first, last, email, username, password FROM Curator')
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
    the_data = request.json
    newpassword = the_data['password']
    curatorID = the_data['curatorID']
    cursor = db.get_db().cursor()

    query = "UPDATE Curator SET password = '%s' WHERE CuratorID = '%s'"%(newpassword,curatorID)

    cursor.execute(query)
    #send commit command to database
    db.get_db().commit()
    return "Curator password was successfully updated"


#get first 5 curators
@curators.route('/first5')
def get_first_curators():
    cursor = db.get_db().cursor()
    query = '''
        SELECT first, last, username, email
        FROM Curator
        ORDER BY CuratorID 
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

