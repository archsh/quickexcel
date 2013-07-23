from quixcel.models.base import get_db_session, setup_db_session, initialize_db
from quixcel.models.base import Customer, Product, Employee, Delivery, Receipt

setup_db_session("sqlite:///test.db")

initialize_db()

session = get_db_session()

c1 = Customer(name="DINGRONG Technologies",short_name="dingrong",address="Shenzhen",contact="SMC")
c2 = Customer(name="PUFANGDA Technologies",short_name="pufangda",address="Shenzhen",contact="HEJIAO")
e1 = Employee(name="Fangze",cellphone="13800138001")
e2 = Employee(name="Fangyi",cellphone="13800138002")
p1 = Product(sn='P001',name_major='P1',name_minor='T',name_ext='16GB',price=105.00)
p2 = Product(sn='P002',name_major='P1',name_minor='W',name_ext='8GB',price=95.00)

