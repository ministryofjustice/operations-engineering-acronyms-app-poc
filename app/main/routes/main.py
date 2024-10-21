from flask import Blueprint, current_app, redirect, render_template, request
from ...models import Acronym


main = Blueprint("main", __name__)

@main.route("/")
def index():

    # Query users from the database (example)
    acronyms = Acronym.query.all()

    return render_template('pages/main.html', acronyms=acronyms)