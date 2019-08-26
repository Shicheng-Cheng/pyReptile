from pyReptile.storage import *
if __name__=='__main__':
    CONNECTION='localhost/27017/test/storage_db'
    person_info=[{'name':'Lucy','age':'21','address':'北京市'},
                 {'name':'Lily','age':'23','address':'上海市'}]


    database=DataStorage(CONNECTION,databaseType='NoSQL')
    database.insert(person_info)
    value={'name':'Bob','age':'13','address':'南京市'}
    database.insert(value)
    condition={'name':'Lucy'}
    value1={'name':'Lucy','age':'25','address':'重庆市'}
    database.update(value1,condition)
