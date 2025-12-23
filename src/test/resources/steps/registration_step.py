import time
from behave import given, when, then

from Utilities import configReader
from pageobjects.RegistrationPage import RegistrationPage


@given("I navigate to qa.way2automation.com")
def step_navigate(context):
    context.reg = RegistrationPage(context.page)
    context.reg.open(configReader.readConfig("basic info", "testsiteurl"))


@when('I enter the name as "{name}"')
def step_enter_name(context, name):
    context.reg.set_name(name)


@when('I enter the phone number as "{phonenumber}"')
def step_enter_phone(context, phonenumber):
    context.reg.set_phone_number(phonenumber)


@when('I enter the email as "{email}"')
def step_enter_email(context, email):
    context.reg.set_email(email)


@when('I enter the country as "{country}"')
def step_enter_country(context, country):
    context.reg.set_country(country)


@when('I enter the city as "{city}"')
def step_enter_city(context, city):
    context.reg.set_city(city)


@when('I enter the username as "{username}"')
def step_enter_username(context, username):
    context.reg.set_username(username)


@when('I enter the password as "{password}"')
def step_enter_password(context, password):
    context.reg.set_password(password)


@when("I click on the submit button")
def step_click_submit(context):
    context.reg.submit_form()
    time.sleep(3)  # tạm để nhìn UI


# Optional: demo step
@given("i login to page")
def step_login(context):
    pass
