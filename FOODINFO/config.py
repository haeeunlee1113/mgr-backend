from flask import Flask

db = {
    'user': 'mgrsdp',
    'password': 'ajrrjfl!',
    'host': 'mgrsdp.c8ybdvubh7vg.ap-northeast-2.rds.amazonaws.com',
    'port': 3306,
    'database': 'mgrsdp'
}


db_url = f"mysql+mysqlconnector://{db['user']}:{db['password']}""@" \
         f"{db['host']}:{db['port']}/{db['database']}"


def getFlaskApp(self):
    app = Flask(self.flask_application_name, template_folder=self.flask_template_folder)
    if self.session_auto_timeout != None:
        app.config["SQLALCHEMY_POOL_RECYCLE"] = self.session_auto_timeout
    self.setupFlaskApplication(app)
    return app