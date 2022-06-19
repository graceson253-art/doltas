
import json
from urllib import response
import requests
from csv import writer
from bs4 import BeautifulSoup
import json
from datetime import datetime
start_time = datetime.now()







resturants=[
    "https://www.talabat.com/uae/restaurant/621133/ginos-deli-jlt?aid=1308"
    , "https://www.talabat.com/uae/restaurant/645430/pasta-della-nona-jlt-jumeirah-lakes-towers?aid=1308",
     "https://www.talabat.com/uae/restaurant/50445/pizzaro-marina-3?aid=1308","https://www.talabat.com/uae/restaurant/605052/the-pasta-guyz-dubai-marina?aid=1308",
     "https://www.talabat.com/uae/restaurant/621796/pizza-di-rocco-jumeirah-lakes-towers--jlt?aid=1308",
     'https://www.talabat.com/uae/restaurant/640203/taco-mercado-dubai-marina?aid=1308','https://www.talabat.com/uae/restaurant/15231/harat-al-sham-al-barsha-1?aid=1308',
     'https://www.talabat.com/uae/restaurant/660555/hakka-wakka-al-barsha-1?aid=1308','https://www.talabat.com/uae/restaurant/632782/hot-spot-cafeteriaal-barsha-1?aid=1308',
     'https://www.talabat.com/uae/restaurant/43713/after-room-cafe-restaurant-dubai-marina?aid=1308'
    ]



with open("Resturants.csv","w",encoding="utf8",newline="\n") as f:
    empty_spaces = ['  ']
    heading_title = ['Resturant Details']
    heading_title2 = ['Menu Details']
    the_writer = writer(f)
    headers = ['Feature Name','Type','Description']
    
  

    for resturant  in resturants:

        the_writer.writerow(heading_title)
        the_writer.writerow(empty_spaces)
        the_writer.writerow(headers)

        response = requests.get(resturant)
        soup = BeautifulSoup(response.content,"lxml")

        script =  soup.find_all('script')[16].text.strip()
        data=json.loads(script)
        resturant_info = data['props']['pageProps']['gtmEventData']['restaurant']
        resturant_munu = data['props']['pageProps']['initialMenuState']['menuData']['items']

        resturant_name = resturant_info['name']
        resturant_logo=  resturant_info['logo']
        resturant_latitude = float(resturant_info['latitude'])
        resturant_longitude =float(resturant_info['longitude'])
        resturant_cusine_tags =[resturant_info['cuisineString']]
 
        rows = [ ['restaurant_name',type(resturant_name).__name__, resturant_name], 
                 ['resturant_logo',type(resturant_logo).__name__, resturant_logo], 
                 ['latitude',type(resturant_latitude).__name__, resturant_latitude], 
                 ['longitude',type(resturant_longitude).__name__, resturant_longitude], 
                 ['cuisine_tags',type(resturant_cusine_tags).__name__, resturant_cusine_tags]] 
                 

        
        the_writer.writerows(rows)
        the_writer.writerows(empty_spaces)
        the_writer.writerows(empty_spaces)
        the_writer.writerows(empty_spaces)
        the_writer.writerow(heading_title2)
        the_writer.writerows(empty_spaces)
        the_writer.writerow(headers)
        for index  in resturant_munu:
            item_name=   index['name']
            item_description = index['description']
            item_price =float(index['price'])
            item_image = index['image']

           

            menu_rows = [ ['item_name',type(item_name).__name__, item_name], 
                 ['item_description',type(item_description).__name__, item_description], 
                 ['item_price',type(item_price).__name__, f'AED {item_price}'], 
                 ['item_image',type(item_image).__name__, item_image], ]


           
            the_writer.writerows(menu_rows)     
            the_writer.writerows(empty_spaces)
            the_writer.writerows(empty_spaces)
            the_writer.writerows(empty_spaces)
             

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
        
    