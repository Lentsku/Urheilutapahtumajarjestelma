from application import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(63), nullable=False)
    lastname = db.Column(db.String(63), nullable=False)
    lastFirst = db.Column(db.String(7), nullable=False)
    birthdate = db.Column(db.Date, index=True, nullable=False)
    email = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=False)
    postalCode = db.Column(db.String(63), nullable=False)
    postOffice = db.Column(db.String(144), nullable=False)
    country = db.Column(db.String(144), nullable=True)

    personSeries = db.relationship('PersonSeries', backref='Person', lazy=True)

    def __init__(self, firstname, lastname, lastFirst, birthdate, email, phone, address, postalCode, postOffice, country):
        self.firstname = firstname
        self.lastname = lastname
        self.lastFirst = lastFirst # Automatically generated from the last and first names
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.address = address
        self.postalCode = postalCode
        self.postOffice = postOffice
        self.country = country

    def get_id(self):
        return self.id