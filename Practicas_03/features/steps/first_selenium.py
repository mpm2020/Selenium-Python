from behave import *
@given('I open seleniumframework website')
def step_impl(context):
   context.browser.get("http://www.seleniumframework.com")
@then('I print the title')
def step_impl(context):
   title = context.browser.title
   print(title)
   assert "Selenium Framework" in title