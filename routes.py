from flask import Flask, render_template
app = Flask(__name__)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Home')

if __name__ == '__main__':
    app.run(debug=True)
