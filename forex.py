##This project WEB SCRAP data from NRB WEBSITE and then displays the Forex record
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

#create class
class get_Forex:
    """
    This class will get Forex data from NRB WebSite
    """
    def __init__(self):
        pass
    
    def todayForex(self):
        url='https://www.nrb.org.np/forex'
        response=requests.get(url,verify=False)  #If verify is not set false,will get error since SSL is not verified
        soup=BeautifulSoup(response.content,'html.parser')#Soup created
        exchf_table=soup.find_all('table')
        
        ##GEt DATA
        
        #FiX Exchange Rate
        td=exchf_table[0].find_all('td')
        currency1=td[0].find(class_='ml-2 text-uppercase').get_text()
        unit1=td[1].get_text()
        buy1=td[2].get_text()
        sell1=td[3].get_text()
        
        # Change string into lists
        cur=[currency1]
        unit=[unit1]
        buy=[buy1]
        sell=[sell1]
        
        # Varying Exchange Rate
        td1=exchf_table[1].find_all('td')
        
        
        i=0
        while i<len(td1):
            #            
            rem=i%4
            if rem==0:
                cur.append(td1[i].find(class_='ml-2 text-uppercase').get_text())
            elif rem==1:
                unit.append(td1[i].get_text())      
            elif rem==2:
                buy.append(td1[i].get_text())
            else:
                sell.append(td1[i].get_text())
            i=i+1
        
        cur_refine=[c.strip('\n') for c in cur] #To remove \n character from currency
        #To split currency and symbol: INR INDIAN RUPEE : INR, INDIAN RUPEE
        sym=[re.split(r'[\(\)]', cs)[0] for cs in cur_refine]
        currency=[re.split(r'[\(\)]', cs)[1] for cs in cur_refine]
        
        #Create DataFrame
        Exc_Rates=pd.DataFrame({
            'Currency':currency,
            'Symbol':sym,
            'Unit':unit,
            'Buying Rate':buy,
            'Selling Rate':sell
        })
        print(Exc_Rates)
    
forex=get_Forex() ###Create Object

##Call object forex.todayForex()






def CHange_Money(self):
            Forex=todayForex()
            usy=input("Input the symbol you want to check")
            usy=usy+' '
            i=0
            while i<len(Forex['Sym']):
                if usy==Forex['Sym'][i].lstrip():
                    print("Match Found for i= {}".format(i))
                    break
                i=i+1
            if i==len(Forex['Sym']):
                print("Please Enter Correct Symbol")
            else:
            #print('The exchange rate is {}'.format(Forex[:][i]))##cannot print
            # Create Display DF
            Disp=pd.DataFrame({
            'Currency':Forex['currency'][i],
            'Sym':Forex['Sym'][i],
            'unit':Forex['unit'][i],
            'sell price':Forex['sell_price'][i],
            'buy price':Forex['buy_price'][i] }, index=[0])
    
print(Disp)

