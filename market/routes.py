from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, valueform,onoff,working
from market import db
from flask_login import login_user, logout_user, login_required, current_user
import pandas as pd
import numpy as np


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    form = valueform()
    stock1=[]
    trigger1=[]
    stop_value1=[]
    limit_value1=[]
    type1=[]
    quantity1=[]
    order1=[]
    form1=onoff()
    df3 = pd.read_csv("system.csv")
    if form1.validate_on_submit():
        if df3['system'].iloc[1]=='on':
            # df3=df3.set_index('system')
            df3['system'].iloc[1]='off'


        elif df3['system'].iloc[1]=='off':
            # df3=df3.set_index('system')
            df3['system'].iloc[1]='on'

            print(df3['system'].iloc[1])

        df3.set_index('system')
        df3.to_csv('system.csv')

    form2=working()
    if form2.validate_on_submit():
        pass

    # if form.validate_on_restart():
    #     flash("The bot Restarted from first", category='success')
    if form.validate_on_submit():
        # for i in range(5):
        stock1.append(form.stock1.data)
        trigger1.append(form.trigger1.data)
        stop_value1.append(form.stop_value1.data)
        limit_value1.append(form.limit_value1.data)
        type1.append(form.type1.data)
        quantity1.append(form.quantity1.data)
        order1.append(form.order1.data)

        stock1.append(form.stock2.data)
        trigger1.append(form.trigger2.data)
        stop_value1.append(form.stop_value2.data)
        limit_value1.append(form.limit_value2.data)
        type1.append(form.type2.data)
        quantity1.append(form.quantity2.data)
        order1.append(form.order2.data)

        stock1.append(form.stock3.data)
        trigger1.append(form.trigger3.data)
        stop_value1.append(form.stop_value3.data)
        limit_value1.append(form.limit_value3.data)
        type1.append(form.type3.data)
        quantity1.append(form.quantity3.data)
        order1.append(form.order3.data)

        stock1.append(form.stock4.data)
        trigger1.append(form.trigger4.data)
        stop_value1.append(form.stop_value4.data)
        limit_value1.append(form.limit_value4.data)
        type1.append(form.type4.data)
        quantity1.append(form.quantity4.data)
        order1.append(form.order4.data)


        stock1.append(form.stock5.data)
        trigger1.append(form.trigger5.data)
        stop_value1.append(form.stop_value5.data)
        limit_value1.append(form.limit_value5.data)
        type1.append(form.type5.data)
        quantity1.append(form.quantity5.data)
        order1.append(form.order5.data)



        df1=pd.DataFrame()
        df1['instrument']=np.array(stock1)
        df1['trigger']=np.array(trigger1)
        df1['stop_value']=np.array(stop_value1)
        df1['limit_value']=np.array(limit_value1)
        df1['type']=np.array(type1)
        df1['quantity']=np.array(quantity1)
        df1['buy/sell']=np.array(order1)

        df3 = pd.read_csv("system.csv")
        df3['system'].iloc[2]=str(form.apikey.data)
        df3['system'].iloc[3]=str(form.apisecretkey.data)
        df3=df3.set_index('system')
        df3.to_csv('system.csv')
        
        df1.to_csv('strategy.csv')
        print(stock1[1])
        flash(f"data sent successfully ", category='success')
        return redirect(url_for('market_page'))

    df = pd.read_csv("strategy.csv")
    print(df3['system'][2])
    print(df)
    return render_template('market.html', form=form,data=df,form2=form2,form1=form1,data1=df3)




    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error: {err_msg}', category='danger')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))

@app.route('/addRegion', methods=['POST'])
def addRegion(form):
    
    return (request.form['projectFilePath'])


