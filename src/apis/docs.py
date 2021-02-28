from flask import Blueprint, render_template

docs_api = Blueprint('docs_api', __name__)


@docs_api.route("/docs")
def docs_get():
    return render_template('swaggerui.html')
