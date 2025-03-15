from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open('storage/data.json', 'r', encoding="utf8") as handler:
        blog_posts = json.load(handler)
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
