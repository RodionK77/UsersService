from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rodionkasirin:12345@postgres:5432/items_db'
#db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)

@app.route('/users', methods=['GET'])
def get_users():
    #users = User.query.all()
    #user_list = [{'id': user.id, 'name': user.name} for user in users]
    #return jsonify(user_list)
    return jsonify("Allow users: id-1:User1; id-2:User2; id-3:User3")

# @app.route('/add_user', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     new_user = User(name=data['name'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'id': new_user.id, 'name': new_user.name})

@app.route('/cancel_users', methods=['GET'])
def get_cancel_users():
    #users = User.query.all()
    #user_list = [{'id': user.id, 'name': user.name} for user in users]
    #return jsonify(user_list)
    return jsonify("Cancel users: id-4:User4; id-5:User5; id-6:User6")

if __name__ == '__main__':
    #with app.app_context():
        #db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5016)
