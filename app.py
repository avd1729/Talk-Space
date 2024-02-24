from flask import Flask, render_template, request, redirect, session, url_for, jsonify
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
    posts = db.relationship('Post', backref='user', lazy=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

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

# Route for searching users


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query']
        users = User.query.filter(
            User.username.ilike(f'%{search_query}%')).all()
        return render_template('search_results.html', users=users, search_query=search_query)
    return redirect(url_for('index'))

# Modified index route to fetch posts from all users


@app.route('/')
def index():
    username = session.get('username')
    posts = Post.query.all()  # Fetch posts from all users
    return render_template('index.html', username=username, posts=posts)

# Route to view posts of a specific user


@app.route('/user/<int:user_id>')
def user_posts(user_id):
    user = User.query.get_or_404(user_id)
    posts = user.posts
    return render_template('user_posts.html', user=user, posts=posts)

# Route to add a new post


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = User.query.filter_by(username=session['username']).first()

        new_post = Post(title=title, content=content, user_id=author.id)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_post.html')

# Route to view and update user profile


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    username = session.get('username')
    user = User.query.filter_by(username=username).first()

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']

        db.session.commit()
        return redirect(url_for('profile'))

    return render_template('profile.html', user=user)

# Route for updating user profile


@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    username = session.get('username')
    user = User.query.filter_by(username=username).first()

    if request.method == 'POST':
        new_username = request.form['username']
        user.email = request.form['email']

        old_username = user.username
        user.username = new_username
        for post in user.posts:
            post.author = new_username

        db.session.commit()

        session['username'] = new_username

        return redirect(url_for('profile'))

    return render_template('update_profile.html', user=user)

# Route for deleting a post


@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

# Route to list all users


@app.route('/users')
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username,
                  'email': user.email} for user in users]
    return jsonify({'users': user_list})

# Route to search for a user by username


@app.route('/users/<string:username>')
def search_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        user_info = {'id': user.id,
                     'username': user.username, 'email': user.email}
        return jsonify({'user': user_info})
    else:
        return jsonify({'message': 'User not found'}), 404

# Route to list all posts


@app.route('/posts')
def get_posts():
    posts = Post.query.all()
    post_list = [{'id': post.id, 'title': post.title, 'content': post.content,
                  'author': post.user.username} for post in posts]
    return jsonify({'posts': post_list})

# Route to list all posts by a particular user


@app.route('/users/<string:username>/posts')
def get_user_posts(username):
    user = User.query.filter_by(username=username).first()
    if user:
        posts = user.posts
        post_list = [{'id': post.id, 'title': post.title,
                      'content': post.content} for post in posts]
        return jsonify({'posts': post_list})
    else:
        return jsonify({'message': 'User not found'}), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
