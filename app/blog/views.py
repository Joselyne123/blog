from flask import render_template,request,redirect,url_for,abort,flash
from . import blog
from flask_login import login_required,current_user
from ..models import User,Blog,Comment
from .forms import PostForm ,CommentForm
from .. import db

#Create a blog
@blog.route('/create',methods = ['GET','POST'])
@login_required
def create_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = Blog(title = post_form.title.data,
                    body = post_form.body.data,
                    user_id = current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post saved')
        return redirect(url_for('main.index'))
    return render_template('blog/create_post.html', post_form=post_form)

# VIEW A POST
@blog.route('blog/<int:post_id>')
def post(post_id):
    post = Blog.query.get_or_404(post_id)
    return render_template('blog/post.html', title =post.title, date = post.posted, post = post)

@blog.route('blog/<int:post_id>/update', methods = ['GET', 'POST'])
@login_required
def update(post_id):
    '''
    function to update post
    '''
    post = Blog.query.get_or_404(post_id)
    if post.author!=current_user:
        #403 error is forbidden
        abort(403)
    post_form  = PostForm()

    if post_form.validate_on_submit():
        post.title = post_form.title.data
        post.body = post_form.body.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('blog.post', post_id=post.id))

    elif request.method == 'GET':
        post_form.title.data = post.title
        post_form.body.data = post.body

    return render_template('blog/create_post.html',title = 'Updating', post_form = post_form)


@blog.route('blog/<int:post_id>/delete', methods = ['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Blog.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    flash('Post deleted.')
    return redirect(url_for('main.index'))


@blog.route('comment/<int:id>')
def comment(id):
    post =Blog.query.filter_by(id=id).first()
    return render_template('blog/view_comments.html', post = post,id=id)

@blog.route('/blog/<int:id>/comment', methods = ['GET','POST'])
@login_required
def new_comment(id):
    # import pdb;pdb.set_trace()
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
    # import pdb;pdb.set_trace()
    return render_template('blog/comment.html',comments =comments, comment_form=form)

@blog.route('comment/<int:id>/delete', methods = ['GET', 'POST'])
@login_required
def delete_comment(id):
    comments = Comment.query.filter_by(id=id).all()
    # if post.author!=current_user:
    #     abort(403)

    # db.session.delete(comment)
    # db.session.commit()

    flash('Comment deleted.')
    return redirect(url_for('main.index'))

