from selenium import webdriver
from secrets import phone
from time import sleep


class TinderBot():

    def __init__(self):
        self.driver = webdriver.Chrome()

        sleep(2)

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(3)

        # accept cookies modal
        cookies_btn = self.driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div/div[1]/div/button")
        cookies_btn.click()

        sleep(3)

        # close modal popup
        modal_btn = self.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/button")
        modal_btn.click()
        
        sleep(2)

        # select signup button
        signup_btn = self.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/main/div[1]/div/div/div/div[4]/div[1]/button") 
        signup_btn.click()

        # login with phone
        try:
            ph_btn = bot.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/span/div[1]/button")
            ph_btn.click()
        except Exception:
            options_btn = bot.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/span/button")
            options_btn.click()
            sleep(3)
            ph_btn = bot.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/span/div[3]/button")
            ph_btn.click()
        
        sleep(2)

        ph_in = bot.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/div[2]/div/input")
        ph_in.send_keys(phone)

        sleep(2)

        ph_submit = ph_submit = bot.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/button")
        ph_submit.click()

        # prompt user for otp
        otp = input("OTP: ")
        otp = [d for d in otp]

        otp1 = self.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/div[3]/input[1]")
        otp2 = self.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/div[3]/input[2]")
        otp3 = self.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/div[3]/input[3]")
        otp4 = self.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/div[3]/input[4]")
        otp5 = self.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/div[3]/input[5]")
        otp6 = self.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/div[3]/input[6]")

        otp1.send_keys(otp[0])
        sleep(1)
        otp2.send_keys(otp[1])
        sleep(1)
        otp3.send_keys(otp[2])
        sleep(1)
        otp4.send_keys(otp[3])
        sleep(1)
        otp5.send_keys(otp[4])
        sleep(1)
        otp6.send_keys(otp[5])
        sleep(1)

        try:
            otp_submit = self.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/button")
            otp_submit.click()
        except Exception:
            return "Please enter valid OTP!"

        # close popups after login
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()


    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()











# Chrome version: 80.0.3987.163