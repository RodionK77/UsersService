import os

from flask import Flask, jsonify, request
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rodionkasirin:12345@postgres:5432/items_db'
#db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)

app = FastAPI()

@app.get('/')
def get_users():
    #users = User.query.all()
    #user_list = [{'id': user.id, 'name': user.name} for user in users]
    #return jsonify(user_list)
    return "Allow users: id-1:User1; id-2:User2; id-3:User3"

# @app.route('/add_user', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     new_user = User(name=data['name'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'id': new_user.id, 'name': new_user.name})

@app.get('/cancel_users')
def get_cancel_users():
    #users = User.query.all()
    #user_list = [{'id': user.id, 'name': user.name} for user in users]
    #return jsonify(user_list)
    return "Cancel users: id-4:User4; id-5:User5; id-6:User6"

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv('PORT', 80)))
