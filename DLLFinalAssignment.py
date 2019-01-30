import matplotlib.pyplot as plt
import numpy as np
import psutil as pu
import requests
import platform

NUM_DATA = 109

first_data = []
symbols = []
dates = []
opens = []
highs = []
lows = []
closes = []
volumes = []
corresponds = []

print("running using: ")
print(platform.processor())

pu.cpu_percent(interval=None)

def get_the_data():
	file = open("ETFs.csv","r")
	
	for i in range(0, NUM_DATA):
		first_data.append(file.readline())
		
	dates.append([])
	
	opens.append([])
	
	highs.append([])
	
	lows.append([])
	
	closes.append([])
	
	volumes.append([])
	
	str1 = 'https://www.google.com/finance/historical?output=csv&q=+'
	str3 = '+&startdate=startmo+startdy+startyr&enddate=endmo+enddy+endyr'
	
	for i in range(0, NUM_DATA):
		str2 = first_data[i].split(',')
		URL = str1 + str2[0] + str3
		symbols.append(str2[0])
		append_this = str2[1].rstrip("\r\n")
		corresponds.append(append_this)
		theRequest = requests.get(URL)
		split_string = theRequest.text.splitlines()
		
		some_date_range = []
		some_opens_range = []
		some_highs_range = []
		some_lows_range = []
		some_closes_range = []
		some_volumes_range = []
		
		for j in range(2, len(split_string)):
			second_string = split_string[j].split(',')

			some_date_range.append(second_string[0])
			if second_string[1] != '-':
				some_opens_range.append(float(second_string[1]))
			if second_string[2] != '-':
				some_highs_range.append(float(second_string[2]))
			if second_string[3] != '-':
				some_lows_range.append(float(second_string[3]))
			if second_string[4] != '-':
				some_closes_range.append(float(second_string[4]))
			some_volumes_range.append(int(second_string[5]))
		
		dates.append(some_date_range)
		opens.append(some_opens_range)
		highs.append(some_highs_range)
		lows.append(some_lows_range)
		closes.append(some_closes_range)
		volumes.append(some_volumes_range)
			
get_the_data()

print("data got. cpu usage: ")
print(pu.cpu_percent(interval=None))

the_x_e = []
the_y_e = []
the_x_cu = []
the_y_cu = []
the_x_co = []
the_y_co = []
the_x_b = []
the_y_b = []

for i in range(1, NUM_DATA):
	if max(closes[i]) - min(closes[i]) != 0 and max(volumes[i]) - min(volumes[i]) != 0:
		append_me_x = (closes[i][0] - min(closes[i])) / (max(closes[i]) - min(closes[i]))
		append_me_y = (volumes[i][0] - min(volumes[i])) / (max(volumes[i]) - min(volumes[i]))
		
		
		if corresponds[i] == "Equity":
			the_x_e.append(append_me_x)
			the_y_e.append(append_me_y)
		elif corresponds[i] == "Commodity":
			the_x_co.append(append_me_x)
			the_y_co.append(append_me_y)
		elif corresponds[i] == "Currency":
			the_x_cu.append(append_me_x)
			the_y_cu.append(append_me_y)
		elif corresponds[i] == "Bond":
			the_x_b.append(append_me_x)
			the_y_b.append(append_me_y)
	
plt.scatter(the_x_e, the_y_e, color='red', label='Equity')
plt.scatter(the_x_co, the_y_co, color='green', label='Commodity')
plt.scatter(the_x_cu, the_y_cu, color='blue', label='Currency')
plt.scatter(the_x_b, the_y_b, color='magenta', label='Bond')

legend = plt.legend(loc='best', shadow=True, fontsize='medium')

plt.show()

print("graph made. CPU usage: ")
print(pu.cpu_percent(interval=None))