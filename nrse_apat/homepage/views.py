from flask import render_template, Blueprint
from flask_security import login_required

homepage_blueprint = Blueprint('homepage_blueprint', __name__)

@homepage_blueprint.route('')
@login_required
def index():
    return render_template(
        'index.html',
        page_title_text="Home"
    )
