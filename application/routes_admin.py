from datetime import datetime as dt

from flask import current_app as app
from flask import render_template, url_for, redirect, flash, request, Markup
from flask_login import login_user, logout_user, current_user, login_required

from . import bcrypt
from .forms import PostForm, ProjectForm, AdminForm
from .models import db, PostModel, ProjectModel, AdminModel 


@app.route('/admin', methods=["GET", "POST"])
def admin():
    """ Route for logging as admin -> needed for creating/updating/deleting posts and projects """

    form = AdminForm()
    if form.validate_on_submit():
        admin = AdminModel.query.filter_by(email="kotatko.lukas@gmail.com").first()
        if bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            flash("You are logged in!", "success")
            return redirect(url_for("posts"))
        flash("Login failed!", "danger")
    return render_template("admin.html", form=form)


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



@app.route('/project/add', methods=["GET", "POST"])
@login_required
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
