import mysql.connector
import json
import uuid

# connect to db
mydb = mysql.connector.connect(
  host="makermap.cbeezzrvvyp6.us-east-2.rds.amazonaws.com",
  user="admin",
  passwd="makermap",
  database="innodb"
)

cursor = mydb.cursor()


def addTool(name, idL, desc, img, book, own, res):
    sql_cmd = ("INSERT INTO Tools(idTools, name, labID, description, imageFolder, bookingLink, ownerID, restrictPublic) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    data = (str(uuid.uuid4()), name, idL, desc, img, book, own, res)
    cursor.execute(sql_cmd, data)
    mydb.commit()