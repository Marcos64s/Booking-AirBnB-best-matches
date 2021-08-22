import time
import selenium
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import smtplib, ssl
import datetime
from nltk import flatten
from pretty_html_table import build_table
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

gmail_user = 'mendesmarcos66@gmail.com'
gmail_password = '2255Ma;)'

sorted_list=[]

subject = 'Super Hiper Mega Party em Budapeste'

urlair = 'https://www.airbnb.pt/s/Budapeste--Hungria/homes?adults=6&place_id=ChIJyc_U0TTDQUcRYBEeDCnEAAQ&checkin=2021-10-02&checkout=2021-10-05'
urlboo = 'https://www.booking.com/searchresults.pt-pt.html?aid=376389&label=Hoteis-dHPE1sykMRe*x3Pll8k6awS267724756065%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1011727%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfNeh-lbHkPZfvshG1kRNbU&sid=38151541cdbfdfb999b6a6826f32d3b2&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.pt-pt.html%3Faid%3D376389%3Blabel%3DHoteis-dHPE1sykMRe%252Ax3Pll8k6awS267724756065%253Apl%253Ata%253Ap1%253Ap22.563.000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-65526620%253Alp1011727%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YfNeh-lbHkPZfvshG1kRNbU%3Bsid%3D38151541cdbfdfb999b6a6826f32d3b2%3Bsb_price_type%3Dtotal%26%3B&ss=Budapeste%2C+Pest%2C+Hungria&is_ski_area=0&ssne=Portim%C3%A3o&ssne_untouched=Portim%C3%A3o&checkin_year=2021&checkin_month=10&checkin_monthday=2&checkout_year=2021&checkout_month=10&checkout_monthday=5&group_adults=8&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=pt&ac_click_type=b&dest_id=-850553&dest_type=city&iata=BUD&place_id_lat=47.499542&place_id_lon=19.046241&search_pageview_id=66244a58cecc0061&search_selected=true&ss_raw=Budapeste'
to = ['danielafreal@hotmail.com', 'biap0903@gmail.com', 'marta.goncalves.ribeiro@gmail.com', 'costa.pedro.goncalves@gmail.com',
        'joel.costa111@gmail.com', 'mar.sofia.sousa@gmail.com', 'marcos.mendes@hotmail.com', 'timoteo.pinto15@gmail.com']
# to = ['marcos.mendes@hotmail.com']

def remove_repeated(test_list):
    for i in test_list:
        if i not in test_list:
            test_list.append(i)
    return test_list

def selenium_airbnb(url,number):
    browser.get(url)
    browser.implicitly_wait(10)

    class_price = '_oluzbk'
    class_link  = '_gig1e7'
    class_name = '_1whrsux9'
    counter=0
    ts = time.time()
    list_all=[]

    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'lxml')
    for each_div in soup.findAll('div',{'class': class_link}):
        try:
            hotel_price = str(each_div.find('div',{'class': class_price}).text.split("€")[1])
            hotel_price = int(hotel_price)/number
            nome = str(each_div.find('span',{'class': class_name}).text)
            add = ['https://www.airbnb.pt/'+str(each_div.find('a')['href']), nome, hotel_price, number]
            list_all.append(add)
        except:
            print("No string")
    sorted_list = sorted(list_all, key=lambda x: x[1])
    sorted_list = remove_repeated(sorted_list)
    return sorted_list

def selenium_booking(url,number):
    browser.get(url)
    browser.implicitly_wait(10)

    class_price = 'bui-price-display__value prco-inline-block-maker-helper'
    class_link  = 'sr_item'
    class_name = 'sr-hotel__name'
    counter=0
    ts = time.time()
    list_all=[]

    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'lxml')
    for each_div in soup.findAll('div',{'class': lambda x: x and class_link in x.split()}):
        try:
            hotel_price = str(re.sub('[^0-9]', '', each_div.find('div',{'class': class_price}).text))
            hotel_price = int(hotel_price)/number
            nome = str(each_div.find('span',{'class': class_name}).text.rstrip())[1:]
            link = 'https://www.booking.pt/'+str(each_div.find('a',{'class': 'sr_item_photo_link'})['href'])
            add = [link, nome, hotel_price, number]
            list_all.append(add)
        except:
            print("No string")
    sorted_list = sorted(list_all, key=lambda x: x[1])
    sorted_list = remove_repeated(sorted_list)
    return sorted_list

listafinal=[]
browser = webdriver.Chrome(ChromeDriverManager().install())  # se usares o da chrome muda aqui para .Chrome
for number in [4,8]:
    url = 'https://www.airbnb.pt/s/Budapeste--Hungria/homes?adults='+str(number)+'&place_id=ChIJyc_U0TTDQUcRYBEeDCnEAAQ&checkin=2021-10-02&checkout=2021-10-05'
    listafinal.append(selenium_airbnb(url,number))
for number in [4,8]:    
    url = str("https://www.booking.com/searchresults.pt-pt.html?aid=376389&label=Hoteis-dHPE1sykMRe*x3Pll8k6awS267724756065%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1011727%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfNeh-lbHkPZfvshG1kRNbU&sid=38151541cdbfdfb999b6a6826f32d3b2&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.pt-pt.html%3Faid%3D376389%3Blabel%3DHoteis-dHPE1sykMRe%252Ax3Pll8k6awS267724756065%253Apl%253Ata%253Ap1%253Ap22.563.000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-65526620%253Alp1011727%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YfNeh-lbHkPZfvshG1kRNbU%3Bsid%3D38151541cdbfdfb999b6a6826f32d3b2%3Bsb_price_type%3Dtotal%26%3B&ss=Budapeste%2C+Pest%2C+Hungria&is_ski_area=0&ssne=Portim%C3%A3o&ssne_untouched=Portim%C3%A3o&checkin_year=2021&checkin_month=10&checkin_monthday=2&checkout_year=2021&checkout_month=10&checkout_monthday=5&group_adults="+str(number)+"&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=pt&ac_click_type=b&dest_id=-850553&dest_type=city&iata=BUD&place_id_lat=47.499542&place_id_lon=19.046241&search_pageview_id=66244a58cecc0061&search_selected=true&ss_raw=Budapeste")
    listafinal.append(selenium_booking(url,number))

sorted_list=flatten(listafinal)
browser.close()
        
def reshape(lst, n):
    return [lst[i*n:(i+1)*n] for i in range(len(lst)//n)]

sorted_list=reshape(sorted_list,4)

df = pd.DataFrame(sorted_list, columns = ['url', 'nome', 'preço por pessoa', 'numero de pessoas'])

df = df.sort_values(by=['preço por pessoa'])

df.to_excel("D:/OneDrive/OneDrive - Universidade de Aveiro/Mine/Git/readme/CodesBP.xlsx",sheet_name='Folha1')

pd.set_option('max_rows', None)
pd.set_option('display.max_columns', None)

# Create the plain-text and HTML version of your message
body = df.head(50).to_string()

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (gmail_user, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, email_text.encode('UTF-8'))
    server.close()

    print('Email sent!')
except Exception as ex:
    print('Something went wrong...' + ex)
