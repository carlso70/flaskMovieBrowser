from flask import Flask, render_template, request, url_for
import movie_request

app = Flask(__name__)

@app.route('/')
def view_search_page():
    return render_template('search_page.html')


@app.route('/search/', methods=['POST'])
def display_results():
	title = request.form['title']
	year = request.form['year']
	data = movie_request.get_movie_info(str(title),str(year))
	return render_template('result_page.html', title=data['Title'], year=data['Released'], poster=data['Poster'])


if __name__=="__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)
