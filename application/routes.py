from datetime import datetime as dt

from flask import render_template, url_for, redirect, flash, request
from flask import current_app as app

from .forms import MessageForm
from .models import db, MessageModel, PostModel, ProjectModel


@app.route('/')
@app.route('/posts')
def index():
    """ Route for home page, the same as when clicked on posts in menu. """
    page = request.args.get("page", 1, type=int)
    posts = PostModel.query.order_by(PostModel.time_posted.desc()).paginate(page, per_page=12, error_out=True)
    return render_template("posts.html", posts=posts)


@app.route('/tech')
def tech():
    """ Route for tools and technologies. """
    return render_template("tech.html")


@app.route('/about')
def about():
    """ Route for info about me. """
    return render_template("about.html")


@app.route('/projects')
def projects():
    """ Route for seeing all my projects. """
    projects = ProjectModel.query.all()
    return render_template("projects.html", projects=projects)


@app.route('/post/<int:post_id>')
def post(post_id: int):
    """ Route for seeing single post. """
    post = PostModel.query.get_or_404(post_id)
    return render_template("post.html", post=post)


@app.route("/tag/<string:tag>")
def tagged_posts(tag: str):
    """ Route for seeing posts that have particular tag. """
    page = request.args.get("page", 1, type=int)
    contains_tag = PostModel.tags.contains(tag)
    posts = PostModel.query.filter(contains_tag).paginate(page, per_page=12, error_out=True)
    return render_template("tags.html", posts=posts)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    """ Route for processing the contact form. """
    form = MessageForm()
    if form.validate_on_submit():
        name = request.form.get("name")
        email = request.form.get("email")
        body = request.form.get("body")
        message = MessageModel(name=name,
                               email=email,
                               body=body,
                               time_sent=dt.now())
        db.session.add(message)
        db.session.commit()
        flash("Your message was sent succesfully. Thank you!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", title="Send me a message", form=form)
