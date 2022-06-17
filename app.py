from datetime import timedelta
import mysql.connector

from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

@app.route('/home')
def get_home_page():
    return render_template('HomePage.html')

@app.route('/')
def redirect_home_page():
    return redirect(url_for('get_home_page'))


@app.route('/food')
def redirect_food_page():
    return redirect("/hobbies")


@app.route('/contact')
def get_contact_page():
    return render_template('contactUs.html')


@app.route('/assignment3_1')
def get_hobbies_page():
    name = "dOrIN"
    food_kinds = ['chocolate', 'banana', 'cake', 'cookies']
    hobbies = ['drawing', 'reading', 'baking', 'swimming']
    #hobbies = []
    return render_template('‘assignment3_1’.html',
                           user_name=name,
                           hobbies=hobbies,
                           favorite_food=food_kinds)


@app.route('/assignment3_2', methods=['GET', 'POST'])
def get_assignment3_2_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        session['name'] = name
    else:
        if 'name' in request.args:
            name = request.args['name']
            if name == '':
                return render_template('‘assignment3_2’.html',
                                       users=users.values())
            founded_user = None
            for user in users.values():
                if user['name'] == name:
                    founded_user = user
                    break
            if founded_user:
                return render_template('‘assignment3_2’.html',
                                       name=founded_user['name'],
                                       email=founded_user['email'],
                                       gender=founded_user['gender'])
            else:
                return render_template('‘assignment3_2’.html', message='User not found.')

    return render_template('‘assignment3_2’.html')


users = {"user1": {"name": "Dorin Ghasri", "email": "Do@gmail.com", "gender": "female"},
         "user2": {"name": "Keren Schmal", "email": "KK@gmail.com", "gender": "female"},
         "user3": {"name": "Nadav Chapnick", "email": "Nadav@gmail.com", "gender": "male"},
         "user4": {"name": "Reut Chitrit", "email": "Reutika@gmail.com", "gender": "female"},
         "user5": {"name": "Liel Partush", "email": "liell@gmail.com", "gender": "female"}}

@app.route('/log_out')
def logout():
    session['name'] = False
    session.clear()
    return redirect(url_for('get_assignment3_2_page'))




if __name__ == '__main__':
    app.run(debug=True)
