from flask import Flask
from flask import request
import random
import json
app = Flask(__name__)

@app.route('/add-data',methods=['POST'])
def add_data():
    contact = {
    'id' : random.randint(1,1000000000),
    'Name' : request.form['Name'],
    'Contact' : request.form['Contact']
    }
    with open('contacts.json') as contacts:
        data = json.load(contacts)
    data['contacts'].append(contact)
    with open('contacts.json','w') as contacts:
        json.dump(data,contacts,indent=4)
    return 'Contact added'

if(__name__=='__main__'):
    app.run(debug=True,port=5000)