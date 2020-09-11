from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

chrome_options = Options()
#chrome_options.add_argument("--headless")
path = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(path, options=chrome_options)

browser.get("https://phd.co.id/login")
print("Please input your login credentials.")
emails = input("Email: ")
passwords = getpass.getpass("Password:")
email = browser.find_element_by_xpath('//*[@id="email"]')
email.send_keys(emails)
pw = browser.find_element_by_xpath('//*[@id="password"]')
pw.send_keys(passwords)
pw.send_keys(Keys.RETURN)
otps = input("OTP: ")
otp = browser.find_element_by_xpath('//*[@id="otp"]')
otp.send_keys(otps)
otp.send_keys(Keys.RETURN)

time.sleep(3)
loc = browser.find_element_by_xpath('//*[@id="mapDelivery"]')
my_address = input("\nInput your address: ")
loc.send_keys(my_address)
time.sleep(3)
loc.send_keys(Keys.ARROW_DOWN)
loc.send_keys(Keys.RETURN)
time.sleep(3)

order_now = browser.find_element_by_xpath('//*[@id="maps"]/div/div/div[1]/div[3]/div/div[4]/div/div/div/div/div/div/div/div/button')
order_now.click()
time.sleep(3)
pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/a[3]')
pizza.click()

pizza_pick = ""
while pizza_pick != "0":
    print("\nPizza List:")
    print("[1] Tripple Meat Lovers\n[2] American Favourite\n[3] American Favourite Chikecken")
    print("[4] Pepperoni\n[5] Meat Lovers\n[6] Meat Lovers Cheesy Mayo")
    print("[7] Meat Lovers Chicken\n[8] Super Supreme\n[9] Super Supreme Chiken")
    print("[10] Splitza Signature\n[11] Meaty\n[12] Supreme")
    print("[13] Cheesy Galore\n[14] Tuna Melt\n[15] Hawaiian Chicken")
    print("[16] Veggie Garden\n[17] Splitza Classic")
    print("[0] Done")
    pizza_pick = input("Pick your pizza: ")

    if pizza_pick == "1":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "2":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "3":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "4":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "5":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[5]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "6":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[6]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "7":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[7]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "8":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[8]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "9":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[9]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "10":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[10]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "11":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[11]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "12":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[12]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "13":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[13]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "14":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[14]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "15":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[15]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "16":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[16]/div[2]/div/button')
        add_pizza.click()
    if pizza_pick == "17":
        add_pizza = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[17]/div[2]/div/button')
        add_pizza.click()

drink = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/a[6]')
drink.click()
drink_pick = ""
while drink_pick != "0":
    print("\nDrink List:")
    print("[1] Chocolicious\n[2] Red Summer Breeze\n[3] Melon Lemonade")
    print("[4] Orange Drinks\n[5] Lemon Tea\n[6] Cappucino Jelly")
    print("[7] Aqua 300 mL\n[0] Done")
    drink_pick = input("Pick your drink: ")

    if drink_pick == "1":
        add_drink = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/button')
        add_drink.click()
    if drink_pick == "2":
        add_drink = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/button')
        add_drink.click()
    if drink_pick == "3":
        add_drink = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/button')
        add_drink.click()
    if drink_pick == "4":
        add_drink = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/div/button')
        add_drink.click()
    if drink_pick == "5":
        add_drink = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[5]/div[2]/div/button')
        add_drink.click()
    if drink_pick == "6":
        add_drink = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[6]/div[2]/div/button')
        add_drink.click()
    if drink_pick == "7":
        add_drink = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[7]/div[2]/div/button')
        add_drink.click()

warning = input("Ready to checkout[y/n]?")
if warning == "y" :
    checkout = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/a')
    checkout.click()

time.sleep(3)
payment = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div/form/div[3]/div[2]/ul/li[2]/label/span/span[2]')
payment.click()

fee = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div/form/div[3]/div[2]/ul/li[2]/label/span/span[2]')
print("Your total fee: {}".format(fee.text))

changes = input("Input amount of change: ")
change = browser.find_element_by_xpath('//*[@id="amount_of_change"]')
change.send_keys(changes)

policy = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div/form/div[5]/div[1]')
policy.click()


time.sleep(10)