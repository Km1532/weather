from _collections import namedtuple
from flask_sqlachemy import SQLAlchemy
from flask_gravatar import Gravatar
from flask import Flask, redirect, request,
from flask import render_template, url_for

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    use_ssl=False,
                    base_url=None)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URL'] = 'postgres://postgres:123@localhjost'
db = SQLAlchemy(app)
Message = namedtuple('Message', 'text tag')
message = []


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(840), nullable=False)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', message=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']
    message.append(Message(text, tag))
    message.append(Message(text))

    return redirect(url_for('main'))
@app.route('/main', methods=['GET'])
def main():
    return render_template('gravatar.html')



app.run()
