from flask import Blueprint, render_template, redirect, url_for

assignment3_1 = Blueprint(
    'assignment3_1',
    __name__,
    static_folder="static",
    static_url_path="/assignment3_1",
    template_folder="templates"
)


@assignment3_1.route('/assignment3_1')
def get_hobbies_page():
    name = "dOrIN"
    food_kinds = ['chocolate', 'banana', 'cake', 'cookies']
    hobbies = ['drawing', 'reading', 'baking', 'swimming']
    return render_template('assignment3_1.html',
                           user_name=name,
                           hobbies=hobbies,
                           favorite_food=food_kinds)


@assignment3_1.route('/food')
def redirect_food_page():
    return redirect(url_for("assignment3_1.get_hobbies_page"))
