from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base
from pymongo import MongoClient

import csv
import os
Base=declarative_base()

class DataStorage(object):
    def __init__(self,CONNECTION,**kwargs):
        self.databaseType=kwargs.get('databaseType','CSV')
        if self.databaseType == 'SQL':
            self.field()
            tablename=kwargs.get('tablename',self.__class__.__name__)
            self.table=self.table(tablename)
            self.DBSession=self.connect(CONNECTION)
        elif self.databaseType == 'NoSQL':
            self.DBSession=self.connect(CONNECTION)
        else:
            self.path=CONNECTION
    def field(self):
        pass
    def connect(self,CONNECTION):
        if self.databaseType=='SQL':
            enhine=create_engine(CONNECTION)
            DBSession=sessionmaker(bind=enhine)()
            Base.metadata.create_all(enhine)
        else:
            info=CONNECTION.split('/')
            connection=MongoClient(info[0],int(info[1]))
            db=connection[info[2]]
            DBSession=db[info[3]]
        return DBSession

    def table(self,tablename):
        class TempTable(Base):
            __tablename__=tablename
            id=Column(Integer,primary_key=True)
        for k,v in self.__dict__.items():
            if isinstance(v,Column):
                setattr(TempTable,k,v)
        return  TempTable

    def insert(self,value):
        if self.databaseType=='SQL':
            self.DBSession.execute(self.table.__table__.insert(),value)
            self.DBSession.commit()
        elif self.databaseType == 'NoSQL':
            if isinstance(value,list):
                self.DBSession.insert_many(value)
            else:
                self.DBSession.insert(value)

    def update(self,value,condition={}):
        if self.databaseType=='SQL':
            if condition:
                c=self.table.__dict__[list(condition.keys())[0]].in_(list(condition.values()))
                self.DBSession.execute(self.table.__table__.update().where(c).values(),value)
            else:
                self.DBSession.execute(self.table.__table__.update().values(),value)
            self.DBSession.commit()
        elif self.databaseType == 'NoSQL':
            self.DBSession.update_many(condition,{'$set':value})

    def getfile(self,content,filepath):
        with open(filepath,'wb') as file:
            file.write(content)
    def write_csv(self,value,title=[]):
        if not title:
            title=sorted(value[0].keys())
        pathExists=os.path.exists(self.path)
        with open(self.path,'a',newline='') as csv_file:
            csv_writer=csv.writer(csv_file)
            if not pathExists:
                csv_writer.writerow(title)
            for v in value:
                value_list=[]
                for t in title:
                    value_list.append(v[t])
                csv_writer.writerow(value_list)

