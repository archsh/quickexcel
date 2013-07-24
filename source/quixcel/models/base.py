### Base Class of Model
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, \
            BLOB, BOOLEAN, CHAR, DATE, DATETIME, DECIMAL, FLOAT, \
            INTEGER, NUMERIC, SMALLINT, TEXT, TIME, TIMESTAMP, \
            VARCHAR, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id         = Column(INTEGER, primary_key=True)
    name       = Column(VARCHAR(128),unique=True,nullable=False)
    short_name = Column(VARCHAR(50),unique=True,nullable=False)
    address    = Column(VARCHAR(128),nullable=False)
    contact    = Column(VARCHAR(24),nullable=False)
    telephone  = Column(VARCHAR(24),nullable=False)
    cellphone  = Column(VARCHAR(24),nullable=False)
    email      = Column(VARCHAR(50))
    comment    = Column(VARCHAR(256))

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
    id         = Column(INTEGER, primary_key=True)
    name       = Column(VARCHAR(24),unique=True,nullable=False)
    cellphone  = Column(VARCHAR(24),nullable=False)
    email      = Column(VARCHAR(50))
    comment    = Column(VARCHAR(256))

    def __init__(self, name, email=None,cellphone=None, comment=None):
        self.name = name
        self.email=email
        self.cellphone = cellphone
        self.comment = comment

    def __repr__(self):
        return "<Employee('%s')>" % self.name

class Product(Base):
    __tablename__ = 'products'
    id         = Column(INTEGER, primary_key=True)
    sn         = Column(VARCHAR(36),unique=True)
    name_major = Column(VARCHAR(24),nullable=False)
    name_minor = Column(VARCHAR(12),nullable=False)
    name_ext   = Column(VARCHAR(12))
    price      = Column(NUMERIC(8,2),nullable=False)
    comment    = Column(VARCHAR(256))

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
    id         = Column(INTEGER, primary_key=True)
    sn         = Column(VARCHAR(24),unique=True,nullable=False)
    customer_id= Column(ForeignKey(Customer.__tablename__+'.id'),nullable=False)
    product_id = Column(ForeignKey(Product.__tablename__+'.id'),nullable=False)
    num        = Column(INTEGER,default=0)
    price      = Column(NUMERIC(8,2),default=0.0)
    amount     = Column(NUMERIC(12,2),default=0.0)
    employee_id= Column(ForeignKey(Employee.__tablename__+'.id'))
    dlv_date   = Column(DATE,default=datetime.datetime.now().date())
    comment    = Column(VARCHAR(256))
    customer = relationship("Customer", backref=backref("deliveries", order_by=id))
    product  = relationship("Product", backref=backref("deliveries", order_by=id))
    employee = relationship("Employee", backref=backref("deliveries", order_by=id))

    def __init__(self, sn, customer, product,num,price=None,amount=None,employee=None,dlv_date=None, comment=None):
        self.sn = sn
        self.customer = customer
        self.product = product
        self.num = num
        self.price=product.price if not price else price
        self.amount = self.price*self.num if not amount else amount
        self.employee = employee
        self.dlv_date = dlv_date
        self.comment = comment

    def __repr__(self):
        return "<Delivery('%s')>" % self.sn

class Receipt(Base):
    __tablename__ = 'receipts'
    id         = Column(INTEGER, primary_key=True)
    customer_id= Column(ForeignKey(Customer.__tablename__+'.id'),nullable=False)
    product_id = Column(ForeignKey(Product.__tablename__+'.id'),nullable=False)
    amount     = Column(NUMERIC(12,2),default=0.0)
    account    = Column(VARCHAR(64),nullable=False)
    recvdate   = Column(DATE,default=datetime.datetime.now().date())
    comment    = Column(VARCHAR(256))
    customer = relationship("Customer", backref=backref("receiptions", order_by=id))
    product  = relationship("Product", backref=backref("receiptions", order_by=id))

    def __init__(self, customer,product,amount,account,recvdate=None,comment=None):
        self.customer = customer
        self.product = product
        self.amount = amount
        self.account = account
        self.recvdate=recvdate
        self.comment = comment

    def __repr__(self):
        return "<Receipt('%s')>" % self.id

DB_ENGINE  = None
DB_SESSION = None

def setup_db_session(dbpath):
    global DB_ENGINE,DB_SESSION
    DB_ENGINE  = create_engine(dbpath, echo=False)
    Session = sessionmaker(bind=DB_ENGINE)
    DB_SESSION = Session()

def get_db_session():
    global DB_SESSION
    if not DB_SESSION:
        raise Exception('Invalid DB Session!')
    else:
        return DB_SESSION

def get_db_engine():
    global DB_ENGINE
    if not DB_ENGINE:
        raise Exception('Invalid DB Engine!')
    else:
        return DB_ENGINE

def db_validate():
    pass


def initialize_db():
    Base.metadata.create_all(get_db_engine())


