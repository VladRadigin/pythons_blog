from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/home')
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