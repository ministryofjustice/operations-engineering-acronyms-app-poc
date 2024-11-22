from flask import Blueprint, render_template, request, redirect, url_for
from ...models import Acronym

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    search_term = ""


    if request.method == "POST":
        search_term = request.form.get("name", "").strip()

        return redirect(url_for('main.index', name=search_term))

    search_term = request.args.get('name', '')
    if search_term:
        acronyms = Acronym.query.filter(Acronym.abbreviation.ilike(f"%{search_term}%")).all()

    else:
        acronyms = Acronym.query.all()

    return render_template("pages/main.html", acronyms=acronyms, search_term=search_term)
