### Base Class of Model

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey

class Customer(Base):
    __tablename__ = 'customers'
    id         = Column(Integer, primary_key=True, sqlite_autoincrement=True)
    name       = Column(String(128))
    short_name = Column(String(50))
    address    = Column(String(128))
    contact    = Column(String(24))
    telephone  = Column(String(24))
    cellphone  = Column(String(24))
    email      = Column(String(50))
    comment    = Column(String(256))

    def __init__(self, name, short_name, address=None, email=None,
                 contact=None,telephone=None,cellphone=None, comment=None):
        self.name = name
        self.short_name = short_name
        self.contact = contact
        self.address = address
        self.email=email
        self.telephone = telephone
        self.cellphone = cellphone
        self.comment = comment

    def __repr__(self):
        return "<Customer('%s')>" % self.name
    
class Employee(Base):
    __tablename__ = 'employees'
    id         = Column(Integer, primary_key=True, sqlite_autoincrement=True)
    name       = Column(String(128))
    short_name = Column(String(50))
    address    = Column(String(128))
    contact    = Column(String(24))
    telephone  = Column(String(24))
    cellphone  = Column(String(24))
    email      = Column(String(50))
    comment    = Column(String(256))

    def __init__(self, name, short_name, address=None, email=None,
                 contact=None,telephone=None,cellphone=None, comment=None):
        self.name = name
        self.short_name = short_name
        self.contact = contact
        self.address = address
        self.email=email
        self.telephone = telephone
        self.cellphone = cellphone
        self.comment = comment

    def __repr__(self):
        return "<Employee('%s')>" % self.name

class Product(Base):
    __tablename__ = 'products'
    id         = Column(Integer, primary_key=True, sqlite_autoincrement=True)
    name       = Column(String(128))
    short_name = Column(String(50))
    address    = Column(String(128))
    contact    = Column(String(24))
    telephone  = Column(String(24))
    cellphone  = Column(String(24))
    email      = Column(String(50))
    comment    = Column(String(256))

    def __init__(self, name, short_name, address=None, email=None,
                 contact=None,telephone=None,cellphone=None, comment=None):
        self.name = name
        self.short_name = short_name
        self.contact = contact
        self.address = address
        self.email=email
        self.telephone = telephone
        self.cellphone = cellphone
        self.comment = comment

    def __repr__(self):
        return "<Product('%s')>" % self.name


class Delivery(Base):
    __tablename__ = 'deliveries'
    id         = Column(Integer, primary_key=True, sqlite_autoincrement=True)
    name       = Column(String(128))
    short_name = Column(String(50))
    address    = Column(String(128))
    contact    = Column(String(24))
    telephone  = Column(String(24))
    cellphone  = Column(String(24))
    email      = Column(String(50))
    comment    = Column(String(256))

    def __init__(self, name, short_name, address=None, email=None,
                 contact=None,telephone=None,cellphone=None, comment=None):
        self.name = name
        self.short_name = short_name
        self.contact = contact
        self.address = address
        self.email=email
        self.telephone = telephone
        self.cellphone = cellphone
        self.comment = comment

    def __repr__(self):
        return "<Delivery('%s')>" % self.name

class Receipt(Base):
    __tablename__ = 'receipts'
    id         = Column(Integer, primary_key=True, sqlite_autoincrement=True)
    name       = Column(String(128))
    short_name = Column(String(50))
    address    = Column(String(128))
    contact    = Column(String(24))
    telephone  = Column(String(24))
    cellphone  = Column(String(24))
    email      = Column(String(50))
    comment    = Column(String(256))

    def __init__(self, name, short_name, address=None, email=None,
                 contact=None,telephone=None,cellphone=None, comment=None):
        self.name = name
        self.short_name = short_name
        self.contact = contact
        self.address = address
        self.email=email
        self.telephone = telephone
        self.cellphone = cellphone
        self.comment = comment

    def __repr__(self):
        return "<Receipt('%s')>" % self.name

