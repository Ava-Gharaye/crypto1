from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_price(text: str):
    return float(
        text.get_text().replace("$", "").replace("", "") .replace("\n", "").replace(",", "")
    )


html_code = urlopen("https://coinranking.com/")
bs4 = BeautifulSoup(html_code.read(), "lxml")
table = bs4.find_all("div", {"class": "valuta"})
valuefor= 10

count = 0
total: float = 0
batch_for = 0

for i in range(0, valuefor, 2):
    count = count + 1
    price = get_price(table[i])
    print(price)
    total = total + price

    if count == 5:
        batch = batch_for+ 1
        print(f"avg [{batch_for}] : { total / 5}")
        print("-------------------------")
        total = 0
        count = 0
        #end



        #2


from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_price(text: str):
    return float(
        text.get_text().replace("$", "").replace("", "") .replace("\n", "").replace(",", "")
    )


html_code2 = urlopen("https://coinmarketcap.com/")
bs42 = BeautifulSoup(html_code.read(), "lxml")
table2 = bs4.find_all('div',{'class':'sc'})
valuefor2= 10

count2 = 0
total2: float = 0
batch_for2 = 0

for i in range(0, valuefor2, 2):
    count2 = count2 + 1
    price2 = get_price(table[i])
    print(price2)
    total2 = total2 + price2

    if count2 == 5:
        batch2 = batch_for2+ 1
        print(f"avg [{batch_for2}] : { total2 / 5}")
        print("-------------------------")
        total2 = 0
        count2 = 0


    
if total2/5 > total/5 :
 print ("the first site is cheapear")
elif total/5 >total2/5 :
 print("the second site is cheaper") 
else :
 print ("they have same price")

        
#end