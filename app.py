from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

# host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Playlister')
# client = MongoClient(host=f'{host}?retryWrites=false')
client=MongoClient()
db = client.contractor
# db = client.get_default_database()
products = db.products
price = db.price
products.drop()
products.insert_one({'title': 'Pineapple', 'img': '/static/images/pineapple.jpg'})
products.insert_one({'title': 'Grape', 'img': '/static/images/grape.jpg'})
products.insert_one({'title': 'Pizza', 'img': '/static/images/pizza.jpg'})
products.insert_one({'title': 'Steak', 'img': '/static/images/steak.jpg'})


app = Flask(__name__)

@app.route('/')
def contractor_index():
    return render_template('contractor_index.html', products=products.find())

@app.route('/products/new')
def contractor_new():
    return render_template('contractor_new.html', products={}, title='New Item')

@app.route('/products', methods=['POST'])
def contractor_submit():
    product = {
        'title': request.form.get('title'),
        'price': request.form.get('price'),
        'picture': request.form.get('picture')
    }
    print(product)
    product_id = products.insert_one(product).inserted_id
    return redirect(url_for('products_show', product_id=product_id))

@app.route('/products/<product_id>')
def contractor_show(product_id):
    product = products.find_one({'_id': ObjectId(product_id)})
    # product_price = price.find({'product_id': ObjectId(product_id)})
    return render_template('flavors.html', product=product)

if __name__ == '__main__':
  app.run(debug=True)