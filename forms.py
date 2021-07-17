from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length, Email
class Queryform(FlaskForm):
    username=StringField('UserName',validators=[DataRequired(),Length (min=2,max=20)])
    email= StringField('Email',validators=[DataRequired(),Email()])
    message=StringField('Message',validators=[DataRequired(),Length(min=2,max=50)])
    submit=SubmitField('Submit')

