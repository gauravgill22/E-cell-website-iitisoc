from flask import Flask, render_template, request, send_file
import smtplib
from dotenv import dotenv_values
import os
from email.mime.multipart import MIMEMultipart
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
mail=Mail(app)


app.config['SECRET_KEY']=os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='dummyid4ecell@gmail.com'
app.config['MAIL_PASSWORD']=os.environ.get("DUMMY_PASSWORD")
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    subject=db.Column(db.String(100),nullable=False)
    message=db.Column(db.String(500),nullable=False)




@app.route("/")
@app.route("/home")
def homeadwork():
    
    return render_template('homeadwork.html')

@app.route("/about") 
def about():
   
    return render_template('about.html')

@app.route("/query")
def query():
   
    return render_template('query.html')

@app.route("/resources")
def resources():
    return render_template('resources.html')

@app.route("/book1")
def book1():
    p="static\\Rich Dad, Poor Dad What the Rich Teach Their Kids About Money--That the Poor and Middle Class Do Not by Robert T. Kiyosaki, Sharon L. Lechter (z-lib.org).pdf"
    return send_file(p,as_attachment=True)

@app.route("/book2")
def book2():
    p="static\\The Lean Startup How Todays Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses by Eric Ries (z-lib.org).pdf"
    return send_file(p,as_attachment=True)

@app.route("/book3")
def book3():
    p="static\\The Entrepreneur Mind 100 Essential Beliefs, Characteristics, and Habits of Elite Entrepreneurs by Kevin D. Johnson (z-lib.org).pdf"
    return send_file(p,as_attachment=True)


@app.route("/book4")
def book4():
    p="static\\Rework by Jason Fried, David Heinemeier Hansson (z-lib.org).pdf"
    return send_file(p,as_attachment=True)

@app.route("/team")
def team():
    return render_template('team.html')


@app.route("/thankyou", methods=["POST"])
def thankyou():
    
    name=request.form.get('Name',type=str)
    subject=request.form.get('Subject',type=str)
    message=request.form.get('Message')
    email=request.form.get('Email')
    


    if not name or not subject or not email or not message:
        error_stmt="All form fields required"
        return render_template("fail.html",error_stmt=error_stmt,name=name,subject=subject,email=email,message=message)
    elif name and subject and message and email:
        msg=Message("Your query has been received ",sender='dummyid4ecell@gmail.com',recipients=[email])
        msg.body="""
        {},
        Thank you for your message!
        Here's what we got from you

        Email:{}
        Subject:{}
        Message:{}

        We'll get back to you soon.
        Regards,
        E-cell,IIT Indore""".format(name,email,subject,message)
        mail.send(msg)
        user=User(name=name,email=email,subject=subject,message=message)
        db.session.add(user)
        db.session.commit()

        return render_template('thankyou.html',name=name,subject=subject, message=message,email=email)
 

if __name__=='__main__':
    app.run(debug=True)