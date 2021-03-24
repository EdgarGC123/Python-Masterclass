from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)#name determines the name of the application, this is the main file of the application.

#PART ONE
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
#     if user == 'Admin':
#         return redirect(url_for('welcome_admin'))
#     else:
#         return redirect(url_for('welcome_guest', guest=user))



#PART THREE
@app.route('/')
def index():
    return render_template('index.html')
    # return 'This is the request made by the client %s' % request.headers

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username, isActive=False)

@app.route('/books')
def books():
    books = ['Book1', 'Book2', 'Book3']
    books2 = [{'name': 'Book1', 'author': 'Author1', 'img': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fopenclipart.org%2Fimage%2F2400px%2Fsvg_to_png%2F211628%2FBook_thick_generic.png&f=1&nofb=1' }, {'name': 'Book2', 'author': 'Author2', 'img': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fopenclipart.org%2Fimage%2F2400px%2Fsvg_to_png%2F211628%2FBook_thick_generic.png&f=1&nofb=1'}, {'name': 'Book3', 'author': 'Author3', 'img': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fopenclipart.org%2Fimage%2F2400px%2Fsvg_to_png%2F211628%2FBook_thick_generic.png&f=1&nofb=1'}]
    return render_template('books.html', books=books2)

app.run(debug=True)#Flask dev server has a reloader and debugger. when debug is set to true, both reloader and debugger is set to true