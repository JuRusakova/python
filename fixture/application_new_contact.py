
from selenium import webdriver
from fixture.session_new_conact import SessionHelper
from fixture.group_new_contact import GroupHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_new_contact = SessionHelper(self)
        self.group_new_contact = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
