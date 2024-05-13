"""SQL Alchemy models"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Employee(db.Model, UserMixin):
    """Model to represent an employee"""
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        """Getter for password"""
        return self.hashed_password

    @password.setter
    def password(self, password):
        """Setter for password"""
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        """Checks password against hashed version"""
        return check_password_hash(self.password, password)
