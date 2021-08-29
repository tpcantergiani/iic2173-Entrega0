from datetime import datetime
from bancoin import db, login_manager
from flask_login import UserMixin
import enum

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}' )"

    @property
    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'last_name': self.last_name,
        'email': self.email,
        }
    

# class Guard(User):
#     __mapper_args__ = {
#         'polymorphic_identity': 'guard'
#     }

#     @property
#     def get_invitations(self):
#         return [invitation.serialize for invitation in self.home.condominum.invitations]
    
#     @property
#     def get_entries(self):
#         homes_id = [home.id for home in self.home.condominium.homes]
#         entries = Entry.query.filter(Entry.home_id.in_(homes_id)).all()
#         return [entry.sequelize for entry in entries]


# class Resident(User):
#     __mapper_args__ = {
#         'polymorphic_identity': 'resident'
#     }

#     @property
#     def get_invitations(self):
#         return [invitation.serialize for invitation in self.home.invitations]
    
#     @property
#     def get_entries(self):
#         return [entry.serialize for entry in self.home.entries]


# class Contact(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), nullable=False)
#     last_name = db.Column(db.String(20), nullable=False)
#     rut = db.Column(db.String(20), nullable=False)
#     patent = db.Column(db.String(8))
#     created_at = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     entries = db.relationship('Entry', backref='contact', lazy=True)
#     invitations = db.relationship('Invitation', backref='contact', cascade = "all,delete", lazy=True)
    

#     def __repr__(self):
#         return f"Contact('{self.name}', '{self.last_name}', '{self.rut}')"
    
#     @property
#     def serialize(self):
#         return {
#         'id': self.id,
#         'name': self.name,
#         'last_name': self.last_name,
#         'rut': self.rut,
#         'patent': self.patent,
#         'user': self.user.serialize
#         }
    
#     @property
#     def min_serialize(self):
#         return {
#         'id': self.id,
#         'name': self.name,
#         'last_name': self.last_name,
#         'rut': self.rut,
#         'patent': self.patent,
#         'user_id': self.user_id
#         }


# class Invitation(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     status = db.Column(db.Integer, default=1) # 1: todo ok, 0: bloqueado; supuesto: para que sea válida la entreda 1. status debe ser 1, 2. la hora actual debes estar en el rango de la invitacion
#     start_time = db.Column(db.DateTime, nullable=False)
#     end_time = db.Column(db.DateTime, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

#     condominium_id = db.Column(db.Integer, db.ForeignKey('condominium.id'), nullable=False)
#     home_id = db.Column(db.Integer, db.ForeignKey('home.id'), nullable=False)
#     contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)
    
#     def __repr__(self):
#         contact = Contact.query.filter_by(id=self.contact_id).first()
#         home_number = Home.query.filter_by(id=self.home_id).first()
#         return f"Invitation( '{contact.name}', Home #'{home_number.number}' from '{self.start_time}' to '{self.end_time}')"

#     @property
#     def serialize(self):
#         return {
#             "id": self.id,
#             "status": self.status,
#             "start_time": self.start_time,
#             "end_time": self.end_time,
#             "contact": self.contact.serialize,
#             "home": self.home.number
#         }


# class Home(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     number = db.Column(db.String(10), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

#     condominium_id = db.Column(db.Integer, db.ForeignKey('condominium.id'), nullable=False)
#     users = db.relationship('User', backref='home', lazy=True)
#     entries = db.relationship('Entry', backref='home', lazy=True)
#     patents = db.relationship('Patent', backref='home', lazy=True)
#     invitations = db.relationship('Invitation', backref='home', lazy=True)

#     @property
#     def serialize(self):
#        return {
#         'id': self.id,
#         'number': self.number,
#         'patents': [patent.serialize for patent in self.patents],
#         'users': [user.id for user in self.users]
#         }
    
#     def __repr__(self):
#         return f"Home( '{self.number}' )"
    
# class Patent(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     patent = db.Column(db.String(8), nullable=False, unique=True)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

#     home_id = db.Column(db.Integer, db.ForeignKey('home.id'), nullable=False)

#     def __repr__(self):
#         return f"Patent( '{self.patent}' )"
    
#     @property
#     def serialize(self):
#         return {
#             'id': self.id,
#             'patent': self.patent
#         }

# class Condominium(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

#     homes = db.relationship('Home', backref='condominium', lazy=True)
#     invitations = db.relationship('Invitation', backref='condominium', lazy=True)

#     def __repr__(self):
#         return f"Condominium( '{self.name}' )"


#     @property
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name
#         }
    
#     @property
#     def users(self):
#         users = []
#         for home in self.homes:
#             users.extend(home.users)
#         return users

# class EntryType(enum.Enum):
#     Unexpected = 0
#     Visit = 1
#     User = 2
#     Provider = 3

# class Entry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     entry_time = db.Column(db.DateTime, default=datetime.utcnow)
#     patent = db.Column(db.String(8))
#     entry_photo = db.Column(db.Text)
#     expected = db.Column(db.Enum(EntryType),default=EntryType.Unexpected)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)


#     home_id = db.Column(db.Integer, db.ForeignKey('home.id'), nullable=False)
#     contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))

#     def __repr__(self):
#         contact = Contact.query.filter_by(id=self.contact_id).first()
#         return f"Entry( '{contact.name}' at '{self.entry_time}' )"
    
#     @property
#     def serialize(self):
#         return {
#             "id": self.id,
#             "entry_time": self.entry_time,
#             "patent": self.patent,
#             "contact": None if not self.contact_id else self.contact.min_serialize,
#             "home": {'id': self.home_id, 'number': self.home.number},
#             "expected": self.expected.value
#         }

# class Access(db.Model):
#     id         = db.Column(db.Integer, primary_key=True)
#     entry_time = db.Column(db.DateTime, default=datetime.utcnow)
#     ip         = db.Column(db.String(20))
#     request    = db.Column(db.String(60))
#     result     = db.Column(db.Integer)
#     service    = db.Column(db.String(60))
#     method     = db.Column(db.String(20))

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

#     def __repr__(self):
#         user = User.query.filter_by(id=self.user_id).first()
#         if user:
#             return f"Acces( '{user.name} {user.last_name}' at '{self.entry_time}' from {self.ip} )"
#         else:
#             return f"Acces(At '{self.entry_time}' from {self.ip} )"
    
#     @property
#     def serialize(self):
#         return {
#             "id": self.id,
#             "entry_time": self.entry_time,
#             "ip": self.ip,
#             "result": self.result,
#             "request": self.request
#         }
