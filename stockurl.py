import re
import urllib.request
import numpy as np
import math

def yahoostat(stock):
	url = 'https://finance.yahoo.com/quote/' + stock + '/key-statistics?p=' + stock
	try:
		x = str(urllib.request.urlopen(url).read())
		
		moving_avg= float(x.split('200-Day Moving Average</span><!-- react-text:')[1].split('</td></tr>')[0].split('>')[-1])
		price= x.split('data-icon="search" data-reactid="30">')[1]

		#trailing_pe = x.split('Trailing P/E</span><!-- react-text: 30 --> <!-- /react-text --><!-- react-text: 31 --><!-- /react-text --><sup aria-label="KS_HELP_SUP_undefined" data-reactid="32"></sup></td><td class="Fz(s) Fw(500) Ta(end)" data-reactid="33">')[1].split('</td>')[0]
		#trailing_pe = float(trailing_pe)
		
		#print(stock, ': ', price)
	
	except:
		print('error')


def sp():
	#lst = []
	sourcecode = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	x = str(sourcecode.read())
	st = re.findall('[/:].">.</a></td>', x)
	st += re.findall('[/:]..">..</a></td>', x)
	st += re.findall('[/:]...">...</a></td>', x)
	st += re.findall('[/:]....">....</a></td>', x)
	st += re.findall('[/:].....">.....</a></td>', x)

	lst = [i.split('>')[1].split('<')[0] for i in st]
	lst.sort()
	return(lst)
	
sp500 = sp()

for each in sp500:
	yahoostat(each)




