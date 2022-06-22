from flask import Blueprint, render_template

contactus = Blueprint(
    'contactus',
    __name__,
    static_folder="static",
    static_url_path="/contactus",
    template_folder="templates"
)


@contactus.route('/contact')
def get_contact_page():
    return render_template('contactUs.html')
