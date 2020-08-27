import os
import logging
from dotenv import load_dotenv
from flask import Flask, redirect
load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

app = Flask(__name__, static_url_path='', static_folder='static')

app.config.from_mapping(SQLALCHEMY_TRACK_MODIFICATIONS=False,
                        SQLALCHEMY_DATABASE_URI=os.environ.get(
                            'DATABASE_URL', 'sqlite:///app.sqlite'))

with app.app_context():
    from core import get_blueprint
    from core.db import db  # NOQA

NAME = os.environ.get('NAME')
TOKEN = os.environ.get('TOKEN')

bp = get_blueprint(TOKEN, NAME)
app.register_blueprint(bp)


@app.route('/')
def index():
    return redirect('index.html')


if __name__ == '__main__':
    app.run()
