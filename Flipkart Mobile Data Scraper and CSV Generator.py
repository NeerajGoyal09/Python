import pandas as pd
import requests 
from bs4 import BeautifulSoup

# Function to extract data from HTML
def get_data(list_name, tag_type , class_name) :
    data = box.find_all(tag_type, class_ = class_name)
    for i in data :
        sep_data = i.text
        list_name.append(sep_data)
Names = []
Prices = []
Storage = []
Display = []
Camera = []

# Scraping mobile phone data from Flipkart
for i in range(1,15):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    box = soup.find('div' , class_ = "_1YokD2 _3Mn1Gg")

    get_data(Names,"div","_4rR01T")
    get_data(Prices,"div","_30jeq3 _1_WHN1")

    Feature_box = box.find_all("ul",class_ = "_1xgFaf")
    for i in Feature_box :
        Features_lines = i.find_all("li", class_ = "rgWa7D")
        for i in range(3) :
            data = Features_lines[i].text
            if i == 0 :
                Storage.append(data)
            elif i == 1:
                Display.append(data)
            elif i == 2 :
                Camera.append(data)
    
# Creating a DataFrame and saving as CSV
df  = pd.DataFrame({"Names": Names , "Prices" : Prices ,"Storage": Storage , "Display" : Display , "Camera" : Camera })

df["Prices"] = df["Prices"].str[1:]

df["Prices"] = df["Prices"].str.replace(",","")

df["Prices"] = df["Prices"].astype(int)

initial_rows = df.shape[0]
# filtering mobile phones with prices exceeding 50,000 rupees
df = df[df['Prices'] <= 50000]

removed_rows = initial_rows - df.shape[0]
print("Number of removed rows :",removed_rows)

df.to_csv("Mobiles_under_50000.csv")

print("The file has been generated ")
