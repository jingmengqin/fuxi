"""
数据库处理操作
"""

import pymysql

class User:
    def __init__(self, host='localhost',
                 port = 3306,
                 user = 'root',
                 passwd = '123456',
                 charset='utf8',
                 database=None):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.database = database
        self.connect_db()

    # 链接数据库
    def connect_db(self):
        self.db = pymysql.connect(host = self.host,
                                  port = self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset)

    # 创建游标对象
    def create_cursor(self):
        self.cur = self.db.cursor()

    #增加
    def push(self,modle,number1,VIN,engine,check1,run1,order1,company,address,name1,telephone1):
        sql = "insert into 武装客车装备发运统计3(modle,number1,VIN,engine,check1,run1,order1,company,address,name1,telephone1)" \
              " values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(modle,number1,VIN,engine,
                                                                                      check1,run1,order1,company,
                                                                                       address,name1,telephone1)
        print(sql)
        try:
            self.cur.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False


    #修改
    def change(self,company,id):
        sql = "update 武装客车装备发运统计3 set company='%s' where id=%s"%(company,id)
        print(sql)
        try:
            self.cur.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False




    #查找
    def chat(self,i):
        sql = "select * from 武装客车装备发运统计3 where id"+i
        print(sql)
        self.cur.execute(sql)
        r = self.cur.fetchall()
        if r:
            return r

    #删除
    def delete(self,id):
        sql = "delete from 武装客车装备发运统计3 where id='%s'"%id
        self.cur.execute(sql)
        self.db.commit()



