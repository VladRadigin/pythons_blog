from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' # <- указываем с какой базой работаем
db = SQLAlchemy(app)


class Article(db.Model):
    # Создаем поля в базе данных
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' %self.id

@app.route('/')
@app.route('/home')
@app.route('/index.html')
def welcome_page():
    return render_template('index.html') # <- Указываем какой файл хотим отобразить


# Статический путь
@app.route('/blog')
def users():
    return render_template('blog.html')


# Динамический путь
# Динамическим путь становится когда в него включаются переменные.
@app.route('/user/<string:name>/<int:id>')
def show_post(name, id):
    return f"Username: {name}\nID: {str(id)}"


if __name__ == '__main__':
    app.run(debug=True)