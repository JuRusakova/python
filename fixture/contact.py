from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re
from selenium.webdriver.common.by import By
class ContactHelper:


    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_no_clear(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, cont):
        wd = self.app.wd
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(cont)
        # submit new contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.home_page_cont()
        return len(wd.find_elements_by_name("selected[]"))

    def fill_contact_form(self, cont):
        wd = self.app.wd
        self.change_field_value("firstname", cont.firstname)
        self.change_field_value("middlename", cont.middlename)
        self.change_field_value("lastname", cont.lastname)
        self.change_field_value("nickname", cont.nickname)
        self.change_field_value("title", cont.title)
        self.change_field_value("company", cont.company)
        self.change_field_value("address", cont.address)
        self.change_field_value("home", cont.home)
        self.change_field_value("mobile", cont.mobile)
        self.change_field_value("work", cont.workphone)
        self.change_field_value("fax", cont.fax)
        self.change_field_value("email", cont.email)
        self.change_field_value("email2", cont.email2)
        self.change_field_value("email3", cont.email3)
        self.change_field_value("homepage", cont.homepage)
        self.change_field_value_no_clear("bday", cont.bday)
        self.change_field_value_no_clear("bmonth", cont.bmonth)
        self.change_field_value("byear", cont.byear)
        self.change_field_value_no_clear("aday", cont.aday)
        self.change_field_value_no_clear("amonth", cont.amonth)
        self.change_field_value("ayear", cont.ayear)
        self.change_field_value("address2", cont.address2)
        self.change_field_value("phone2", cont.phone2)
        self.change_field_value("notes", cont.notes)


    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.home_page_cont()
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.home_page_cont()
        # select first contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # allert
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None


    def delete_all_contacts(self):
        wd = self.app.wd
        self.home_page_cont()
        # select all cotact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # allert
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def home_page_cont(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/") > 0:
            wd.find_element_by_link_text("home").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.home_page_cont()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones ))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id = id, home = homephone, mobile=mobilephone, workphone=workphone, phone2=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, mobile=mobilephone, workphone=workphone, phone2=secondaryphone)





