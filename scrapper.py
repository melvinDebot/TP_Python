# Required Imports
import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import unittest
from unittest.mock import Mock


# Initialize Flask App
app = Flask(__name__)
# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

r = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(r.content)


li_title = []
for div in soup.find_all({'li'}, {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}, 'div'):
    img = div.find('img', alt=True)
    li_title.append(img['alt'])
len(li_title)

li_price = []
price_brut = soup.findAll("p", {'class': 'price_color'})
price = [x.string for x in price_brut]
for i in price:
    i = i[1:]
    li_price.append(i)
len(li_price)

stocks_brut = soup.findAll("p", {'class': "instock availability"})
stocks = [stock.text for stock in stocks_brut]
for i in stocks:
    li_stock = [i.strip('\n ') for i in stocks]
len(li_stock)

li_notes = []
for x in soup.find_all({'li'}, {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}, 'div'):
    y = x.find('p', {'class': 'star-rating'}).attrs['class']
    li_notes.append(y[1])
len(li_notes)

di = {"title": li_title, "price": li_price, "note": li_notes, "stock": li_stock}

df = pd.DataFrame(di)
print('')
print('------------ DATA SCRPPER -------------')
print(df)

#print(di)
for i in range(1, len(di)+1):
    db.collection('todos').add(df.to_dict('records')[i])


@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'note': 'six', 'price': '42.80', 'stock': 'inStock, 'title': 'melvin'}
    """
    try:
        id = request.json['note']
        todo_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON
        todo : Return document that matches query ID
        all_todos : Return all documents
    """
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('note')
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/update', methods=['POST', 'PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'note': 'six', 'price': '42.80', 'stock': 'inStock, 'title': 'maxime'}
    """
    try:
        id = request.json['note']
        todo_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection
    """
    try:
        # Check for ID in URL query
        todo_id = request.args.get('note')
        todo_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


print('')
print('------------ TEST UNITAIRE SCRAPPE -------------')

class Test_Scrappe(unittest.TestCase):
    def setUp(self):
        self.fake_data_scrappe = {'title': 'melvin', 'statut': True}

    
    def get_call_api(self):
        create()
        self.assertTrue(self.fake_data_scrappe['statut'], True)

print('')
print('------------ API -------------')
port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)












