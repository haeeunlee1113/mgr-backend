from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # project module
from FOODINFO.flask_model.route import info_route

app = Flask(__name__)  ##db info setting
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://mgrsdp:ajrrjfl!@mgrsdp.c8ybdvubh7vg.ap-northeast-2.rds.amazonaws.com/mgrsdp"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)
app.register_blueprint(info_route.info_route)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

