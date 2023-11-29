import time
from random import randrange
from selenium import webdriver
import pandas as pd


global path_to_login, path_to_duration

path_to_login = 'login.csv'
path_to_duration = 'duration.txt'

class Website:
    def __init__(self, credentials='', driver='', duration=''):
        self.credentials = credentials
        self.driver = driver
        self.duration = duration
        

        if len(self.credentials) > 1:
            self.username = self.credentials[0]
            self.password = self.credentials[1]
       #     print(self.username, self.password,'f')
        else:
            pass


    def get_credentials(self):
        import csv

        credentials = open(path_to_login)
        credentials_csv = csv.reader(credentials)
        

        rows = []


        for row in credentials_csv:
            row.remove('')
            rows.append(row)

        return rows

        



    def ScrapeMain(self):
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.options import Options
       # print(self.username)
        import random



        
        

        #driver = webdriver.Chrome()
        #driver.get(self.website)

        action = ActionChains(self.driver) 


       # To Prevent Bot Detection
        time.sleep(randrange(5))

        email_box = driver.find_element(By.CLASS_NAME, "blocks-kddr16")
        time.sleep(randrange(1))
        email_box.send_keys(self.username)

        time.sleep(randrange(2))

        password_box = driver.find_element(By.CLASS_NAME, "blocks-fpd3nj")
        time.sleep(1)

        password_box.click()
        time.sleep(1)
       # print(self.password,'s')
        password_box.send_keys(str(self.password))
        time.sleep(2)

        ActionChains(driver).send_keys(Keys.ENTER).perform()

        

        #ScrapeLoop(self, duration_seconds)

        time.sleep(8)
        return 

    def GetDuration(self):
        from bs4 import BeautifulSoup
        return int(open(path_to_duration).read())



    def ScrapeLoop(self):
        from bs4 import BeautifulSoup
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys

        action = ActionChains(self.driver)


        posts_array = []


        for i in range(self.duration):
            print(i)

            for l in range(3):
                ActionChains(driver).send_keys(Keys.DOWN).perform()
                time.sleep(1)
            
            #current = time.time()
            
            posts_raw = driver.find_elements(By.CLASS_NAME, "blocks-16m6fnr")
            for post in posts_raw:
                posts_array.append(post.text)
               # print(post.text)

            #print(posts_array)


        #posts_array = list(dict.fromkeys(posts_array))

        print(posts_array)  

        return posts_array
        #return pd.DataFrame(posts_array, columns=[''])

            

            
                    








        



           


        
        







        


            
        




# Gets The Login Info From A Text File
login_info = Website('test2.csv').get_credentials()


data_total = set()

for profile in login_info:
    driver = webdriver.Chrome()
    driver.get('https://nextdoor.com')
    dur = Website().GetDuration()
    



    Website(profile, driver).ScrapeMain()

    time.sleep(randrange(2))

    
    data_part = set(Website(profile, driver, dur).ScrapeLoop())

    data_total.update(data_part)


    #output = open('output.txt', 'a')

    #print(str(data))

    #output.write(str(data))

    #full_data.append(data)




# Analysises the data


#ptim_data = pd.DataFrame(full_data, columns=['data'])


print(data_total)






   




    

    

















'''

random_time = randrange(5)

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('https://nextdoor.com');

time.sleep(random_time) # Let the user actually see something!


search_login = driver.find_element('id', 'id_email')



search_login.send_keys('julianformayor@protonmail.com')


search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
'''