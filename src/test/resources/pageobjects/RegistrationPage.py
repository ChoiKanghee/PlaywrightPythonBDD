from common.BasePage import BasePage


class RegistrationPage(BasePage):

    def __init__(self,page):
        super().__init__(page)


    def open(self,url):
        self.navigate_to(url)

    def set_name(self,name):
        self.type("name_XPATH",name)

    def set_phone_number(self,phoneNum):
        self.type("phone_XPATH",phoneNum)

    def set_email(self,email):
        self.type("email_XPATH",email)

    def set_country(self,set_country):
        self.select("country_XPATH",set_country)

    def set_city(self,city):
        self.type("city_XPATH",city)

    def set_username(self,username):
        self.type("username_XPATH",username)


    def set_password(self,password):
        self.type("password_XPATH",password)

    def submit_form(self):
        self.click("submit_XPATH")