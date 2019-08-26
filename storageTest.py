from pyReptile.storage import *
if __name__=='__main__':
    CONNECTION='data.csv'
    person_info=[{'name':'Lucy','age':'21','address':'北京市'},
                 {'name':'Lily','age':'23','address':'上海市'}]


    database=DataStorage(CONNECTION)
    database.write_csv(person_info,title=person_info[0].keys())