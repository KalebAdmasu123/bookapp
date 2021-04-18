import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project One: TODO"

#class User(db.Model):
 #   __tablename__='users'

  #  id=db.Column(db.Integer,primary_key=True)
   # name=db.Column(db.String,unique=True)
   # email=db.Column(db.String,unique=True)

#@app.route("/new",method=['get','post'])
#def new():
 #   if request.method=='POST':
  #      email=request.form['email']
   #     name=request.form['name']

    #    user=User(name=name,email=email)
     #   db.session.add(user)
      #  db.session.commit()
    #return render_template('new.html')
#@app.route("/user/<username>")
#def users(username):
 #   user=User.query.filter_by(name)

