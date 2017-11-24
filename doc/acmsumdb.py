#encoding: utf-8
import pymysql

class ACMREdb:

    def __init__(self,sql=""):
        self.db = pymysql.connect(host='localhost',user='root',passwd='123456',db='acmre',charset = 'utf8',port = 3306)
        self.cur = self.db.cursor()


    def creatdb(self): # 这里的creatdb语句执行一次即可
        #self.cur.execute("DROP TABLE IF EXISTS acmsolvesum")  # 如果存在student表则事先删除掉

        sql = """
                    CREATE TABLE acmsolvesum(
                    id CHAR(20) NOT NULL PRIMARY KEY,
                    name CHAR(20),
                    dlnuojname CHAR(20),
                    dlnuojsum INT,
                    hduojname CHAR(20),
                    hduojsum INT,
                    vojname CHAR(20),
                    vojsum INT, 
                    codeforcename CHAR(20),
                    codeforcerank INT
                    )
                    """
        self.cur.execute(sql)

    def insertdb(self,dict):
        sql="""
        INSERT INTO acmsolvesum(id,name,dlnuojname,dlnuojsum,hduojname,hduojsum,vojname,vojsum,codeforcename,codeforcerank)
         VALUES('%s','%s','%s','%d','%s','%d','%s','%d','%s','%d')  
        """%(dict['id'],dict['name'],dict['dlnuojname'],0,dict['hduojname'],0,dict['vojname'],0,dict['codeforcename'],0)
        try:
            self.cur.execute(sql)
            self.db.commit()
            print("successful")
        except:
            self.db.rollback()

    def deletedb(self,ID):  # 删除语句

        sql = "DELETE FROM acmsolvesum WHERE id = '%d'" % (ID)

        try:
            self.cur.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def updatedb(self,ojname,solvesum,id):  # 更新
        sql = "UPDATE acmsolvesum SET  %s = '%d'  WHERE id = '%s'" % (ojname,solvesum,id)

        try:
            self.cur.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def querydbAll(self):
        sql=""" SELECT * FROM acmsolvesum """
        self.cur.execute(sql)

        results = self.cur.fetchall()

        return results

    def __del__(self):
        self.db.close()



a = ACMREdb()
a.creatdb();





