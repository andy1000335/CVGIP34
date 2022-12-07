import pygsheets
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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

options = webdriver.ChromeOptions()
options.add_argument('--incognito')

receipt = 'https://docs.google.com/spreadsheets/d/1aEEzlAJ4n-Z3BZBZ47-CEDnDz5224XoiagpkZE4OqXo/edit#gid=986872402'
gc = pygsheets.authorize(service_account_file='operating-bird-319611-b9cee5c4fb45.json')
sheet = gc.open_by_url(receipt)[0]
datas = sheet.get_as_df(start='A1', index_colum=0, empty_value=None, include_tailing_empty=False, numerize=False)
dataNum = datas.shape[0]
propNum = datas.shape[1]

for i in range(dataNum):
    data = datas.iloc[i]
    print(str(i)+'\n姓名\t\t'+data[1]+'\n信箱\t\t'+data[2]+'\n電話\t\t'+data[3] \
          +'\n帳戶末5碼\t'+data[4]+'\n匯款時間\t'+data[5]+'\n審核\t\t'+str(data[7]))
    print('----------------------------------------')

while(True):
    print('\n選擇號後將顯示匯款證明圖片，輸入 Q 或 q 以離開程式')
    id = input('請選擇編號：')
    if id=='Q' or id =='q':
        print('\n退出程式...\n')
        break
    else:
        try:
            connect = connectDatabase()
            data = datas.iloc[int(id)]
            path = data[6]
            print('\n圖片開啟中...')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            driver.get(path)
            print('\n'+id+'\n姓名\t\t'+data[1]+'\n信箱\t\t'+data[2]+'\n電話\t\t'+data[3] \
                  +'\n帳戶末5碼\t'+data[4]+'\n匯款時間\t'+data[5]+'\n'+'審核\t\t'+str(data[7]))
            check = input('是否審核通過？(Y/N) ')

            with connect.cursor() as cursor:
                if check=='Y' or check=='y':
                    try:
                        SQLCommand = 'UPDATE RECEIPT SET isCheck=%s WHERE FileName=%s'
                        cursor.execute(SQLCommand, (1, data[6].split('id=')[1]))
                        connect.commit()
                        sheet.update_value('H'+str(int(id)+2), 1)
                        print('\n審核完成')
                    except pymysql.err.OperationalError:
                        print('\nERROR: 資料庫不存在該資料，請確定該資料已上傳資料庫')   
                elif check=='N' or check=='n':
                    try:
                        SQLCommand = 'UPDATE RECEIPT SET isCheck=%s WHERE FileName=%s'
                        cursor.execute(SQLCommand, (0, data[6].split('id=')[1]))
                        connect.commit()
                        sheet.update_value('H'+str(int(id)+2), 0)
                        print('\n審核完成')
                    except pymysql.err.OperationalError:
                        print('\nERROR: 資料庫不存在該資料，請確定該資料已上傳資料庫')    
                else:
                    print('輸入錯誤')
        except IndexError:
            print('編號不存在，請重新輸入')
        except pymysql.err.OperationalError:
            print('\nERROR: 資料庫連結錯誤，請確定網路狀態')
            break