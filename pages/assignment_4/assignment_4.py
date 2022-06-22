import random

from flask import Blueprint, render_template, redirect, url_for, request, jsonify, session
import mysql.connector
import requests

assignment_4 = Blueprint(
    'assignment_4',
    __name__,
    static_folder="static",
    static_url_path="/assignment_4",
    template_folder="templates"
)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment_4.route('/assignment_4')
def get_assignment_4():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', users=users_list, message=request.args.get('message'))


@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    print(f'{name} {email} {gender}')
    query = "INSERT INTO users(name, email, gender) VALUES ('%s', '%s', '%s')" % (name, email, gender)
    interact_db(query=query, query_type='commit')
    return redirect(url_for('assignment_4.get_assignment_4', message=f"{name} inserted successfully"))


@assignment_4.route('/delete_user', methods=['POST'])
def delete_user():
    user_name = request.form['user_name']
    query = "DELETE FROM users WHERE name='%s';" % user_name
    # print(query)
    interact_db(query, query_type='commit')
    return redirect(url_for('assignment_4.get_assignment_4', message=f"{user_name} deleted successfully"))


@assignment_4.route('/update_user', methods=['POST'])
def update_user():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    query = "UPDATE users " \
            "Set email='%s', gender='%s'" \
            "WHERE name='%s';" % (email, gender, name)
    interact_db(query, query_type='commit')
    return redirect(url_for('assignment_4.get_assignment_4', message=f"{name} update successfully"))


@assignment_4.route('/users', methods=['GET'])
def get_users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return jsonify(users_list)


# Form2
@assignment_4.route('/outer_source', methods=['GET'])
def get_outer_source():
    user_id = request.args['user_id']
    response = requests.get(url=f"https://reqres.in/api/users/{user_id}")
    user = response.json()
    session['user'] = user.get('data')
    return render_template('assignment_4.html')


def if_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


@assignment_4.route('/assignment4/restapi_users', defaults={'USER_ID': 1}, methods=['GET'])
@assignment_4.route('/assignment4/restapi_users/<USER_ID>', methods=['GET'])
def get_restapi_users(USER_ID):
    if if_integer(USER_ID):
        response = requests.get(url=f"https://reqres.in/api/users/{USER_ID}")
        if response.status_code is 200:
            users = response.json()
            return users.get('data')
        else:
            message = "Error: User doesn't exist"
            return jsonify(message)
    else:
        message = "Error: please insert integer"
        return jsonify(message)

