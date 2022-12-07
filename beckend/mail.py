import pymysql

def connectDatabase():
    DB_SETTING = {
        'host': '140.124.44.25', 
        'port': 3306, 
        'user': 'cvgiproot', 
        'password': 'cvgip2021', 
        'db': 'CVGIP', 
        'charset': 'utf8'
    }
    return pymysql.connect(**DB_SETTING)

connect = connectDatabase()
with connect.cursor() as cursor:
    SQLCommand = 'SELECT Mail \
                  FROM PARTICIPANT \
                  WHERE (ID<2000 AND ID<>47 AND ID<>100)'
    cursor.execute(SQLCommand)
    result = cursor.fetchall()
result = list(set(result))
print(len(result))


for r in result:
    print(r[0], end=' ')
