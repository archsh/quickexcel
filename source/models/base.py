### Base Class of Model

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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
    cellphone  = Column(String(24))
    email      = Column(String(50))
    comment    = Column(String(256))

    def __init__(self, name, email=None,cellphone=None, comment=None):
        self.name = name
        self.email=email
        self.cellphone = cellphone
        self.comment = comment

    def __repr__(self):
        return "<Employee('%s')>" % self.name

class Product(Base):
    __tablename__ = 'products'
    id         = Column(Integer, primary_key=True, sqlite_autoincrement=True)
    sn         = Column(String(128))
    name_major = Column(String(50))
    name_minor = Column(String(128))
    name_ext   = Column(String(24))
    price      = Column(String(24))
    comment    = Column(String(256))

    def __init__(self, sn, name_major, name_minor=None, name_ext=None,
                 price=None, comment=None):
        self.sn = sn
        self.name_major = name_major
        self.name_minor = name_minor
        self.name_ext = name_ext
        self.price=price
        self.comment = comment

    def __repr__(self):
        return "<Product('%s')>" % self.name


class Delivery(Base):
    __tablename__ = 'deliveries'
    id         = Column(Integer, primary_key=True, sqlite_autoincrement=True)
    sn         = Column(String(128))
    customer   = Column(String(50))
    model      = Column(String(50))
    num        = Column(String(128))
    price      = Column(String(24))
    amount     = Column(String(24))
    employee   = Column(String(24))
    dlv_date   = Column(String(50))
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

DB_ENGINE  = None
DB_SESSION = None

def setup_db_session(dbpath):
    global DB_ENGINE,DB_SESSION
    DB_ENGINE  = create_engine(dbpath, echo=True)
    DB_SESSION = sessionmaker(bind=DB_ENGINE)

def get_db_session():
    global DB_SESSION
    if not DB_SESSION:
        raise Exception('Invalid DB Session!')
    else:
        return DB_SESSION

def db_validate():
    pass


def initialize_db():
    Base.metadata.create_all(get_db_session())





