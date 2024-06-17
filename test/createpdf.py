#-*- coding: utf-8 -*-
 
from bs4 import BeautifulSoup as Soup
import sqlite3
import csv
import html

used_names = []
sqliteConnection = sqlite3.connect('C:/sqlite/landandowners.db')
cur = sqliteConnection.cursor()


soup = Soup(open("test.html", 'rt', encoding='UTF8'), 'html.parser', from_encoding='UTF8')

cur.execute('select * from owners')
rows = cur.fetchall()

sqliteConnection.close()


def insert_row(row):
    table_column_1 = '''<td width=109 valign=top style='width:81.75pt;border:solid black 1.0pt; 
    padding:5.0pt 5.0pt 5.0pt 5.0pt;height:22.35pt'><p class=MsoNormal 
    style='line-height:normal;border:none'>''' + row[0]+ '''</p></td>'''
    table_column_2 = '''<td width=265 valign=top style='width:198.75pt;border:solid black 1.0pt;
    border-left:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:22.35pt'><p 
    class=MsoNormal style='line-height:normal;border:none'>''' + row[1]+ '''</p></td>'''
    table_column_3 = '''<td width=250 valign=top style='width:187.5pt;border:solid
    black 1.0pt;border-left:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:22.35pt'>
    <p class=MsoNormal style='line-height:normal;border:none'>''' + row[2] + '''</p></td>'''
    html_row = '''<tr>''' + table_column_1 + table_column_2 + table_column_3 + '''</tr>'''

    html_row_soup = Soup(html_row, 'html.parser')
    soup.table.append(html_row_soup)

    
insert_row(rows[0])
insert_row(rows[3])
insert_row(rows[4])

with open("result.html", "w", encoding='UTF8') as file:
    file.write(str(soup))

