# -*- coding: utf-8 -*-
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
    id         = Column(INTEGER, primary_key=True,doc=u'序号')
    name       = Column(VARCHAR(128),unique=True,nullable=False,doc=u'名称')
    short_name = Column(VARCHAR(50),unique=True,nullable=False,doc=u'简称')
    address    = Column(VARCHAR(128),nullable=False,doc=u'地址')
    contact    = Column(VARCHAR(24),nullable=False,doc=u'联系人')
    telephone  = Column(VARCHAR(24),nullable=False,doc=u'电话')
    cellphone  = Column(VARCHAR(24),nullable=False,doc=u'手机')
    email      = Column(VARCHAR(50),doc=u'邮件')
    comment    = Column(VARCHAR(256),doc=u'备注')

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
    id         = Column(INTEGER, primary_key=True,doc=u'序号')
    name       = Column(VARCHAR(24),unique=True,nullable=False,doc=u'姓名')
    cellphone  = Column(VARCHAR(24),nullable=False,doc=u'手机')
    email      = Column(VARCHAR(50),doc=u'邮件')
    comment    = Column(VARCHAR(256),doc=u'备注')

    def __init__(self, name, email=None,cellphone=None, comment=None):
        self.name = name
        self.email=email
        self.cellphone = cellphone
        self.comment = comment

    def __repr__(self):
        return "<Employee('%s')>" % self.name

class Product(Base):
    __tablename__ = 'products'
    id         = Column(INTEGER, primary_key=True,doc=u'序号')
    sn         = Column(VARCHAR(36),unique=True,doc=u'编号')
    name_major = Column(VARCHAR(24),nullable=False,doc=u'主型号')
    name_minor = Column(VARCHAR(12),nullable=False,doc=u'辅型号')
    name_ext   = Column(VARCHAR(12),doc=u'扩展型号')
    price      = Column(NUMERIC(8,2),nullable=False,doc=u'价格')
    comment    = Column(VARCHAR(256),doc=u'备注')

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
    id         = Column(INTEGER, primary_key=True,doc=u'序号')
    sn         = Column(VARCHAR(24),unique=True,nullable=False,doc=u'单号')
    customer_id= Column(ForeignKey(Customer.__tablename__+'.id'),nullable=False,doc=u'客户')
    product_id = Column(ForeignKey(Product.__tablename__+'.id'),nullable=False,doc=u'产品')
    num        = Column(INTEGER,default=0,doc=u'数量')
    price      = Column(NUMERIC(8,2),default=0.0,doc=u'价格')
    amount     = Column(NUMERIC(12,2),default=0.0,doc=u'金额')
    employee_id= Column(ForeignKey(Employee.__tablename__+'.id'),doc=u'业务员')
    dlv_date   = Column(DATE,default=datetime.datetime.now().date(),doc=u'发货日期')
    comment    = Column(VARCHAR(256),doc=u'备注')
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
    id         = Column(INTEGER, primary_key=True,doc=u'序号')
    customer_id= Column(ForeignKey(Customer.__tablename__+'.id'),nullable=False,doc=u'客户')
    product_id = Column(ForeignKey(Product.__tablename__+'.id'),nullable=False,doc=u'产品')
    amount     = Column(NUMERIC(12,2),default=0.0,doc=u'金额')
    account    = Column(VARCHAR(64),nullable=False,doc=u'帐号')
    recvdate   = Column(DATE,default=datetime.datetime.now().date(),doc=u'收款日期')
    comment    = Column(VARCHAR(256),doc=u'备注')
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


