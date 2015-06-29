from datetime import datetime
import os

from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask.ext.stormpath import (
    StormpathError,
    StormpathManager,
    User,
    login_required,
    login_user,
    logout_user,
    user,
)


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'zi-t\xaa\xc7\xf0.\xdb\xc3\xed\xc0}$\xbaL\xa1\xa6\xb1\xd5'
app.config['STORMPATH_API_KEY_FILE'] = 'apiKey.properties'
app.config['STORMPATH_APPLICATION'] = 'flaskr'

stormpath_manager = StormpathManager(app)

@app.route('/')
def show_posts():
    posts = []
    for account in stormpath_manager.application.accounts:
        if account.custom_data.get('posts'):
            posts.extend(account.custom_data['posts'])

    posts = sorted(posts, key=lambda k: k['date'], reverse=True)
    return render_template('show_posts.html', posts=posts)

@app.route('/add', methods=['POST'])
@login_required
def add_post():
    if not user.custom_data.get('posts'):
        user.custom_data['posts'] = []

    user.custom_data['posts'].append({
        'date': datetime.utcnow().isoformat(),
        'title': request.form['title'],
        'text': request.form['text'],
    })
    user.save()

    flash('New post successfully added.')
    return redirect(url_for('show_posts'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        try:
            _user = User.from_login(
                request.form['email'],
                request.form['password'],
            )
            login_user(_user, remember=True)
            flash('You were logged in.')

            return redirect(url_for('show_posts'))
        except StormpathError, err:
            error = err.message

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    logout_user()
    flash('You were logged out.')

    return redirect(url_for('show_posts'))

# When developing locally, this will use port 5000, 
# in production Heroku will set the PORT environment variable.
    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)