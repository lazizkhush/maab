from bs4 import BeautifulSoup

with open('weather.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

info = soup.find_all('tr')
info_list = [i.text.replace('\n', ' ').lstrip()  for i in info]

highest_temp = 0
highest_temp_day = ''
temp_sum = 0
sunny_days = []
for i in range(len(info_list)):
    item =  info_list[i]
    print(item)
    if i>0:
        items = item.split()
        for x in range(len(items)):
            if x == 1:
                temp = int(items[x][:2])
                temp_sum += temp
                if temp>highest_temp:
                    highest_temp = temp
                    highest_temp_day = items[0]

            elif x == 2:
                item[x] == 'Sunny'
                sunny_days.append(items[0])
                
print("The day with Highest temprature:")
print(highest_temp_day, f'{highest_temp}°C')

print(f'Sunny days: {sunny_days}')

avg_temp = temp_sum/(len(info_list)-1)
print(f"Average temprature: {avg_temp}")



    

