# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 15:28:33 2021

@author: Brandon Imstepf
"""


from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import re


#------------------------------------------------------------------------------#
#                                                                              #
# What is the most expensive color to play? What is the least? Let's find out. #
#                                                                              #
#------------------------------------------------------------------------------#


os.chdir("Case Study 2 - MTG")

#location = '2 GW Company.htm'
#locn = location.replace('.htm', '') #for export later


#Get all the html code related the Cards

#Setup the columns
names = []
namelen = []
colors = []
prices = []
cmcs = []
rarities = []

#this is to loop through the whole folder and scrape each .htm file
for filename in os.listdir():
    if filename.endswith(".htm"):
        print(filename)
        

        #this just sets up the HTML scraper
        soup = BeautifulSoup(open(filename, encoding="utf8"), "html.parser")
        
        #this isolates the parts of the HTML I want to extract from
        card_div = soup.find_all('tr',class_='cardItem')
        
        for container in card_div:
            
            #Name
            name = container.a.text
            names.append(name)
            
            #Name Length
            namelen.append(len(name))
            
            #Price
            price = container.find('span',class_='paper option').text
            price = price.replace('\n', '')
            prices.append(price)
            
            #Rarity
            rarity2 = container.find('td',class_='number').span
            rarity = str(rarity2)
            rarity = rarity.replace('<span class="rarity ', '')
            rarity = rarity.replace('\"></span>', '')
            rarities.append(rarity)
            
            
            #Color and CMC
            color2 = container.find('td', class_='manaCost', style="")
            color3 = str(color2)
            cmc = 0
            color = ''
            
                #I am in love with this library
                #finds all the numbers in the string following 'ms-' and converts to a list
            cmc2 = re.findall(r'ms-(\d+)',color3)
        
                #converts the list back into integers
            if not cmc2: #converts empty lists to a 0 generic mana cost
                cmc = 0 
            else:
                cmc = int(cmc2[0]) 
            
            #I could not find a way to make this cleaner. Embarrassing.
            if color3.__contains__('ms-u'):
                color += 'U'
                cmc += 1
                
            if color3.__contains__('ms-r'):
                color += 'R'
                cmc += 1
                
            if color3.__contains__('ms-b'):
                color += 'B'
                cmc += 1
                
            if color3.__contains__('ms-g'):
                color += 'G'
                cmc += 1
            
            if color3.__contains__('ms-w'):
                color += 'W' 
                cmc += 1
            
            if color == '':
                color = 'V'
                
            colors.append(color)
            cmcs.append(cmc)
            color3 = ''
            color = ''
    


#put everything into a nice data frame
cards = pd.DataFrame({
    'name': names,
    'namelength': namelen,
    'price': prices,
    'color': colors,
    'cmc':cmcs,
    'rarity': rarities,
    })

#changing the name length from a string to an int for cleaner data
cards['namelength'] = cards['namelength'].astype(int)

#checking the card counts
print(cards.value_counts())
cards = cards.drop_duplicates()
print("---------HERE WE REMOVE EXTRA CARDS----------")
print(cards.value_counts())

print(cards)

cards.to_csv('mtgData.csv')
#cards.to_csv(locn + ' mtg.csv')
