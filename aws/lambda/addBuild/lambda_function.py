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


def addBuilding(name, addr, lat, longi, desc, img, man, hour):
    sql_cmd = ("INSERT INTO Buildings(idBuildings, name, address, latitude, longitude, description, imageFolder, manager, hours) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (str(uuid.uuid4()), name, addr, lat, longi, desc, img, man, hour)
    cursor.execute(sql_cmd, data)
    print(cursor.statement)
    mydb.commit()
