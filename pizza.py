from selinium import webdriver
from time import sleep
import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',130)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r =sr.Recognizer()



def pizza():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.dominos.co.in/')
    speak('hello sir welcome to dominos')

    driver.find_element_by_link_text('ORDER ONLINE NOW').click()

    driver.find_element_by_class_name('srch-cnt-srch-inpt').click()
    sleep(2)

    speak('we are fetching your location')

    location ='104,Main 7Rd,Ward No 7 Secunderabad,Alankrita Meadows,Trimulgherry,Secunderabad, Telangana 500015, India'
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input').send_keys(location)
    sleep(2)

    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]').click()
    sleep(5)

    try:

        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[1]').click()
        sleep(2)

    except:
        exit()


    speak('enter your login details')
    with sr.Microphone() as source:
        print("listining....")
        audio = r.listen(source)
        phone_num = r.recognize_google(audio)

        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(
            phone_num)
        sleep(5)

        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
        sleep(5)

    with sr.Microphone() as source:
        print("listining....")
        audio = r.listen(source)
        rec_otp = r.recognize_google(audio)
        otp_num = rec_otp
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input').send_keys(
            otp_num)
        sleep(10)
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span').click()
        sleep(10)


# till here the process is done with the voice command and the menu part of the dominos website sometime it will be change so iam not doing voice
   # command to the menu part and here there is small part that will order automatically by giving the pizza name

    # speak add pizza
    # rec_pizza
    # pz = rec_pizza
    pz ='Farmhouse'

    #

    if 'Margherita' in pz:
        driver.find_element_by_xpath('//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click
        sleep(5)
        #speak'Make my pizza more yummy?'
        cheeze ='yes'
        if 'yes'in cheeze:
            driver.find_element_by_xpath('//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[2]/button/span').click()
            sleep(5)
        else:
            driver.find_element_by_xpath('//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
            sleep(5)


    elif 'Farmhouse' in pz:
        driver.find_element_by_xpath('//*[@id="mn-lft"]/div[2]/div/div[2]/div/div/div[2]/div[3]/div/button/span').click()
        sleep(10)
        cheeze ='yes'

        if 'yes'in cheeze:
            driver.find_element_by_xpath('//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[2]/button/span').click()
            sleep(5)
        else:
            driver.find_element_by_xpath('//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
            sleep(5)




pizza()