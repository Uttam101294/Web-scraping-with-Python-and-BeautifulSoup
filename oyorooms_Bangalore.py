import bs4
import requests
import csv
file=open("oyo.csv",'a+',newline="", encoding="utf-8")
writer=csv.writer(file)
writer.writerow(['Venue_Name', 'Address', 'Format', 'Price'])
v=input("Enter city name :")
url1="https://www.oyorooms.com/hotels-in-"+v+"/"
url2=url1+"/?page="
venues = list()
for i in range(32):
	j=i+1
	url=url2+str(j)
	data=requests.get(url)
	soup=bs4.BeautifulSoup(data.text,"html.parser")
	file=open("oyoBangalore.csv",'a+',newline="", encoding="utf-8")
	for div in soup.find_all('div',class_='hotelCardListing__descriptionWrapper'):
		try:
			venue_format = div.find('div',class_="amenityWrapper").text.strip()
		except Exception:
		    venue_format="Not Available"
		try:
		    price=div.find('span',class_="listingPrice__finalPrice").text.strip().encode('ascii', 'ignore').decode('utf-8')
		except Exception:
		 	price="NA"
		venue = {
		 	'venue_name': div.find('h3',class_="listingHotelDescription__hotelName d-textEllipsis").text.strip(),
		   	'address': div.find('div',class_="d-body-lg d-textEllipsis listingHotelDescription__hotelAddress").text.strip(),
		   	'format':venue_format,
		    'price': price
		    
		}
		print(venue)
		venues.append(venue)
		writer.writerow(venue.values())
