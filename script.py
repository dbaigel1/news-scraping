#Created by Daniel Baigel 11/10/18

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime as dt
import csv
from textblob import TextBlob
#create a bunch of soup, one for each news source
#then scrape the headlines and see how they trend each day
#dataframe should have column names of: date, 4 news sources, type of headline, positive/neutral/negative trend
#further applications:
#	create categories for types of news: sports, politics, environment, technology, finance, entertainment, international, pop culture
#   and then label them as positive, neutral, or negative using machine learning
# bring in old data from mainfile
#TODO: ADD SUBJECTIVITY, makes analysis more interesting

#get the date
today = dt.today()

#create lists of categories to compare to
politics = ["trump", "dems", "democrats", "democrat", "democracy", "rep", "republican", 
"republicans", "politics", "election", "elections", "candidate", "candidates", "ballots",
"ballot", "campaign", "government", "govt", "gov't", "senate", "judiciary", "president",
"paul ryan", "vote", "voting", "votes", "GOP", "DNC", "RNC"]

sports = ["soccer", "football", "tennis", "hockey", "baseball", "world series", 
"world-series", "sport", "sports", "champion", "tournament", "lacrosse", "softball",
"olympics", "world cup"]

environment = ["storm", "typhoon", "earthquake", "tsunami", "hurricane", "tornado", 
"earthquakes", "rain", "global warming", "climate", "environment"]

technology = ["amazon", "iphone", "android", "google", "microsoft", "macbook", "technology"]

international = ["france", "london", "england", "uk", "brexit", "british", "china",
"japan", "chinese", "tariff", "tariffs", "south africa", "asia", "south america", 
"africa", "african", "countries", "abroad"]


##########################Get the soup ready##################################################
headlines = []

###########################FOX#################################################
urlFOX = requests.get("https://www.foxnews.com/")
if urlFOX.status_code != 200:
    print(urlFOX.status_code + "\n")
    print("Something is wrong with Fox...")
    sys.exit("Check website status code")

soupFOX = BeautifulSoup(urlFOX.content, 'html.parser')

FOXcontainer = soupFOX.find(class_="collection collection-spotlight has-hero")
FOXcontainer2 = FOXcontainer.find('header', class_='info-header')

FOXheadline = FOXcontainer2.find('a').get_text()
foxBlob = TextBlob(FOXheadline)
foxPolarity = foxBlob.sentiment.polarity
foxSubj = foxBlob.sentiment.subjectivity
print(FOXheadline)
print(foxPolarity)
print(foxSubj)
print("Done with FOX")
headlines.append(FOXheadline)


##########################NBC#################################################
urlNBC = requests.get("https://www.nbcnews.com/")

if urlNBC.status_code != 200:
    print(urlNBC.status_code + "\n")
    print("Something is wrong with NBC...")
    sys.exit("Check website status code")

soupNBC = BeautifulSoup(urlNBC.content, 'html.parser')

NBCcontainer = soupNBC.find('article', class_="teaseCard content___3FGvZ")

NBCcontainer2 = NBCcontainer.find_all('h2')

NBCheadline = NBCcontainer2[1].find('a').get_text()
nbcBlob = TextBlob(NBCheadline)
nbcPolarity = nbcBlob.sentiment.polarity
nbcSubj = nbcBlob.sentiment.subjectivity
print(NBCheadline)
print(nbcPolarity)
print(nbcSubj)
print("Done with NBC")

headlines.append(NBCheadline)

############################WP#################################################
urlWP = requests.get("https://www.washingtonpost.com/?noredirect=on")
if urlWP.status_code != 200:
    print(urlWP.status_code + "\n")
    print("Something is wrong with Washington Post...")
    sys.exit("Check website status code")

soupWP = BeautifulSoup(urlWP.content, 'html.parser')

WPcontainer = soupWP.find(class_="headline small normal-style text-align-inherit ")
WPheadline = WPcontainer.find('a').get_text()
wpBlob = TextBlob(WPheadline)
wpPolarity = wpBlob.sentiment.polarity
wpSubj = wpBlob.sentiment.subjectivity
print(WPheadline)
print(wpPolarity)
print(wpSubj)
print("Done with WP")

headlines.append(WPheadline)
# ##########################WP#################################################
urlABC = requests.get("https://abcnews.go.com/")
if urlABC.status_code != 200:
    print(urlABC.status_code + "\n")
    print("Something is wrong with ABC...")
    sys.exit("Check website status code")

soupABC = BeautifulSoup(urlABC.content, 'html.parser')

ABCcontainer = soupABC.find(id="row-1", class_="rows")

ABCheadline = ABCcontainer.find('h1').get_text().strip()

