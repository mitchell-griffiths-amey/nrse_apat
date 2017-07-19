from flask import render_template, Blueprint
from flask_security import login_required

actions_blueprint = Blueprint('actions_blueprint', __name__)

@actions_blueprint.route('')
@login_required
def index():
    return render_template(
        'actions/index.html',
        page_title_text='Actions'
    )