from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    params = {}
    params["title"] = title
    return render_template('base.html', **params)

@app.route('/training/<prof>')
def plan(prof):
    params = {}
    if "строитель" in prof.lower() or "инженер" in prof.lower():
        prof = "инженер"
    else:
        prof = "научный"
    params["prof"] = prof
    return render_template('content.html', **params)

@app.route('/list_prof/<type_list>')
def get_prof_list(type_list):
    prof_list = [1, 2, 3, 4, 5]
    return render_template("list.html", type_list=type_list, list=prof_list)


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/answer', methods=['GET', 'POST'])
@app.route('/auto_answer', methods=['GET', 'POST'])
def answer():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('auto_answer.html', title='Авторизация', form=form)


@app.route('/success')
def otvet():
    return "Ура"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')