import MySQLdb
 
conn = MySQLdb.connect(
            host='localhost',
            user='ikiru_user',
            passwd='password',
            port=3306,
            db='ikiru_dev_db',
            charset='utf8')
pen = conn.cursor()
pen.execute("DROP DATABASE IF EXISTS ikiru_dev_db")
pen.execute("CREATE DATABASE IF NOT EXISTS ikiru_dev_db")
conn = MySQLdb.connect(
            host='localhost',
            user='ikiru_user',
            passwd='password',
            port=3306,
            db='ikiru_dev_db',
            charset='utf8')
pen = conn.cursor()