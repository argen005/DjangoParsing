from django.shortcuts import render
from .models import Phone, Price
from bs4 import BeautifulSoup
import re
import requests

#def parse_myphone():
    # Код парсинга для myphone.kg

#def parse_sulpak():
    # Код парсинга для sulpak.kg

def parse_softech():
    url = "https://softech.kg/phones/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        phone_links = []

        for link_tag in soup.find_all('a', href=True):
            link_url = link_tag['href']
            if 'phones' in link_url and link_url not in phone_links:
                phone_links.append(link_url)

        for phone_link in phone_links:
            phone_response = requests.get(phone_link)
            if phone_response.status_code == 200:
                phone_soup = BeautifulSoup(phone_response.text, "html.parser")
                phone_name_tags = phone_soup.find_all('a', href=re.compile(r'.*smartfon.*', re.I))          
                for phone_name_tag in phone_name_tags:
                        
                        print(phone_name_tag.text)
                        print(phone_name_tag['href'])
parse_softech()
