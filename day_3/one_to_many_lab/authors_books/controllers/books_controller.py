from flask import Blueprint, render_template, request, redirect
from repositories import book_repository, author_repository
from models.book import Book

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route("/books")
def books():
    all_books = book_repository.select_all()

    return render_template("books/index.html", books=all_books)

@book_blueprint.route('/books/<book_id>', methods=['POST'])
def delete_book(book_id):
    book_repository.delete(book_id)
    return redirect ('/books')

@book_blueprint.route('/new')
def new_book():
    return render_template('books/new.html')

@book_blueprint.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    year = request.form['year']
    author_id = request.form['author_id']
    
    author = author_repository.select(author_id)
    book = Book(title, year, author)
    book_repository.save(book)
    return redirect('/books')