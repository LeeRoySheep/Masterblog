from flask import Flask, render_template, request, redirect, url_for
from storage_handler import StorageHandler

#Setting up the Flask app
app = Flask(__name__)
#Creating an instance of the StorageHandler class
#and passing the path to the JSON file
storage = StorageHandler('storage/data.json')


@app.route('/')
def index():
    """
    Flask route to render the index.html template
    :return:
    """
    blog_posts = storage.comments
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Flask route to add a new blog post
    :return:
    """
    if request.method == 'POST':
        blog_posts = storage.comments
        new_post = dict()
        new_post["id"] = blog_posts[len(blog_posts)-1]["id"] + 1
        new_post["title"] = request.form.get('title')
        new_post["author"] = request.form.get('name')
        new_post["content"] = request.form.get('comment')
        blog_posts.append(new_post)
        storage.comments = blog_posts
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """
    Flask route to delete a blog post by id
    :param post_id:
    :return:
    """
    post = storage.fetch_by_id(post_id)
    storage.comments = storage.comments.remove(post)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Flask route to update a blog post by id
    :param post_id:
    :return:
    """
    # Fetch the post from the JSON file by id
    post = storage.fetch_by_id(post_id)
    if request.method == 'POST':
        blog_posts = storage.comments
        for pos in blog_posts:
            if pos["id"] == post_id:
                pos["author"] = request.form.get('name')
                pos["content"] = request.form.get('comment')
                storage.comments = blog_posts
                return redirect(url_for('index'))
    return render_template('update.html', post=post)


@app.route('/like/<int:post_id>')
def like(post_id):
    """
    Flask route to like a blog post
    :param post_id:
    :return:
    """
    blog_posts = storage.comments
    for post in blog_posts:
        if post["id"] == post_id:
            post["likes"] = post.get("likes", 0) + 1
            storage.comments = blog_posts
            break
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    """
    Flask error handler for 404 page not found
    :param error:
    :return:
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Flask error handler for 500 internal server error
    :param error:
    :return:
    """
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
