from flask import Flask,render_template,request
from articles import Articles
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password1!@localhost/blog'
db = SQLAlchemy(app)

class Data(db.Model):
	__tablename__ = "blog"
	id = db.Column(db.Integer, primary_key=True)
	head = db.Column(db.String(100),unique=True)
	author = db.Column(db.String(50))
	blog = db.Column(db.String(500))

	def __init__(self,head,author,blog):
		self.head = head
		self.author = author
		self.blog = blog




Articles = Articles()


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/aboutme')
def aboutme():
	return render_template('aboutme.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')
	 
@app.route('/process', methods = ['POST'])		
def process():
	pass
	if request.method == 'POST':
		_title = request.form['title']
		_author = request.form['author']
		print (_title,_author)
	# _name = request.form.get('name')
	# if _name :
		return render_template('response.html',title = _title ,author =_author)
	# else :
	# 	return "Error in Page try Again"
		
@app.route('/articles')
def articles():
	return render_template('articles.html',articles = Articles)

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/blog_success', methods = ['POST','GET'])
def blog_success():
	if request.method == 'POST':
		_title = request.form['head']
		_author = request.form['author_name']
		_blog = request.form['blog_name']
		print (_title,_author,_blog)
		data = Data(_title,_author,_blog)
		db.session.add(data)
		db.session.commit()
		datas = Data.query.all()
		return render_template('blog_success.html',datas = datas)


@app.route('/search',methods =['POST','GET'])
def search():
	if request.method == 'POST':
		result = Data.query.filter_by(head = 'Dog').all()
		print(result)
		return render_template('search.html',result = result)

	return render_template('search.html')












if __name__ == '__main__':
	app.run(debug=True)