from pyReptile.storage import *
class Person(DataStorage):
    def field(self):
        self.name=Column(String(50),comment='姓名')
        self.age=Column(String(50),comment='年龄')
        self.address = Column(String(50), comment='地址')

class School(DataStorage):
    def field(self):
        self.school=Column(String(50),comment='学校')
        self.name=Column(String(50),comment='姓名')

if __name__=='__main__':
    CONNECTION='mysql+pymysql://root:admin@localhost/nea?charset=utf8mb4'
    person=Person(CONNECTION,databaseType='SQL')
    school=School(CONNECTION,databaseType='SQL')
    person_info = [{'name': 'Lucy', 'age': '21', 'address': '北京市'},
                   {'name': 'Lily', 'age': '23', 'address': '上海市'}]
    person.insert(person_info)
    # value = {'name': 'Bob', 'age': '13', 'address': '南京市'}
    # person.insert(value)
    # condition = {'name': 'Lucy'}
    # value1 = {'name': 'Lucy', 'age': '25', 'address': '重庆市'}
    # person.update(value1, condition)

