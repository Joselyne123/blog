from flask import render_template,request,redirect,url_for,abort,flash
from . import users
from flask_login import login_required,current_user
from ..models import User,Comment,Blog
from .forms import CommentForm
from .. import db

#lists of blogs
@users.route('/<username>')
def user_post(username):
    page = request.args.get('page', 1, type = int)
    user = User.query.filter_by(username = username).first_or_404()
    blog_posts = Blog.query.filter_by(author=user).order_by(Blog.posted.desc()).pagenate(page=page, per_page=10)
    return render_template('user_post.html', blog_posts = blog_posts, user = user)

@users.route('users/<int:id>')
def comment(id):
    post = Blog.query.filter_by(id=id).first()
    return render_template('view_comments.html',post=post,id=id)

@users.route('/users/<int:id>/comment', methods = ['GET','POST'])
@login_required
def post_comment(id):
    comments = Comment.query.filter_by(id=id).all()
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(body = form.body.data,
                            blog_id = id,
                          author_id= current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Comments added successfuly!')
        return redirect(url_for('.comment', id=id))

    # from pprint import pprint
    # pprint(post)
    return render_template('comment.html',comments =comments, comment_form=form)




