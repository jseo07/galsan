from bs4 import BeautifulSoup
from datetime import datetime
import copy 


sample = ["서장원", "20020709", "세종시 달빛로 165 803동 1901호", 
          "01041284955", [["충청남도 아산시 탕정면 갈산리 149-1", "지목", "150", "T"],
                          [ "충청남도 아산시 탕정면 갈산리 150-4", "지목2", "230", "F"]]]
 
table_row = '''
<tr style="height:22.3pt">
    <td style="width:37.4pt; border:0.75pt solid #939393; padding:1.4pt 1.02pt; vertical-align:middle">
        <p class="a" id="no" style="margin-top:2pt; text-align:center; line-height:160%; font-size:9pt; font-family:돋움체">1</p>
    </td>
    <td style="width:107.1pt; border:0.75pt solid #939393; padding:1.4pt 1.02pt; vertical-align:middle">
        <p class="a" id="landadr" style="margin-top:2pt; text-align:center; line-height:160%; font-size:9pt; font-family:돋움체">&#xa0;</p>
    </td>
    <td style="width:107.1pt; border:0.75pt solid #939393; padding:1.4pt 1.02pt; vertical-align:middle">
        <p class="a" id="jimok" style="margin-top:2pt; text-align:center; line-height:160%; font-size:9pt; font-family:돋움체">&#xa0;</p>
    </td>
    <td style="width:107.1pt; border:0.75pt solid #939393; padding:1.4pt 1.02pt; vertical-align:middle">
        <p class="a" id="area" style="margin-top:2pt; text-align:center; line-height:160%; font-size:9pt; font-family:돋움체">&#xa0;</p>
    </td>
    <td style="width:75.8pt; border:0.75pt solid #939393; padding:1.4pt 1.02pt; vertical-align:middle">
        <p class="a" id="bool" style="margin-top:2pt; text-align:center; line-height:160%; font-size:9pt; font-family:돋움체">&#xa0;</p>
    </td>
</tr>'''

with open('template.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
row_soup = BeautifulSoup(table_row, 'html.parser')
now = datetime.now()

#loland : list of land, [landadr, 지목, area, bool]
def replace_content(name, dob, usradr, phoneno, loland, resultno):
    old_name = soup.find(id="name")
    name1 = soup.find(id="name1")
    old_dob = soup.find(id="dob")
    old_usradr = soup.find(id="usradr")
    old_phoneno = soup.find(id="phoneno")
    old_loland = soup.find(id="landtable")
    year = soup.find(id="year")
    month = soup.find(id="month")
    day = soup.find(id="day")

    old_name.string = name
    name1.string = name
    old_dob.string = dob
    old_usradr.string = usradr
    old_phoneno.string = phoneno
    #add listofland to table
    year.string = now.strftime("%Y")
    month.string = now.strftime("%m")
    day.string = now.strftime("%d")
    for land in loland:
        old_loland.append(append_row(land))
    # Save the modified HTML back to the file
    with open(resultno, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

def append_row(land):
    row_soup_copy = copy.copy(row_soup)
    landadr = row_soup_copy.find(id="landadr")
    jimok = row_soup_copy.find(id="jimok")
    area = row_soup_copy.find(id="area")
    bool = row_soup_copy.find(id="bool")
    landadr.string = land[0]
    jimok.string = land[1]
    area.string = land[2]
    bool.append = land[3]
    return row_soup_copy

        
sample_land = [["충청남도 아산시 탕정면 갈산리 149-1", "지목", "150", "T"],
                          [ "충청남도 아산시 탕정면 갈산리 150-4", "지목2", "230", "F"]]
replace_content("서장원", "19990604", "어디시 저기구 동남동 어디아파트", "01098031012", sample_land, 'result.html')

