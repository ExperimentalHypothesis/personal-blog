from datetime import datetime as dt

from flask import render_template, url_for, redirect, flash, request
from flask import current_app as app
from application.forms import ContactForm
from application.models import db, MessageModel

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/posts')
def posts():
    return render_template("posts.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    """ Process the contact form """
    form = ContactForm()
    if form.validate_on_submit():
        name = request.form.get("name")
        email = request.form.get("email")
        body = request.form.get("body")
        message = MessageModel( name=name,
                                email=email, 
                                body=body, 
                                time_sent=dt.now())
        db.session.add(message)
        db.session.commit()
        flash(f"Your message was sent succesfully. Thank you!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", title="Contact Me", form=form)