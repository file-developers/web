from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class NewProjectForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    description = StringField('Description:', validators=[Length(min=20, max=200)])
    submit = SubmitField('Submit')
