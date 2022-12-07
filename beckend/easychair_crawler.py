from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--incognito')

path = 'https://easychair.org/my/verified?info=104498922.jLBsIk2sXtEGDB1O#'
account = 't109318147'
password = 'wang980001'

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(path)
driver.implicitly_wait(10)

driver.find_element_by_id('name').send_keys(account)
driver.find_element_by_id('password').send_keys(password)
ActionChains(driver).click(driver.find_element_by_name('Log in')).perform()
driver.implicitly_wait(10)

driver.get('https://easychair.org/conferences/submissions?a=26860630')
table = driver.find_element_by_id('ec:table1').find_elements_by_tag_name('tbody')[1]
datas = table.find_elements_by_tag_name('tr')

papers = []
for row in datas:
    p = []
    info = row.find_elements_by_tag_name('td')
    for col in info:
        if col.text != '':
            p.append(col.text)
    papers.append(p)


#---------------- SQL script ----------------#

import pymysql
import datetime

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
    for paper in papers:
        id = paper[0]
        title = paper[2]
        time = '2021 ' + paper[3]
        author = paper[1]
        isPass = True
        owner = None
        time = datetime.datetime.strptime(time, '%Y %b %d, %H:%M')
        try:
            SQLCommand = 'INSERT PAPER VALUE (%s, %s, %s, %s, %s, %s)'
            cursor.execute(SQLCommand, (id, title, time, author, isPass, owner))
            connect.commit()
        except pymysql.err.IntegrityError:
            SQLCommand = 'UPDATE PAPER SET Title=%s, Time=%s, Author=%s WHERE PaperId=%s'
            cursor.execute(SQLCommand, (title, time, author, id))
            connect.commit()
        # except:
            # pass