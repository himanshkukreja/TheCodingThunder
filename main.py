from flask import Flask,render_template, request, session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail


local_server=True
with open('config.json','r') as c:
  params = json.load(c)["params"]

app = Flask(__name__)
app.secret_key = 'secret-key'
app.config.update(
  MAIL_SERVER = 'smtp.gmail.com',
  MAIL_PORT ='465',
  MAIL_USE_SSL = "True",
  MAIL_USERNAME=params['gmail_username'],
  MAIL_PASSWORD=params['gmail_password']
)

mail =Mail(app)

if(local_server):
  app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),  nullable=False)
    email = db.Column(db.String(255),  nullable=False)
    phone_num = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255),  nullable=False)
    date = db.Column(db.String, nullable=True)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255),  nullable=False)
    subtitle = db.Column(db.String(255),  nullable=False)
    slug = db.Column(db.String(25),  nullable=False)
    content = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String, nullable=True)

@app.route('/')
def home():
  posts = Posts.query.filter_by().all()[0:params["no_of_posts"]]
  return render_template('index.html',params = params, posts = posts)

@app.route('/about')
def about():
  return render_template('about.html',params = params)

@app.route('/contact', methods= ['GET', 'POST'])
def contact():
    if(request.method=="POST"):
        name = request.form.get('name')
        email =request.form.get('email')
        phone =request.form.get('phone')
        message =request.form.get('message')
        
        entry= Contacts(name=name, email=email, phone_num=phone, message=message, date=datetime.now())

        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name, 
                           sender= email, 
                           recipients =[params['gmail_username']],
                           body = message + "\n" + phone
                         )

    return render_template('contact.html',params = params)

@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
  post = Posts.query.filter_by(slug=post_slug).first()
  return render_template('post.html',params = params, post = post)



@app.route('/admin', methods=['GET', 'POST'])
def dashboard():

  if ('user' in session and session['user']==params['admin_user']):
    posts = Posts.query.all()
    return render_template('dashboard.html',params = params, posts=posts)
  if (request.method == "POST"):
    username = request.form.get('uname')
    password = request.form.get('pass')
    if (username==params['admin_user']  and password==params['admin_password']):
      session['user'] = username
      posts = Posts.query.all()
      return render_template('dashboard.html',params = params, posts=posts)
  else:
    return render_template('signin.html',params = params)

@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def edit(sno):
  if ('user' in session and session['user']==params['admin_user']):
    if request.method == "POST":
      box_title = request.form.get('title')
      tagline = request.form.get('tagline')
      slug = request.form.get('slug')
      content = request.form.get('content')
      img_file = request.form.get('img_file')

      if sno =='0':
        entry = Posts(title=box_title, slug= slug, content=content, tagline = tagline, img = img_file)
        db.session.add(entry)
        db.session.commit()

    return render_template('edit.html', params=params, sno=sno)




app.run(port=500, debug=True)