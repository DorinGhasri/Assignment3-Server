from flask import Blueprint, render_template, redirect, url_for

home = Blueprint(
    'home',
    __name__,
    static_folder="static",
    static_url_path="/home",
    template_folder="templates"
)


@home.route('/home')
def get_home_page():
    return render_template('HomePage.html')


@home.route('/')
def redirect_home_page():
    return redirect(url_for('home.get_home_page'))
