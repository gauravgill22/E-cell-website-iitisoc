from flask import Flask, render_template, request, send_file,redirect,flash,get_flashed_messages
import smtplib
from dotenv import dotenv_values
import os
from email.mime.multipart import MIMEMultipart
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename




app=Flask(__name__)
mail=Mail(app)


app.config['SECRET_KEY']=os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_BINDS']={'Inspire':'sqlite:///db2.sqlite3','Subscribe':'sqlite:///db3.sqlite3'}
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

class Inspire(db.Model):
    __bind_key__='Inspire'
    id=db.Column(db.Integer,primary_key=True)
    pname=db.Column(db.String(50),nullable=False)
    pemail=db.Column(db.String(50),nullable=False)
    ptitle=db.Column(db.String(200),nullable=False)
   





class Subscribe(db.Model):
    __bind_key__='Subscribe'
    id=db.Column(db.Integer,primary_key=True)
    semail=db.Column(db.String(50),nullable=False)
   





@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def homeadwork():
    if request.method=="POST":
        semail=request.form.get('Email Address')
        if not semail:
            print("Email address not entered")
            return render_template('homeadwork.html',dangeralert=True)
        else:
            subscribe=Subscribe(semail=semail)
            db.session.add(subscribe)
            db.session.commit()
            print("email address added to database from home")
            return render_template('homeadwork.html',sweetalert=True)
            
    return render_template('homeadwork.html')



@app.route("/query")
def query():
   
    return render_template('query.html')

@app.route("/resourses",methods=["GET","POST"])
def resourses():
    if request.method=="POST":
        semail=request.form.get('Email Address')
        if not semail:
            print("Email address not entered")
            return render_template('resourses.html',dangeralert=True)
        else:
            subscribe=Subscribe(semail=semail)
            db.session.add(subscribe)
            db.session.commit()
            print("email address added to database from resources")
            return render_template('resourses.html',salert=True)
    return render_template('resourses.html')


@app.route("/blog",methods=["GET","POST"])
def blog():
    if request.method=="POST":
        semail=request.form.get('Email Address')
        if not semail:
            print("Email address not entered")
            return render_template('blog.html',dangeralert=True)
        else:
            subscribe=Subscribe(semail=semail)
            db.session.add(subscribe)
            db.session.commit()
            print("email address added to database from blogs")
            return render_template('blog.html',salert=True)
    return render_template('blog.html')

@app.route("/books",methods=["GET","POST"])
def books():
    if request.method=="POST":
        semail=request.form.get('Email Address')
        if not semail:
            print("Email address not entered")
            return render_template('books.html',dangeralert=True)
        else:
            subscribe=Subscribe(semail=semail)
            db.session.add(subscribe)
            db.session.commit()
            print("email address added to database from books")
            return render_template('books.html',salert=True)
    return render_template('books.html')

@app.route("/videos",methods=["GET","POST"])
def videos():
    if request.method=="POST":
        semail=request.form.get('Email Address')
        if not semail:
            print("Email address not entered")
            return render_template('video.html',dangeralert=True)
        else:
            subscribe=Subscribe(semail=semail)
            db.session.add(subscribe)
            db.session.commit()
            print("email address added to database from videos")
            return render_template('video.html',salert=True)
    return render_template('video.html')

@app.route("/blog1")
def blog1():
    return render_template('blog1.html')

@app.route("/blog2")
def blog2():
    return render_template('blog2.html')

@app.route("/blog3")
def blog3():
    return render_template('blog3.html')

@app.route("/blog4")
def blog4():
    return render_template('blog4.html')

@app.route("/blog5")
def blog5():
    return render_template('blog5.html')

@app.route("/diaries",methods=["GET","POST"])
def diaries():
    if request.method=="POST":
        semail=request.form.get('Email Address')
        if not semail:
            print("Email address not entered")
            return render_template('diaries.html',dangeralert=True)
        else:
            subscribe=Subscribe(semail=semail)
            db.session.add(subscribe)
            db.session.commit()
            print("email address added to database from diaries")
            return render_template('diaries.html',salert=True)
    return render_template('diaries.html')



@app.route("/team",methods=["GET","POST"])
def team():
    if request.method=="POST":
        semail=request.form.get('Email Address')
        if not semail:
            print("Email address not entered")
            return render_template('3team.html',dangeralert=True)
        else:
            subscribe=Subscribe(semail=semail)
            db.session.add(subscribe)
            db.session.commit()
            print("email address added to database from team")
            return render_template('3team.html',salert=True)
    return render_template('3team.html')

app.config['FILE_UPLOADS'] = "C:\\Users\\Sejal Kotian\\myproject\\static\\uploads"
app.config["ALLOWED_FILE_EXTENSIONS"]=["PNG","JPEG","PDF","JPG","DOCX"]
app.config["MAX_FILE_FILESIZE"]=0.8*1024*1024

def allowed_file(filename):
    if not "." in filename:
        return False
    ext =filename.rsplit(".",1)[1]
    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False

def allowed_file_filesize(filesize):

    if int(filesize) <= app.config["MAX_FILE_FILESIZE"]:
        return True
    else:
        return False





@app.route("/innovationandprojects", methods=["GET","POST"])
def innovationandprojects():
    if request.method=="POST":
        pname=request.form.get('Enter your Name',type=str)
        pemail=request.form.get('Enter your Email',type=str)
        ptitle=request.form.get('Project Title')

        if not pname or not pemail or not ptitle:
            flash("Couldn't submit.All form fields required!","warning")
            return render_template('innovationandprojects.html')
        else:
            inspire=Inspire(pname=pname,pemail=pemail,ptitle=ptitle)
            db.session.add(inspire)
            db.session.commit()
        
        if request.files:
            if not allowed_file_filesize(request.cookies.get('filesize')):
               print ("Filesize exceeded")
               flash("Couldn't upload,Filesize exceeded!","warning")
               return redirect(request.url)
            file=request.files["File"]
            if file.filename=="":
                print("File must have a filename")
                flash("File must be uploaded")
                return redirect(request.url)
            if not allowed_file(file.filename):
                print("The file extension was not allowed")
                return redirect(request.url)
            else:
                filename=secure_filename(file.filename)
                file.save(os.path.join(app.config['FILE_UPLOADS'],filename))
                print("FILE SAVED")
                flash("Congratulations!Your work has been submitted!","success")
                return render_template('innovationandprojects.html',happyalert=True)
            
            
        return render_template('innovationandprojects.html',pname=pname,pemail=pemail,ptitle=ptitle)
    else:
        return render_template('innovationandprojects.html')


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