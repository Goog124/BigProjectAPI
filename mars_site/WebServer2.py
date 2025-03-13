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
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    education = StringField('Образование', validators=[DataRequired()])
    profession = StringField('Профессия', validators=[DataRequired()])
    sex = StringField('Пол', validators=[DataRequired()])
    motivation = StringField("Мотивация", validators=[DataRequired()])
    ready = BooleanField('Готовы остаться на марсе?')
    submit = SubmitField('Записаться')


@app.route('/answer', methods=['GET', 'POST'])
@app.route('/auto_answer', methods=['GET', 'POST'])
def answer():
    form = LoginForm()
    if form.validate_on_submit():
        res = {
            "Фамилия": form.data["surname"],
            "Имя": form.data["name"],
            "Образование": form.data["education"],
            "Профессия": form.data["profession"],
            "Пол": form.data["sex"],
            "Мотивация": form.data["motivation"],
            "Готовы остаться на марсе?": form.data["ready"],
        }
        # return "<br>".join([f"{i} : {j}" for i, j in res.items()])
        return render_template('otvet.html', data=res)
    return render_template('auto_answer.html', title='Авторизация', form=form)


@app.route('/success/<data>')
def otvet(data):
    return ""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')