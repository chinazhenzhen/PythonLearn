#!/usr/bin/python3
#encoding: utf-8



'''
pymysql用法总结
导入pymysql的包
 cur = db.cursor()
 生成游标
 cur.execute(sql)执行sql
 插入删除和修改数据库数据时要提交数据库操作
 db.commit()
 失败时候要回滚
 db.rollback()

'''

import pymysql


def connectdb():
    print('connecting...')

    db = pymysql.connect(host='localhost',user='root',passwd='123456',db='blog',port = 3306)
    print('connect yes')

    return db

def createtable(db): #创建数据库中的表


    #利用 cursor获取游标，进行数据库的操作
    cur = db.cursor()

    cur.execute("DROP TABLE IF EXISTS student")  #如果存在student表则事先删除掉
    sql = """
            CREATE TABLE student(
            id CHAR(11) NOT NULL,
            name char(8),
            grade INT
            )
            """
    cur.execute(sql)

def insertdb(db):  #插入信息
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO student(id,name,grade)
         VALUES ('001', 'CZQ', 70),
                ('002', 'LHQ', 80),
                ('003', 'MQ', 90),
                ('004', 'WH', 80),
                ('005', 'HP', 70),
                ('006', 'YF', 66),
                ('007', 'TEST', 100)
                """
    try:
        # 执行sql语句
        cur.execute(sql)
        # 提交到数据库执行
        print("successful")
        db.commit()
    except:
        # Rollback in case there is any error
        print ("faild")
        db.rollback()
        #修改更新失败，数据库回滚，回滚到失败之前


def querydb(db): # 查询语句
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # SQL 查询语句
    #sql = "SELECT * FROM student \
    #    WHERE Grade > '%d'" % (80)
    sql = "SELECT * FROM student"
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            grade = row[2]
            # 打印结果
            print ("ID: %s, Name: %s, Grade: %d" %(id, name, grade))
    except:
        print ("failed")


def deletedb(db):#删除语句
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # SQL 删除语句
    sql = "DELETE FROM student WHERE grade = '%d'" % (100)

    try:
       # 执行SQL语句
       cur.execute(sql)
       # 提交修改
       db.commit()
    except:
        print ('failed')
        # 发生错误时回滚
        db.rollback()



def updatedb(db):# 更新
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # SQL 更新语句
    sql = "UPDATE student SET grade = grade + 3 WHERE id= '%s'" % ('003')

    try:
        # 执行SQL语句
        cur.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print ('failed')
        # 发生错误时回滚
        db.rollback()


def closedb(db):  #关闭数据库
    db.close()

def main():
    db = connectdb()    # 连接MySQL数据库

    createtable(db)     # 创建表
    insertdb(db)        # 插入数据
    querydb(db)
    deletedb(db)        # 删除数据'
    querydb(db)
    updatedb(db)        # 更新数据
    querydb(db)

    closedb(db)         # 关闭数据库

if __name__ == '__main__':
    main()