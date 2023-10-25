from flask import Flask, render_template, redirect, request, url_for
from flask import session

import json

app = Flask(__name__, template_folder='templates/main')
app.secret_key = 'pLeAsE sEt tHe sEcREt kEy yOUr wIsH'

# Fake user data
users = {
    'john': {
        'username': 'john',
        'password': 'password123',
        'email': 'johndoe@me.com',
        'is_admin': False
    },
    'jane': {
        'username': 'jane',
        'password': 'password456',
        'email': 'janedoe@me.com',
        'is_admin': False
    },
    'admin': {
        'username': 'admin',
        'password': 'password',
        'email': 'admin@me.com',
        'is_admin': True
    }
}


@app.route('/')
def root():
    return render_template('home.html', title='Natrec - AI Web Application')


@app.route('/home')
def home():
    return render_template('home.html', title='Natrec - AI Web Application')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')


@app.route('/features')
def features():
    return render_template('features.html', title='Features we offer')


@app.route('/about')
def about():
    return render_template('about.html', title='About Us')


@app.route('/price')
def price():
    return render_template('price.html', title='Prices to our servces')


@app.route('/privacy')
def privacy_policy():
    return render_template('privacy.html', title='Privacy Policy')


@app.route('/terms')
def terms():
    return render_template('terms.html', title='Terms & Conditions')


@app.route('/login')
def login():
    return render_template('login.html', title='Login to Natrec')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/signup')
def signup():
    return render_template('signup.html', title='Signup to Natrec')


@app.route('/dashboard')
def dashboard():
    username = session.get('username')  # Access the username from the session
    if username in users:
        return render_template('dashboard.html', title='Dashboard', user=users[username])
    return redirect(url_for('login'))


@app.route('/auth/login', methods=['POST'])
def login_auth():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember_me = True if request.form.get('rememberMe') else False
        if username in users and users[username]['password'] == password:
            # User is authenticated, set the username in the session
            # Session is used to store data across requests(secure and encrypted)
            session['username'] = username
            session.permanent = remember_me
            # Perform necessary actions, such as redirecting to the dashboard
            return redirect(url_for('dashboard'))
        else:
            # Invalid credentials, show error message
            error_message = 'Invalid username or password'
            return render_template('login.html', error_message=error_message)
    return redirect(url_for('login'))


@app.route('/auth/signup', methods=['GET', 'POST'])
def signup_auth():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if username already exists
        if username in users:
            error_message = 'Username already exists'
            return render_template('signup.html', error_message=error_message, title="Signup to Natrec")

        # Store user information in the users dictionary
        users[username] = {'username': username,
                           'email': email, 'password': password, 'is_admin': False}

        # Redirect to the login page or any other desired page
        return redirect(url_for('login'))

    return render_template('signup.html',title="Signup to Natrec")


@app.route('/admin')
def admin():
    username = session.get('username')
    if username in users and users[username]['is_admin']:
        return render_template('admin.html', title='Admin Page', users=users)
    error_message = "Please login with administrator account(access denied)"
    return render_template('login.html', error_message=error_message)


@app.route('/blog')
def blog():
    return render_template('blog/blog.html', title="Blog")


# Custom error handler for 404 Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    # Return the error page and its status code
    response = app.response_class(
        # Create a response based on the not found template
        response=render_template('not_found.html', title='Page Not Found(404)', status=404),
        status=404,
        mimetype='text/html'
    )
    return response 


@app.route('/blog/<page>')
def access_log(page):
    return render_template(f'blog/{page}.html', title=page)


@app.route('/tutorials')
def tutorials():
    return render_template(f'tutorials/tutorials.html', title="Tutorials")


@app.route('/started')
def get_started():
    return render_template(f'tutorials/get_started.html', title="Get Started")



@app.route('/user/remove', methods=['POST'])
def remove_user():
    if "username" in request.json:
        username = request.json['username']
        # remove user from users dictionary(if its not current user)
        if session.get('username') != username  and username in users:
            del users[username]
        else:
            return json.dumps({'success': False})
    return json.dumps({'sucess': True})

if __name__ == '__main__':
    app.run(debug=True)
