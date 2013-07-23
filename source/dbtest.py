from quixcel.models.base import get_db_session, setup_db_session, initialize_db
from quixcel.models.base import Customer, Product, Employee, Delivery, Receipt

setup_db_session("sqlite:///test.db")

initialize_db()

session = get_db_session()
if False:
    c1 = Customer(name="DINGRONG Technologies",short_name="dingrong",address="Shenzhen",contact="SMC",telephone='',cellphone='')
    c2 = Customer(name="PUFANGDA Technologies",short_name="pufangda",address="Shenzhen",contact="HEJIAO",telephone='',cellphone='')
    e1 = Employee(name="Fangze",cellphone="13800138001")
    e2 = Employee(name="Fangyi",cellphone="13800138002")
    p1 = Product(sn='P001',name_major='P1',name_minor='T',name_ext='16GB',price=105.00)
    p2 = Product(sn='P002',name_major='P1',name_minor='W',name_ext='8GB',price=95.00)
    
    session.add(c1)
    session.add(c2)
    session.add(e1)
    session.add(e2)
    session.add(p1)
    session.add(p2)
    session.commit()

if False:
    res = session.query(Customer).all()
    for c in res:
        print c.id, c.name
        
    res = session.query(Employee).all()
    for c in res:
        print c.id, c.name
    
    res = session.query(Product).all()
    for c in res:
        print c.id, c.name_major, c.price
    
if False:
    c1 = session.query(Customer).all()[0]
    c2 = session.query(Customer).all()[1]
    e1 = session.query(Employee).all()[0]
    e2 = session.query(Employee).all()[1]
    p1 = session.query(Product).all()[0]
    p2 = session.query(Product).all()[1]
    
    deliverys = [
            Delivery('D030713001',c1,p1,100,employee=e1),
            Delivery('D030713002',c1,p2,1000,employee=e1),
            Delivery('D030713003',c2,p1,10100,employee=e2),
            Delivery('D030713004',c2,p2,500,employee=e2),
        ]
    session.add_all(deliverys)
    session.commit()
    
if True:
    c1 = session.query(Customer).all()[0]
    c2 = session.query(Customer).all()[1]
    e1 = session.query(Employee).all()[0]
    e2 = session.query(Employee).all()[1]
    p1 = session.query(Product).all()[0]
    p2 = session.query(Product).all()[1]
    for d in session.query(Delivery).filter(Delivery.customer==c1,Delivery.product==p1):
        print d
    

