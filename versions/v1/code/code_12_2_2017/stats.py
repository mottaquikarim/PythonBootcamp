from bs4 import BeautifulSoup
from requests import get
import pandas as pd

# grab the HTML from source
r = get('http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights')

soup = BeautifulSoup(r.text, 'html.parser')
table = soup.findAll("table", { "class" : "wikitable" })
if len(table):
    table = table[0]
rows = table.findAll('tr')
glossary = rows[0]
data = rows[1:]

# grab all the TH values from glossary
th = [header.text.strip() for header in glossary.findAll('th')]
data_dict = {val: [] for val in th}
# print(data_dict)
# print(th)
# print(data)

for data_row in data:
    c = data_row.findAll('td')
    for idx, c_item in enumerate(c):
        dict_key = th[idx]
        d = c_item.text
        if dict_key == 'Weight(pounds)':
            d = int(d or 0)
        data_dict[dict_key].append(d)

df = pd.DataFrame(data_dict)
# print(df.loc[:,['Weight(pounds)','Height(inches)']])
print(df.head())
print(df.sort_values(by='Weight(pounds)'))

