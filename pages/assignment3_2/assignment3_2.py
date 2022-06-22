from flask import Blueprint, render_template, redirect, url_for, request, session

assignment3_2 = Blueprint(
    'assignment3_2',
    __name__,
    static_folder="static",
    static_url_path="/assignment3_2",
    template_folder="templates"
)


@assignment3_2.route('/assignment3_2', methods=['GET', 'POST'])
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
                return render_template('assignment3_2.html',
                                       users=users.values())
            founded_user = None
            for user in users.values():
                if user['name'] == name:
                    founded_user = user
                    break
            if founded_user:
                return render_template('assignment3_2.html',
                                       name=founded_user['name'],
                                       email=founded_user['email'],
                                       gender=founded_user['gender'])
            else:
                return render_template('assignment3_2.html', message='User not found.')

    return render_template('assignment3_2.html')


users = {"user1": {"name": "Dorin Ghasri", "email": "Do@gmail.com", "gender": "female"},
         "user2": {"name": "Keren Schmal", "email": "KK@gmail.com", "gender": "female"},
         "user3": {"name": "Nadav Chapnick", "email": "Nadav@gmail.com", "gender": "male"},
         "user4": {"name": "Reut Chitrit", "email": "Reutika@gmail.com", "gender": "female"},
         "user5": {"name": "Liel Partush", "email": "liell@gmail.com", "gender": "female"}}


@assignment3_2.route('/log_out')
def logout():
    session['name'] = False
    session.clear()
    return redirect(url_for('assignment3_2.get_assignment3_2_page'))


