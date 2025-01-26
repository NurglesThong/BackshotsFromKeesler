from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base

# Initialize Flask app
app = Flask(__name__)

# Set up the database connection
engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Route to display all users
@app.route('/')
def index():
    users = session.query(User).all()
    return render_template('index.html', users=users)

# Route to add a new user
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)