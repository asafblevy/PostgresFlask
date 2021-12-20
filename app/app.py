import os
import json

from flask import Flask

app = Flask(__name__)

dbUser = os.environ.get('POSTGRESQL_USERNAME')
dbPassword = os.environ.get('POSTGRESQL_PASSWORD')
dbHost = os.environ.get('POSTGRESQL_HOST')

config = {
    'DATABASE_URI': "postgresql://%s:%s@%s:5432" % (dbUser, dbPassword, dbHost),
    'HOSTNAME': os.environ['HOSTNAME'],
    'GREETING': os.environ.get('GREETING', 'Hello'),

    
}

@app.route("/")
def hello():
    return config['GREETING'] + ' from ' + config['HOSTNAME'] + '!'

@app.route("/config")
def configuration():
    return json.dumps(config)


@app.route("/version")
def version():
    return {"version": "0.2"}

@app.route('/db')
def db():
    from sqlalchemy import create_engine

    engine = create_engine(config['DATABASE_URI'], echo=True)
    rows = []
    with engine.connect() as connection:
        result = connection.execute("select name, age from anzu;")
        rows = [dict(r.items()) for r in result]
    return json.dumps(rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80', debug=True)