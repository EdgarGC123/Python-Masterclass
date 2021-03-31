from flask import Flask, redirect, url_for, request, render_template

from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir,"mydabase.db"))


app = Flask(__name__)#name determines the name of the application, this is the main file of the application.

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class Book(db.Model):
    name = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    author = db.Column(db.String(100), nullable=False)


#PART ONE
# @app.route('/')
# def home():
#     return 'Hello World'

# @app.route('/profile/<int:id>')
# def profile(id):
#     return '<h1>This is a profile page for %d </h1>' % id


#PART TWO
# @app.route('/admin')
# def welcome_admin():
#     return 'Welcome Admin'

# @app.route('/guest/<guest>')
# def welcome_guest(guest):
#     return 'Welcome Guest %s' % guest

# @app.route('/user/<user>')
# def welcome_user(user):
#     if user == 'admin':
#         return redirect(url_for('welcome_admin'))
#     else:
#         return redirect(url_for('welcome_guest', guest=user))



#PART THREE
# @app.route('/')
# def index():
#     # return render_template('index.html')
#     return 'This is the request made by the client %s' % request.headers

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username, isActive=True)


# @app.route('/books')
# def books():
#     books = [{'name':'Book1', 'author':'Author1'}, {'name':'Book2', 'author':'Author2'}, {'name':'Book3', 'author':'Author3'}]
#     return render_template('books.html', books = books)



@app.route('/books')
def books():
    books = ['Book1', 'Book2', 'Book3']
    books2 = [
        {'name': 'Book1', 'author': 'Author1', 'img': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fopenclipart.org%2Fimage%2F2400px%2Fsvg_to_png%2F211628%2FBook_thick_generic.png&f=1&nofb=1' }, 

        {'name': 'Book2', 'author': 'Author2', 'img': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fopenclipart.org%2Fimage%2F2400px%2Fsvg_to_png%2F211628%2FBook_thick_generic.png&f=1&nofb=1'}, 
        
        {'name': 'Book3', 'author': 'Author3', 'img': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fopenclipart.org%2Fimage%2F2400px%2Fsvg_to_png%2F211628%2FBook_thick_generic.png&f=1&nofb=1'},

        {'name': 'Book3', 'author': 'Author3', 'img': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fopenclipart.org%2Fimage%2F2400px%2Fsvg_to_png%2F211628%2FBook_thick_generic.png&f=1&nofb=1'},

        {'name': 'Book3', 'author': 'Author3', 'img': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fopenclipart.org%2Fimage%2F2400px%2Fsvg_to_png%2F211628%2FBook_thick_generic.png&f=1&nofb=1'},
    
    ]
    books3 = Book.query.all()
    return render_template('books.html', books=books3)

@app.route('/addbook', methods=['POST', 'GET'])
def addbook():
    if request.method == 'POST':
        print('WE IN IT BOISS')
        name = request.form['name']
        author = request.form['author']
        book = Book(name=name, author=author)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('addbook.html')

@app.route('/submitbook', methods=['POST'])
def submitbook():
    name = request.form['name']
    author = request.form['author']
    book = Book(name=name, author=author)
    db.session.add(book)
    db.session.commit()
    return 'Book name is %s and author is %s' % (name, author)

@app.route('/updatebooks')
def updatebooks():
    books = Book.query.all()
    return render_template('updatebooks.html', books=books)

@app.route('/update', methods=['POST'])
def update():
    newname = request.form['newname']
    oldname = request.form['oldname']
    newauthor = request.form['newauthor']
    # oldauthor = request.form['oldauthor']

    book = Book.query.filter_by(name=oldname).first()
    book.name = newname
    book.author = newauthor
    db.session.commit()
    return redirect('/books')

@app.route('/delete', methods=['POST'])
def delete():
    name = request.form['name']
    book = Book.query.filter_by(name=name).first()
    db.session.delete(book)
    db.session.commit()
    return redirect('/books')

if __name__ == "__main__":

    app.run(debug=True)#Flask dev server has a reloader and debugger. when debug is set to true, both reloader and debugger is set to true
