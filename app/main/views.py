from flask import render_template, request, redirect, url_for, flash
from ..models import registration,blogs, coments, contacts, newslater
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash,check_password_hash
from .. import db
from . import root
import requests
import os
from flask_login import login_user, current_user
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
import urllib.request, json
# from ..request import get_quotes


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'app/static/uploads/'
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@root.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        Blogtitle = request.form['Blogtitle']
        blogpitch = request.form['blogpitch']
        Blogbody = request.form['Blogbody']
        postedby = current_user.useremail

        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(url_for('profile'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        filenames = filename.rsplit('.', 1)
        fname = filenames[0]
        lname = filenames[1]
        fullnames = fname + "." + lname
        # commit db
        send_image = blogs(post = Blogbody,postby = postedby,blog_image = fullnames,blog_title = Blogtitle,blog_pitch = blogpitch)
        db.session.add(send_image)
        db.session.commit()
        flash("Image upload successfull")
        # send email
        # msg = Message('Hello', sender = 'techrollblogs@gmail.com', recipients = [useremails])
        # msg.body = "Hello thank you for signing up to this page, you can check my blogs at techrollblogs.epizy.com"
        # mail.send(msg)

    title = "Techrollblogs | Home-page"
    names = current_user
    getblogs = blogs.query.order_by(blogs.id.desc()).all()
    base_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    req = requests.get(base_url)
    data = json.loads(req.content)
    return render_template('home.html', title = title, names = names, getblogs = getblogs , data = data)

@root.route('/contact', methods = ['POST','GET'])
def contact():
    if request.method == 'POST':
        contact = request.form['contacts']
        useremail = request.form['useremail']
        messages = request.form['messages']
        new_message = contacts(phone = contact, useremail = useremail, message = messages)
        db.session.add(new_message)
        db.session.commit()
        flash("<span style='color:green;'>Message sent, a reply will be sent to your email</span>")
        return redirect(request.referrer)

    title = "Techrollblogs | contact-page"
    return render_template('contact.html', title = title)

@root.route('/about', methods = ['POST','GET'])
def about():
    title = "Techrollblogs | About--page"
    return render_template('about.html', title = title)

@root.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        useremail = request.form['useremail']
        upassword = request.form['upassword']
        get_users = registration.query.filter_by(useremail = useremail).first()
        if get_users:
            passwrds = get_users.password
            verifypass = check_password_hash(passwrds, upassword)
            if verifypass:
                login_user(get_users, remember = True)
                return redirect(url_for('root.index'))
            else:
                flash("wrong password, please try again")
        else:
            flash("user with this username dont exist")
    title = "Techrollblogs | Login-page"
    return render_template('login.html', title = title)

@root.route('/signup', methods = ['POST','GET'])
def signup():
    if request.method == 'POST':
        usernames = request.form['useremail']
        passwords = request.form['password']
        passhash = generate_password_hash(passwords)
        check_user = registration.query.filter_by(useremail = usernames).first()
        if check_user:
            flash("user with this username already exist")
        else:
            new_user = registration(username = usernames, useremail = usernames, password = passhash)
            db.session.add(new_user)
            sends = db.session.commit()
            if sends:
                
                return redirect(url_for('login'))
            else:
                return redirect(request.referrer)
    title = "Techrollblogs | Signup-page"
    return render_template('signup.html', title = title)

@root.route("/seecoments/<int:id>")
def seecoments(id):
    getoneblogs = blogs.query.filter_by(id = id).all()
    getcomment = coments.query.filter_by(id = id).all()
    return render_template('seecomments.html', getoneblogs = getoneblogs, getcomment = getcomment)

@root.route('/postcomments', methods = ['POST','GET'])
def postcomments():
    if request.method == 'POST':
        comments = request.form['postcomm']
        new_comment = coments(comment = comments)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.referrer)


@root.route('/signupnewslater', methods = ['POST','GET'])
def signupnewslater():
     if request.method == 'POST':
        signupemail = request.form['signupemail']
        new_signups = newslater(useremail = signupemail)
        db.session.add(new_signups)
        db.session.commit()
        return redirect(request.referrer)