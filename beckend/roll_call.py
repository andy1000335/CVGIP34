import pymysql
import pandas as pd

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
    SQLCommand = 'SELECT ID, CH_Name, EN_Name, JobTitle, Address, Phone FROM PARTICIPANT'
    cursor.execute(SQLCommand)
    result = cursor.fetchall()

df = pd.DataFrame(result)
df.columns = ['ID', '中文姓名', '英文姓名', '職稱', '地址', '電話']
df.to_excel('名單.xlsx', index=False)