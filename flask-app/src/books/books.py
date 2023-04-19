from flask import Blueprint, request, jsonify, make_response
import json
from src import db


books = Blueprint('books', __name__)

# Get all the books from the BookBank
@books.route('/books', methods=['GET'])
def get_books():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of books
    cursor.execute('SELECT first,last, pagecount coverimage,\
        genre, title, link, conditionofbook, inbank, isphysical,\
        numcopies, synopsis, isautographed, bookid, userid, curatorid,\
        authorid FROM Books')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# # get the top 5 books from the database
# @books.route('/mostExpensive')
# def get_most_pop_books():
#     cursor = db.get_db().cursor()
#     query = '''
#         SELECT product_code, product_name, list_price, reorder_level
#         FROM books
#         ORDER BY list_price DESC
#         LIMIT 5
#     '''
#     cursor.execute(query)
#        # grab the column headers from the returned data
#     column_headers = [x[0] for x in cursor.description]

#     # create an empty dictionary object to use in 
#     # putting column headers together with data
#     json_data = []

#     # fetch all the data from the cursor
#     theData = cursor.fetchall()

#     # for each of the rows, zip the data elements together with
#     # the column headers. 
#     for row in theData:
#         json_data.append(dict(zip(column_headers, row)))

#     return jsonify(json_data)


@books.route('/newbook', methods = ['POST'])
def add_book():

    the_data = request.json
    current_app.logger.info(the_data)

    first = the_data['book_first']
    last = the_data['book_last']
    pageCount = the_data['book_pageCount']
    genre = the_data['book_genre']
    title = the_data['book_title']
    condition = the_data['book_conditionOfBook']
    inBank = the_data['book_inBank']
    isPhysical = the_data['book_Physical']
    numCopies = the_data['book_numCopies']
    synopsis = the_data['book_synopsis']
    isAutographed = the_data['book_isAutographed']


    query = 'Insert into books (first, last, pageCount, genre, title, conditionOfBook,inBank, isPhysical, numCopies, synopsis, isAutographed ) values(" '
    query += first  + ' " , " ' 
    query += last + ' " , ' 
    query += str(pageCount) + ' " , '
    query += genre + ' " , ' 
    query += title + ' " , '
    query += condition + ' " , '
    query += inBank + ' " , '
    query += isPhysical + ' " , '
    query += str(numCopies) + ' " , '
    query += synopsis + ' " , '
    query += isAutographed + ')'

    current_app.logger.info(query)


    # executing and commitimg the insert statement
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(query)

    #send commit command to database
    db.get_db().commit()

    return 'Success'


@app.route("/book/<bookid>", methods=["DELETE"])
def book_delete(bookid):
    book = Books.query.get(bookid)
    db.session.delete(book)
    db.session.commit()
    return "Book was successfully deleted"