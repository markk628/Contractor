from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def contractor_index():
    return render_template('contractor_index.html', )

@app.route('/cart')
def contractor_new():
    return render_template('contractor_new.html', title='Your Cart')