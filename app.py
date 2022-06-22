from datetime import timedelta
from flask import Flask
from pages.contactus.contactus import contactus
from pages.home.home import home
from pages.assignment3_1.assignment3_1 import assignment3_1
from pages.assignment3_2.assignment3_2 import assignment3_2
from components.navbar.navbar import navbar
from pages.assignment_4.assignment_4 import assignment_4
app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(contactus)
app.register_blueprint(assignment3_1)
app.register_blueprint(assignment3_2)
app.register_blueprint(assignment_4)
app.register_blueprint(navbar)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


if __name__ == '__main__':
    app.run(debug=True)
