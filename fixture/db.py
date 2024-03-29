import pymysql.cursors
from model.group import Group
from model.contact import Contact
from model.C_in_g import CinG


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_list_all(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, workphone, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, email=email, email2=email2,
                       email3=email3, home=home, mobile=mobile, workphone=workphone, phone2=phone2))
        finally:
            cursor.close()
        return list

    def get_contact_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                list.append(Group(id=str(group_id)))
        finally:
            cursor.close()
        return list

    def get_contact_not_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                'select id, firstname, lastname FROM addressbook where id not in (SELECT id from address_in_groups)')
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_group_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name FROM group_list where group_id in "
                           "(SELECT group_id from address_in_groups)")
            for row in cursor:
                (group_id, group_name) = row
                list.append(Group(id=group_id, name=group_name))
        finally:
            cursor.close()
        return list

    def get_group_without_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name FROM group_list where group_id not in "
                           "(SELECT group_id from address_in_groups)")
            for row in cursor:
                (group_id, group_name) = row
                list.append(Group(id=group_id, name=group_name))
        finally:
            cursor.close()
        return list

    def get_contacts_in_groups_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(CinG(id=id, group_id=group_id))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()