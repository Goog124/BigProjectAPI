from datetime import datetime, timedelta
from flask import *
from pyexpat.errors import messages

from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user
from data.users import User
from data.jobs import Jobs
from data.login import LoginForm
from data.job_form_model import JobForm
from data.resister_form import RegisterForm
import werkzeug.security

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    db_sess.commit()
    return render_template('all_jobs.html', jobs=jobs)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        db_sess = db_session.create_session()
        user.surname = form.surname.data
        user.name = form.surname.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.email = form.email.data
        user.set_password(form.password.data)
        db_sess.add(user)
        try:
            db_sess.commit()
        except Exception as e:
            return render_template('register_user.html',
                                          title='Регистрация',
                                          form=form,
                                          message="Уже есть")
        return redirect("/login")
    return render_template('register_user.html', title='Регистрация', form=form)

@app.route('/work', methods=['GET', 'POST'])
def work():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.team_leader = form.team_leader.data
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.work_done.data
        job.start_date = datetime.now()
        job.end_date = datetime.now() + timedelta(days=3)
        db_sess.add(job)
        db_sess.commit()
        return redirect("/")
    return render_template('add_work.html', title='Работа', form=form)

def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()