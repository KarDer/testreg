from __future__ import with_statement
from contextlib import closing

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     render_template, flash, jsonify

app = Flask(__name__)
app.config.from_object('config')

from registration import Users

@app.route('/rpc_verification_email', methods=['GET', 'POST'])
def rpc_verification_email():
    """
    Checks the existence of the entered email
    :return: OK or ERROR
    """
    user = Users()
    if request.method == 'POST':
        if not user.verification_email(request.form['email']):
            return jsonify({"result": "ERROR"})

    return jsonify({"result": "OK"})

@app.route('/api_filter', methods=['GET'])
def api_filter():
    """
    It accepts any key - values and searches the them
    /api_filter?email=my@mail.ua
    or
    /api_filter?username=myname
    :return: dict in json
    """
    user = Users()

    if request.args.keys():
        # If you entered more than one, then take the first
        filter = request.args.keys()[0]
        value = request.args[filter]
        result = user.get_on_filter(filter, value)

        if result:
            return jsonify({i: value for i, value in enumerate(result)})
        else:
            return jsonify({"result": "Empty"})

    return jsonify({"result": "ERROR"})

@app.route('/api_registration', methods=['GET'])
def api_registration():
    """
    Upon receipt of the data creates a user
    /api_registration?username=mynameIS&email=my@mail.ua&pass=0000&phone=380665551122
    :return: OK or ERROR
    """
    user = Users()
    if not user.verification_email(email = request.args.get("email")):
        return jsonify({"result": "ERROR"})
    if request.args.get("username") and request.args.get("email") and \
            request.args.get("pass")and request.args.get("phone"):
        login_user = user.add_user(metod='get')

        if login_user:
            return jsonify({"result": "OK"})

    return jsonify({"result": "ERROR"})

@app.route('/')
def show_entries():
    """
    It displays a list of users
    :return:
    """
    user = Users()
    entries = user.get_all_users()
    return render_template('show_entries.html', entries=entries)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    user Login
    :return:
    """
    error = None
    if request.method == 'POST':
        user = Users()
        login_user = user.login()

        if login_user:
            session['logged_in'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('show_entries'))
        else:
            error = 'The data is not correct, or that user does not exist'

    return render_template('login.html', error=error)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    """
    Registration via the website
    :return:
    """
    error = None
    if request.method == 'POST':
        if not request.form['username'] or not request.form['email'] \
                or not request.form['pass'] or not request.form['phone']:
            error = 'Not all fields are completed'
        else:
            user = Users()
            user.add_user()

            session['logged_in'] = request.form['username']
            flash('you have registered and are logged in as %s' % request.form['username'])
            return redirect(url_for('show_entries'))

    return render_template('registration.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))



# ************ DB connect ************ #
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()
# ************ end ************ #

if __name__ == '__main__':
    app.run()