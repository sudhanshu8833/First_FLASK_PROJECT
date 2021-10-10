from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User
import pandas as pd



class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class working(FlaskForm):
    df2 = pd.read_csv("system.csv")
    submit = SubmitField(label=str(df2['system'].iloc[0]))

class onoff(FlaskForm):
    df2 = pd.read_csv("system.csv")
    submit = SubmitField(label='on/off') 

class valueform(FlaskForm):
    
    stock1=StringField(label='Stock:', validators=[Length(min=1, max=30), DataRequired()])
    trigger1=StringField(label='Trigger according to:', validators=[DataRequired()])
    stop_value1=StringField(label='value:', validators=[Length(min=1), DataRequired()])
    limit_value1=StringField(label='stop_value:', validators=[DataRequired()])
    quantity1=StringField(label='quantity:', validators=[DataRequired()])
    type1=StringField(label='quantity:', validators=[DataRequired()])
    order1=StringField(label='order type:', validators=[DataRequired()])


    stock2 = StringField(label='Stock:', validators=[Length(min=1, max=30), DataRequired()])
    trigger2 = StringField(label='Trigger according to:', validators=[DataRequired()])
    stop_value2 = StringField(label='value:', validators=[Length(min=1), DataRequired()])
    limit_value2 = StringField(label='Confirm Password:', validators=[DataRequired()])
    quantity2=StringField(label='quantity:', validators=[DataRequired()])
    type2=StringField(label='quantity:', validators=[DataRequired()])
    order2=StringField(label='order type:', validators=[DataRequired()])

    stock3=StringField(label='Stock:', validators=[Length(min=1, max=30), DataRequired()])
    trigger3=StringField(label='Trigger according to:', validators=[DataRequired()])
    stop_value3=StringField(label='value:', validators=[Length(min=1), DataRequired()])
    limit_value3=StringField(label='Confirm Password:', validators=[DataRequired()])
    quantity3=StringField(label='quantity:', validators=[DataRequired()])
    type3=StringField(label='quantity:', validators=[DataRequired()])
    order3=StringField(label='order type:', validators=[DataRequired()])

    stock4=StringField(label='Stock:', validators=[Length(min=1, max=30), DataRequired()])
    trigger4=StringField(label='Trigger according to:', validators=[DataRequired()])
    stop_value4=StringField(label='value:', validators=[Length(min=1), DataRequired()])
    limit_value4=StringField(label='Confirm Password:', validators=[DataRequired()])
    quantity4=StringField(label='quantity:', validators=[DataRequired()])
    type4=StringField(label='quantity:', validators=[DataRequired()])
    order4=StringField(label='order type:', validators=[DataRequired()])

    stock5=StringField(label='Stock:', validators=[Length(min=1, max=30), DataRequired()])
    trigger5=StringField(label='Trigger according to:', validators=[DataRequired()])
    stop_value5=StringField(label='value:', validators=[Length(min=1), DataRequired()])
    limit_value5=StringField(label='Confirm Password:', validators=[DataRequired()])
    quantity5=StringField(label='quantity:', validators=[DataRequired()])
    type5=StringField(label='quantity:', validators=[DataRequired()])
    order5=StringField(label='order type:', validators=[DataRequired()])

    apikey=StringField(label='ApiKey', validators=[DataRequired()])
    apisecretkey=StringField(label='Api Secret Key', validators=[DataRequired()])
    submit=SubmitField(label='Submit')

    # restart=SubmitField(label='Restart')


    # stock=[]
    # trigger=[]
    # stop_value=[]
    # limit_value=[]
    # for i in range(5):
    #     stock.append(StringField(label='Stock:', validators=[Length(min=1, max=30), DataRequired()]))
    #     trigger.append(StringField(label='Trigger according to:', validators=[DataRequired()]))
    #     stop_value.append(StringField(label='value:', validators=[Length(min=1), DataRequired()]))
    #     limit_value.append(PasswordField(label='Confirm Password:', validators=[DataRequired()]))
    # submit = SubmitField(label='Submit')


