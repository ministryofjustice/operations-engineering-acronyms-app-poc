from flask import Blueprint, render_template
from ...models import Acronym


main = Blueprint("main", __name__)


@main.route("/")
def index():

    # Query users from the database (example)
    acronyms = Acronym.query.all()

    return render_template('pages/main.html', acronyms=acronyms)
