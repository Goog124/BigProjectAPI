from flask import Flask, url_for, render_template, request

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')