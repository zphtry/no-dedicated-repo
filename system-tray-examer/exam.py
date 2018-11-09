import requests
import re

rexp = r'''
<td>Информатика и вычислительная техника</td>
<td>09.04.01</td>
<td style="text-align: center;">40</td>
<td style="text-align: center;">\d+</td>
<td style="text-align: center;">[\d\.]+</td>
<td style="text-align: center;" rowspan="4">\d+</td>
<td style="text-align: center;">(\d+)</td><tr>'''


def getPoint():
	try:
		req = re.findall(rexp.replace('\n', '\s*'), requests.get('https://abitur.mtuci.ru/ajax.php?function=get_page&page_name=magistratura_livetable').text)
		if len(req) == 0: return 'ER'
		else: return req[0]
	except: return 'ER'
	