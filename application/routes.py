from datetime import datetime as dt

from flask import render_template, url_for, redirect, flash, request, Markup
from flask import current_app as app
from .forms import ContactForm, PostForm
from .models import db, MessageModel, PostModel


@app.route('/')
def index():
    return render_template("posts.html")


@app.route('/')
@app.route('/posts')
def posts():
    posts = PostModel.query.all()
    return render_template("posts.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/post/new', methods=["GET", "POST"])
def new_post():
    """ Route for adding new article """
    form = PostForm()
    if form.validate_on_submit():
        title = request.form.get("title")
        body = request.form.get("body")
        tags = request.form.get("tags") # TODO check how to do multiple strings..
        post = PostModel(title=title,
                         body=body,
                         tags=tags,
                         time_posted=dt.now())
        db.session.add(post)
        db.session.commit()
        flash(f"Post '{title}' was saved to database", 'success')
        return redirect(url_for("new_post"))
    return render_template("new_post.html", form=form)

    
@app.route('/post/<int:post_id>')
def post(post_id:int):
    post = PostModel.query.get_or_404(post_id)
    return render_template("post.html", post=post)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    """ Route for processing the contact form """
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