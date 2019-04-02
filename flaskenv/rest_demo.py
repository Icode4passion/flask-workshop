from flask import Flask , jsonify

app = Flask(__name__)

movies = [
{
	'id' : 1,
	'title': 'Batman',
	'Author': 'Bob Kane',
	'Director' : 'Christopher'
},
{
	'id' : 2,
	'title': 'Superman',
	'Author': 'Jerry Siegel',
	'Director' : 'Richard Donner'
	
}]

@app.route('/movies/api/v1.0/movies',methods=['GET'])
def get_tasks():
	return jsonify({'movies':movies})

if __name__ == '__main__':
	app.run(debug = True)
