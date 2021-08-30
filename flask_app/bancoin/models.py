from datetime import datetime
from bancoin import db, login_manager
from flask_login import UserMixin
import enum

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

    transactions = db.relationship('Transaction', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}' )"

    @property
    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'email': self.email,
        'created_at': self.created_at
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

    transactions = db.relationship('Transaction', backref='product', lazy=True)

    def __repr__(self):
        return f"{self.name}: {self.quantity})"
    
    @property
    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'created_at': self.created_at
        }

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Float, nullable=False)
    intention = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return f"{self.product}: {self.quantity})"
    
    @property
    def serialize(self):
        return {
        'id': self.id,
        'product': self.product_id,
        'user': self.user_id,
        'quantity': self.quantity,
        'created_at': self.created_at
        }