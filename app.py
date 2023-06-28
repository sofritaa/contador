from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] += 1
    return render_template('index.html', visits=session['visits'], counter=session.get('counter', 0))


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('home'))


@app.route('/increment', methods=['POST'])
def increment():
    increment_value = request.form.get('increment', 1, type=int)
    session['counter'] = session.get('counter', 0) + increment_value
    return redirect(url_for('home'))


@app.route('/reset')
def reset():
    session.pop('counter', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
