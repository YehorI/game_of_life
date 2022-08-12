from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange


class WHform(FlaskForm):
    width = IntegerField('Высота', validators=[NumberRange(2, 30)])
    height = IntegerField('Ширина', validators=[NumberRange(2, 30)])
    submit = SubmitField("Применить")