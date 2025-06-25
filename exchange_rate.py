import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.select('table.tbl_exchange tbody tr')

data = []
for row in rows:
    currency = row.select_one('td.tit').get_text(strip=True)
    rate = row.select_one('td.sale').get_text(strip=True)
    data.append([currency, rate])

df = pd.DataFrame(data, columns=['Currency', 'Exchange Rate'])
df.to_excel('exchange_rate.xlsx', index=False)

print('✅ 환율 엑셀 저장 완료')
