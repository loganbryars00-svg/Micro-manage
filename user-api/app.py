# This code creates web server using Flask framework, defines user data structure, and creates API endpoints for managing users.
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#Initialize Flask app
app = Flask(__name__)

# Configure database connnection from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/userdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define User model
# Represents users table in the database with id, name, and email fields
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        """Convert User object to dictionary"""
        return {'id': self.id, 'name': self.name, 'email': self.email}
    
# Create database tables prior to the first request
with app.app_context():
    db.create_all()

# API endpoint to create a new user by inputting name and email JSON data
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'message': 'User created successfully',
        'user': new_user.to_dict()
     }), 201, 

# API endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({
        'message': "All users retrieved successfully",
        'users': [user.to_dict() for user in users]
    }), 200

# API endpoint to get a user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({
        'message': 'User retrieved successfully',
        'user': user.to_dict()
    }), 200

# API endpoint to update a user by ID
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({
        'message': 'User updated successfully',
        'user': user.to_dict()
    }), 200

# API endpoint to delete a user by ID
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({
        'message': 'User deleted successfully'
    }), 200

# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    # Host='0.0.0.0' to make the server externally visible
    app.run(host='0.0.0.0', port=5000, debug=True)