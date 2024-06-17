from tabulate import tabulate
from bs4 import BeautifulSoup as Soup
import sqlite3
import csv

sqliteConnection = sqlite3.connect('C:/sqlite/landandowners.db')
cur = sqliteConnection.cursor()


file = open("test/ownersfile.csv", "r", encoding='UTF8')
data = list(csv.reader(file, delimiter=","))
file.close()

""""
table = [["서장원", "세종시 달빛로 165 거시기 거시기", "몇평"], 
         ["서배석", "서울시 어딘가 좋은곳", "대충 천평"]]
string = "<p>한글</p>"
string_utf = string.encode('utf-8')
soup = Soup(open("test/test.html"), 'html.parser')
table_soup = Soup(string_utf, 'html.parser', from_encoding='utf-8')
#Soup(tabulate(table, tablefmt='html'), 'html.parser', from_encoding='cp949')
soup.body.append(table_soup)
with open("test/test.html", "w") as file:
    file.write(str(soup))
    
    """

def add_owner(name, adress, land_ad):
    value_str = '''"''' + name + '''"''' + ''', "''' + adress + '''", "''' + land_ad + '''"'''
    sql = ''' INSERT INTO owners VALUES(''' + value_str + ''')'''
    cur.execute(sql)
    sqliteConnection.commit()

def add_data_to_table(data):
    for line in data:
        name = line[0]
        adress = line[1]
        land_ad = '''충청남도 아산시 탕정면 ''' + line[2] + ''' ''' + line[3]
        add_owner(name, adress, land_ad)

def main():
    add_data_to_table(data)

main()
