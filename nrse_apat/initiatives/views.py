from flask import render_template, Blueprint
from flask_security import login_required

initiatives_blueprint = Blueprint('initiatives_blueprint', __name__)

@initiatives_blueprint.route('')
@login_required
def index():
    return render_template(
        'initiatives/index.html',
        page_title_text='Initiatives'
    )