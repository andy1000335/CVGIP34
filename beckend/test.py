# import pymysql
# import datetime

# # def connectDatabase():
# #     DB_SETTING = {
# #         'host': '140.124.44.25', 
# #         'port': 3306, 
# #         'user': 'cvgiproot', 
# #         'password': 'cvgip2021', 
# #         'db': 'CVGIP', 
# #         'charset': 'utf8'
# #     }
# #     return pymysql.connect(**DB_SETTING)

# # connect = connectDatabase()
# # with connect.cursor() as cursor:
# #     SQLCommand = 'INSERT RECEIPT VALUE (%s, %s, %s, %s, %s, %s)'
# #     cursor.execute(SQLCommand, (546, 'test_file5', '11111', datetime.date.today(), '', False))
# #     connect.commit()
# joinTime = datetime.datetime.strptime('2021/6/20 AM 8:24:36', '%Y/%m/%d %p %I:%M:%S')

# print(joinTime.date()<datetime.date(2021, 7, 31))

i = 1e10
i = str(i)
print(i)
i = int(i)
print(i)