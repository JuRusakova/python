from selenium.webdriver.support.ui import Select

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

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
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
        self.change_field_value("work", cont.workphon)
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


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select first cotact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # allert
        wd.switch_to.alert.accept()


    def delete_all_contacts(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select all cotact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # allert
        wd.switch_to.alert.accept()