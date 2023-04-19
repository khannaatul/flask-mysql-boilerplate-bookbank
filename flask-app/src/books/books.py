from flask import Blueprint, request, jsonify, make_response, current_app
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

    bookid = the_data['books_id']
    first = the_data['books_first']
    last = the_data['books_last']
    pageCount = the_data['books_pageCount']
    genre = the_data['books_genre']
    title = the_data['books_title']
    condition = the_data['books_conditionOfBook']
    inBank = the_data['books_inBank']
    isPhysical = the_data['books_isPhysical']
    numCopies = the_data['books_numCopies']
    synopsis = the_data['books_synopsis']


    query = 'Insert into Books (bookID, first, last, pageCount, genre, title, conditionOfBook,inBank, isPhysical, numCopies, synopsis) values(" '
    query += str(bookid)  + ' " , " '
    query += first  + ' " , " ' 
    query += last + ' " , " ' 
    query += str(pageCount) + ' " , " '
    query += genre + ' " , " ' 
    query += title + ' " , " '
    query += condition + ' " , " '
    query += str(inBank)  + ' " , " '
    query += str(isPhysical) + ' " , " '
    query += str(numCopies) + ' " , " '
    query += synopsis +  ' ")'

    current_app.logger.info(query)


    # executing and commitimg the insert statement
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(query)

    #send commit command to database
    db.get_db().commit()

    return 'Success'


@books.route("/bookdelete/<bookid>", methods=["DELETE"])
def book_delete(bookID):
    book = Books.query.get(bookID)
    db.session.delete(book)
    db.session.commit()
    return "Book was successfully deleted"