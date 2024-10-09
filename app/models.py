# pylint: disable=R0903
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Acronym(db.Model):
    __tablename__ = 'acronyms'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    abbreviation = db.Column(db.String, nullable=False)
    definition = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)

    __table_args__ = (db.UniqueConstraint('abbreviation', 'definition', name='_abbreviation_definition_uc'),)
