from datetime import datetime as dt

from flask import render_template, url_for, redirect, flash, request, Markup
from flask import current_app as app
from flask_login import login_user, logout_user, current_user, login_required

from . import bcrypt
from .forms import ContactForm, PostForm, ProjectForm, AdminForm
from .models import db, MessageModel, PostModel, ProjectModel, AdminModel # TODO sjednotit nazvy


@app.route('/')
def index():
    posts = PostModel.query.all()
    return render_template("posts.html", posts=posts)


@app.route('/posts')
def posts():
    posts = PostModel.query.all()
    return render_template("posts.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/projects')
def projects():
    """ Route for seeing all my projects """

    projects = ProjectModel.query.all()
    return render_template("projects.html", projects=projects)


@app.route('/post/add', methods=["GET", "POST"])
@login_required
def add_post():
    """ Route for adding new article """

    form = PostForm()
    if form.validate_on_submit():
        title = request.form.get("title")
        body = request.form.get("body")
        tags = request.form.get("tags") # TODO check how to do multiple strings..
        # print(request.form.get("title"), form.title.data) # DEBUG stejne?
        post = PostModel(title=title,
                         body=body,
                         tags=tags,
                         time_posted=dt.now())
        db.session.add(post)
        db.session.commit()
        flash(f"Post '{title}' was saved to database", 'success')
        return redirect(url_for("post", post_id=post.id))
    return render_template("add_post.html", title="Add New Post", form=form)


@app.route('/post/<int:post_id>/edit', methods=["GET", "POST"])
@login_required
def edit_post(post_id:int):
    """ Route for editing a post """

    post = PostModel.query.get_or_404(post_id)
    form = PostForm()
    # show the current text
    if request.method == "GET":
        form.title.data = post.title
        form.body.data = post.body
    # update and save the changed text
    elif form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.commit()
        flash("Post updated!", "success")
        return redirect(url_for("post", post_id=post.id))
    return render_template("add_post.html", title="Edit Post", form=form)


# TODO napojit na nejakej cudlik
@app.route('/post/<int:post_id>/delete', methods=["POST"])
@login_required
def delete_post(post_id:int):
    """ Route for deleting a post """

    post = PostModel.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash(f"Post {post.title} deleted!", "success")
    return redirect(url_for("posts"))


@app.route('/post/<int:post_id>')
def post(post_id:int):
    post = PostModel.query.get_or_404(post_id)
    return render_template("post.html", post=post)


@app.route('/project/add', methods=["GET", "POST"])
def add_project():
    """ Route for adding project """

    form = ProjectForm()
    if form.validate_on_submit():
        project = ProjectModel( title=form.title.data,
                                description=form.description.data,
                                project_url=form.project_url.data,
                                github_url=form.github_url.data,
                                time_added=dt.now()
        )
        db.session.add(project)
        db.session.commit()
        flash(f"Project '{form.title.data}' was saved to database", "success")
        return redirect(url_for("projects"))
    return render_template("add_project.html", title="Add project", form=form)



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
    return render_template("contact.html", title="Send me a message", form=form)


@app.route('/admin', methods=["GET", "POST"])
def admin():
    """ Route for logging as admin -> needed for creating/updating/deleting posts """

    form = AdminForm()
    if form.validate_on_submit():
        admin = AdminModel.query.filter_by(email="kotatko.lukas@gmail.com").first()
        if bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            flash("You are logged in!", "success")
            return redirect(url_for("posts"))
        flash("Login failed!", "danger")
    return render_template("admin.html", form=form)