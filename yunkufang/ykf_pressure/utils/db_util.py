'''
version: V2.0
Author: 学海无涯任我游
Date: 2020-12-02 11:22:35
LastEditors: 学海无涯任我游
LastEditTime: 2020-12-11 11:04:05
'''
import sys, pymysql, datetime,json
from warnings import filterwarnings

filterwarnings("ignore",category=pymysql.Warning)

class MysqlDb:
    def __init__(self):
        #建立数据库连接
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='ren123456',db='testcase',charset='utf8')
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    def __del__(self):
        #关闭游标
        self.cur.close()
        #关闭连接
        self.conn.close()

    def query(self, sql, state="all"):
        """
        查询
        """
        self.cur.execute(sql)
        # data = {}
        if state == "all":
            data = self.cur.fetchall()
        else:
            data = self.cur.fetchone()
        return data


    def execute(self, sql):
        """
        更新、修改、删除
        """
        try:
            # print("sql=======",sql)
            #使用execute操作sql
            rows = self.cur.execute(sql)
            #提交事务
            self.conn.commit()
            return True
        except Exception as e:
            print("数据库操作异常:{}".format(e))
            #事务回滚修改
            self.conn.rollback() 
        

if __name__ == "__main__":
    # r = MysqlDb().query("select * from `case`"
    sql = "INSERT INTO `case` (app,module,run) VALUES('youtime','user','yes');"
    r = MysqlDb().execute(sql) 
    print(r)
 
        

