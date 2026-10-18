import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'local-dev-secret-change-before-hosting')
# Local default matches the password you previously chose. Change it before publishing online.
PASSWORD = os.environ.get('BIRTHDAY_PASSWORD', 'rini1917')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('password', '') == PASSWORD:
            session['unlocked'] = True
            return redirect(url_for('home'))
        flash('Hmm… my heart is waiting for the right password. 💌')
    return render_template('login.html')

@app.route('/home')
def home():
    if not session.get('unlocked'):
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT', 5000)), debug=False)
