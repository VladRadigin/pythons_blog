from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Text, DateTime
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' # <- указываем с какой базой работаем
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    # Создаем поля в базе данных
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    intro = Column(String(300), nullable=False)
    content = Column(Text, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

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

@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        _title = request.form['title']
        _intro = request.form['intro']
        _text = request.form['text']

        article = Article(title=_title, intro=_intro, content=_text)
    
        db.session.add(article)
        db.session.commit()
        return redirect('/')
    
    else: return render_template('create-article.html')

# Динамический путь
# Динамическим путь становится когда в него включаются переменные.
# @app.route('/user/<string:name>/<int:id>')
# def show_post(name, id):
#     return f"Username: {name}\nID: {str(id)}"


if __name__ == '__main__':
    app.run(debug=True)