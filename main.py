import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver_path=r"YOUR CHROME DRIVER PATH"

driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

store = driver.find_elements_by_css_selector("#store div")
# print(store.get_attribute("id"))
item_ids = [item.get_attribute("id") for item in store]

timeout = time.time() + 5
fivemin = time.time() + 60*5


start=True
while start:
    cookie.click()

    if time.time()>timeout:
        allprices=driver.find_elements_by_css_selector("#store b")
        item_price=[]

        # <b> to integer price
        for price in allprices:
            storetext=price.text
            # print(text)
            # Cursor - 15
            # Grandma - 100
            # Factory - 500
            # Mine - 2,000
            # Shipment - 7,000
            # Alchemy lab - 50,000
            # Portal - 1,000,000
            # Time machine - 123,456,789
            if storetext!="":
                cost=int( storetext.split("-")[1].strip().replace(",","")  )
                item_price.append(cost)
                # print(item_price) #i mean storetext.split("-")[1].strip()     ['15', '100', '500', '2,000', '7,000', '50,000', '1,000,000', '123,456,789']

        # dic for items(ids) and prices
        cookie_upgrades={}
        for n in range(len(item_price)):
            cookie_upgrades[item_price[n]]=item_ids[n]
            # print(cookie_upgrades) #  {15: 'buyCursor', 100: 'buyGrandma', 500: 'buyFactory', 2000: 'buyMine', 7000: 'buyShipment', 50000: 'buyAlchemy lab', 1000000: 'buyPortal', 123456789: 'buyTime machine'}


        #num of cookies count
        moneycookies=driver.find_element_by_id("money").text
        if "," in moneycookies:
            moneycookies=moneycookies.replace(",","")
        cookie_count=int(moneycookies)

        # manakunnapointskievevikonachu? things we can affird for
        afford_upgrades={}
        for price,item in cookie_upgrades.items():
            if cookie_count>price:
                afford_upgrades[price]=item
            # print(afford_upgrades)
            # {15: 'buyCursor'}
            # {15: 'buyCursor', 100: 'buyGrandma'}

        # purchase high
        high_upgrade_cost=max(afford_upgrades)
        # print(high_upgrade) #100
        to_purchase_id=afford_upgrades[high_upgrade_cost]

        driver.find_element_by_id(to_purchase_id).click()

        #then again click i mean wait for 5 secs
        timeout=time.time()+5

    if time.time()>fivemin:
        cookie_per_sec=driver.find_element_by_id("cps").text
        print(cookie_per_sec)
        break



