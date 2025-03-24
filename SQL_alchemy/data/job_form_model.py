from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField, StringField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired

class JobForm(FlaskForm):
    job = StringField('Работа', validators=[DataRequired()])
    team_leader = IntegerField('id начальника', validators=[DataRequired()])
    work_size = IntegerField('Время выполнения', validators=[DataRequired()])
    collaborators = StringField('id рабочих', validators=[DataRequired()])
    work_done = BooleanField('Работа выполнена?')
    submit = SubmitField('Добавить работу')



