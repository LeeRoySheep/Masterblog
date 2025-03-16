from flask import Flask, render_template, request, redirect, url_for
from storage_handler import StorageHandler

app = Flask(__name__)
storage = StorageHandler('storage/data.json')

@app.route('/')
def index():
    blog_posts = storage.comments
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        blog_posts = storage.comments
        new_post = dict()
        new_post["id"] = (len(blog_posts)+1)
        new_post["title"] = request.form.get('title')
        new_post["author"] = request.form.get('name')
        new_post["content"] = request.form.get('comment')
        blog_posts.append(new_post)
        storage.comments = blog_posts
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
