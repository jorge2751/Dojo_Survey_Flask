from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    favorite_language = request.form['favorite-language']
    comments = request.form['comments']

    # Check that mandatory fields are not empty
    if not name or not location or not favorite_language:
        error = "Please fill out all mandatory fields."
        return render_template('index.html', error=error)

    session['name'] = name
    session['location'] = location
    session['favorite_language'] = favorite_language
    session['comments'] = comments

    return redirect(url_for('result'))

@app.route('/result')
def result():
    name = session.get('name')
    location = session.get('location')
    favorite_language = session.get('favorite_language')
    comments = session.get('comments')

    return render_template('result.html', name=name, location=location, favorite_language=favorite_language, comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
