from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootpass@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'uihfdher387294730'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Route for user registration


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')

        new_user = User(username=username, email=email,
                        password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        session['username'] = username

        return redirect(url_for('index'))

    return render_template('register.html')

# Route for user login


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['username'] = username
            return redirect(url_for('index'))

    return render_template('login.html')

# Route for logging out


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# Route for index page


@app.route('/')
def index():
    username = session.get('username')
    return render_template('index.html', username=username)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
