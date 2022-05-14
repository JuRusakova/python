
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group2):
        wd = self.app.wd
        self.open_group_page()
        #init create group
        wd.find_element_by_name("new").click()
        #fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group2.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group2.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group2.footer)
        #submit group creation
        wd.find_element_by_name("submit").click()
        self.return_group_page()


    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
