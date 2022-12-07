import pygsheets
import pymysql
import datetime

registration = 'https://docs.google.com/spreadsheets/d/11Ff0tZF7bCOiKWvfmgh3fRd9tStFIaztfvmrpz4w1xI/edit?usp=sharing'

gc = pygsheets.authorize(service_account_file='operating-bird-319611-b9cee5c4fb45.json')
sheet = gc.open_by_url(registration)
datas = sheet[0].get_as_df(start='A1', index_colum=0, empty_value='', include_tailing_empty=False, numerize=False)

dataNum = datas.shape[0]
propNum = datas.shape[1]

def checkNull(property):
    if property == '':
        return None
    else:
        return property

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
    for i in range(dataNum):
        data = datas.iloc[i]
        joinTime = data[0].replace('下午', 'PM').replace('上午', 'AM')
        joinTime = datetime.datetime.strptime(joinTime, '%Y/%m/%d %p %I:%M:%S')
        
        if joinTime.date() < datetime.date(2021, 7, 31):
            if data[9] == '學生':
                identity = 'Student'
                price = 2500
            else:
                identity = 'Teacher'
                price = 3700
        elif joinTime.date() < datetime.date(2021, 8, 13):
            if data[9] == '學生':
                identity = 'Student'
                price = 3000
            else:
                identity = 'Teacher'
                price = 4200
        else:
            if data[9] == '學生':
                identity = 'Student'
                price = 3500
            else:
                identity = 'Teacher'
                price = 4700
        if data[11] != '':
            price -= 1000

        try:
            SQLCommand = 'INSERT PARTICIPANT VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(SQLCommand, (8001+i, data[1], data[2], data[3], data[5], data[6], data[7], \
                                        checkNull(data[8]), checkNull(data[11]), price, joinTime, data[4], identity))
            connect.commit()
        except pymysql.err.IntegrityError:
            pass


receipt = 'https://docs.google.com/spreadsheets/d/1aEEzlAJ4n-Z3BZBZ47-CEDnDz5224XoiagpkZE4OqXo/edit#gid=986872402'

sheet = gc.open_by_url(receipt)
datas = sheet[0].get_as_df(start='A1', index_colum=0, empty_value='', include_tailing_empty=False, numerize=False)

dataNum = datas.shape[0]
propNum = datas.shape[1]

# for i in range(dataNum):
#     data = datas.iloc[i]
#     for p in range(propNum):
#         if data[p] == '':
#             print('Non', end='\t')
#         else:    
#             print(data[p], end='\t')
#     print()

connect = connectDatabase()
with connect.cursor() as cursor:
    for i in range(dataNum):
        try:
            data = datas.iloc[i]
            SQLCommand = 'SELECT ID FROM PARTICIPANT WHERE Phone=%s AND Mail=%s'
            cursor.execute(SQLCommand, (data[3], data[2]))
            id = cursor.fetchall()[0][0]

            try:
                file = data[6].split('id=')[1]
                time = datetime.datetime.strptime(data[5], '%Y/%m/%d')

                SQLCommand = 'INSERT RECEIPT VALUE (%s, %s, %s, %s, %s, %s)'
                cursor.execute(SQLCommand, (id, file, data[4], time, 'image url: '+data[6], False))
                connect.commit()
            except:
                pass
        except:
            print('ERROR: OWNER ID NOT FOUND')