abcBlob = TextBlob(ABCheadline)
abcPolarity = abcBlob.sentiment.polarity
abcSubj = abcBlob.sentiment.subjectivity

print(ABCheadline)
print(abcPolarity)
print(abcSubj)
print("Done with ABC")

headlines.append(ABCheadline)
###########################Breitbart###################################################

urlBB = requests.get("https://www.breitbart.com/")
if urlBB.status_code != 200:
    print(urlBB.status_code + "\n")
    print("Something is wrong with Breitbart...")
    sys.exit("Check website status code")

soupBB = BeautifulSoup(urlBB.content, 'html.parser')

BBcontainer = soupBB.find(class_="top_article_main")

BBheadline = BBcontainer.find('h2').get_text().strip()

bbBlob = TextBlob(BBheadline)
bbPolarity = bbBlob.sentiment.polarity
bbSubj = bbBlob.sentiment.subjectivity

print(BBheadline)
print(bbPolarity)
print(bbSubj)
print("Done with BB")

headlines.append(BBheadline)
###########################BuzzFeed################################################


urlBF = requests.get("https://www.buzzfeed.com/")
if urlBF.status_code != 200:
    print(urlBF.status_code + "\n")
    print("Something is wrong with BuzzFeed...")
    sys.exit("Check website status code")

soupBF = BeautifulSoup(urlBF.content, 'html.parser')

BFcontainer = soupBF.find(class_="featured-card__body")

BFheadline = BFcontainer.find('h1').get_text().strip()

bfBlob = TextBlob(BFheadline)
bfPolarity = bfBlob.sentiment.polarity
bfSubj = bfBlob.sentiment.subjectivity

print(BFheadline)
print(bfPolarity)
print(bfSubj)
print("Done with BF")

headlines.append(BFheadline)
####################################################################################
categories = []
for headline in headlines:
    #create array of words in headline
    word = ""
    words = []
    categoryTag = ""
    for char in headline:
        char = char.lower()
        if char != ' ':
            word += char
        else:
            words.append(word)
            word = ""
    for word in words:

        if word in politics:
            categoryTag = "politics"
            break
        elif word in sports:
            categoryTag = "sports"
            break
        elif word in international:
            categoryTag = "international"
            break
        elif word in environment:
            categoryTag = "environment"
            break
        elif word in technology:
            categoryTag = "technology"
            break
        else:
            continue

    if categoryTag == "":
        categoryTag = "miscellaneous"
    
    categories.append(categoryTag)

foxCategory = categories[0]
nbcCategory = categories[1]
wpCategory = categories[2]
abcCategory = categories[3]
bbCategory = categories [4]
bfCategory = categories[5]

#Create a pandas dataframe
columnNames = ["Date", "Fox Headline", "Fox Polarity", "Fox Subjectivity","Fox Category", 
"NBC Headline", "NBC Polarity", "NBC Subjectivity", "NBC Category", 
"Wash Post Headline", "Wash Post Polarity", "Wash Post Subjectivity", "Wash Post Category", 
"ABC Headline", "ABC Polarity", "ABC Subjectivity", "ABC Category",
"Breitbart Headline", "Breitbart Polarity", "Breitbart Subjectivity", "Breitbart Category", 
"Buzzfeed Headline", "Buzzfeed Polarity", "Buzzfeed Subjectivity", "Buzzfeed Category"]

#rounding polarities and subjectivities to 2 decimal places
foxPolarity = round(foxPolarity,2)
nbcPolarity = round(nbcPolarity,2)
abcPolarity = round(abcPolarity,2)
wpPolarity = round(wpPolarity,2)
bbPolarity = round(bbPolarity,2)
bfPolarity = round(bfPolarity,2)

foxSubj = round(foxSubj,2)
nbcSubj = round(nbcSubj,2)
abcSubj = round(abcSubj,2)
wpSubj = round(wpSubj,2)
bbSubj = round(bbSubj,2)
bfSubj = round(bfSubj,2)

newsTable = pd.DataFrame(columns = columnNames)
newsTable.loc[0] = [today, FOXheadline, foxPolarity, foxSubj, foxCategory, 
NBCheadline, nbcPolarity, nbcSubj, nbcCategory, 
WPheadline, wpPolarity, wpSubj, wpCategory, 
ABCheadline, abcPolarity, abcSubj, abcCategory, 
BBheadline, bbPolarity, bbSubj, bbCategory, 
BFheadline, bfPolarity, bfSubj, bfCategory]
#print(newsTable)

#append csv onto main csv file
#if not working, try changing index to None
newFile = newsTable.to_csv('new_csv.csv', index = 0, header=False)

sourceFile = open('new_csv.csv', 'r')
data = sourceFile.read()
with open('data_file.csv', 'a') as destFile:
    destFile.write(data)












