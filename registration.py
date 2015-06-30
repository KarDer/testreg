from flask import request, g
import pickle

class Users(object):

    def get_on_filter(self, filter = None, value = None):
        """
        Depending on the filter, the return value
        :return: [{'username': u'name', 'phone': 380669994411, 'email': u'mail@mail.com'}]
        """
        if filter and value:
            cur = g.db.execute('select username, email, phone, date_added, more from user where '+filter+' = ? order by id desc', [value])
            entries = [dict(username=row[0], email=row[1], phone=row[2], date_added=row[3], more=pickle.loads(row[4])) for row in cur.fetchall()]
            return entries
        return ''

    def get_all_users(self):
        """
        All registred users
        :return: [{'username': u'name', 'phone': 380669994411, 'email': u'mail@mail.com'}]
        """
        cur = g.db.execute('select username, email, phone, date_added from user order by id desc')
        entries = [dict(username=row[0], email=row[1], phone=row[2], date_added=row[3]) for row in cur.fetchall()]
        return entries

    def add_user(self, metod = 'form', more = ''):
        """
        Adds a new user in DB
        :return: If all is well - True
        """
        if metod == 'form':
            g.db.execute('insert into user (username, email, pass, phone, more) values (?, ?, ?, ?, ?)',
                 [request.form['username'], request.form['email'], request.form['pass'], request.form['phone'], more])
        elif metod == 'get':
            g.db.execute('insert into user (username, email, pass, phone, more) values (?, ?, ?, ?, ?)',
                 [request.args['username'], request.args['email'], request.args['pass'], request.args['phone'], more])
        g.db.commit()
        return True

    def login(self):
        """
        Validates the correct login and password
        :return: returns user
        """
        cur = g.db.execute('select username, email, phone from user where username = ? and pass = ?',
                           [request.form['username'], request.form['pass']])
        entries = [dict(username=row[0], email=row[1], phone=row[2]) for row in cur.fetchall()]
        return entries

    def verification_email(self, email=None):
        """
        Checking the existence of email
        :param email:
        :return: if empty - True, if not empty - False
        """
        if email:
            cur = g.db.execute('select email from user where email = ?', [email])
            if not cur.fetchall():
                return True
        return False