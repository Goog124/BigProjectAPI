from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run(port=8080, host='127.0.0.1')

    user = User()
    user.surname = "Konstantin"
    user.name = "Zverev"
    user.age = 28
    user.position = "zam_capitan"
    user.speciality = "pedagog"
    user.address = "module_2"
    user.email = "kza4@kvantroium.ru"
    user.hashed_password = "yaliceum"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()