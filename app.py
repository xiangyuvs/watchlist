from flask import Flask, url_for
from flask import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)


@app.route('/test')
def test_url_for():
    # ?????????????????????? URL??
    print(url_for('hello'))  # ???/
    # ??????????????? URL ??? URL ?
    print(url_for('user_page', name='greyli'))  # ???/user/greyli
    print(url_for('user_page', name='peter'))  # ???/user/peter
    print(url_for('test_url_for'))  # ???/test
    # ???????????????????????????????? URL ???
    print(url_for('test_url_for', num=2))  # ???/test?num=2
    return 'Test page'
