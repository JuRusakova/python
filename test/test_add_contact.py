# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", title="", company="", address="",
            home="", mobile="", workphone="", fax="", email="", email2="", email3="",
            homepage="", bday="", bmonth="", byear="", aday="", ayear="", amonth="",
            address2="", phone2="", notes="", nickname="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 15), lastname=random_string("lastname", 15),
            nickname=random_string("nickname", 10), title=random_string("title", 15), company=random_string("company", 20), address=random_string("address", 10),
            home=random_string("58", 15), mobile=random_string("5828", 15), workphone=random_string("wrkph", 15), fax=random_string("fax", 15),
            email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20),
            homepage=random_string("homepage", 20), bday= "7", bmonth= "July", byear= "1990", aday="12", ayear="2010", amonth="February",
            address2=random_string("address2", 10), phone2=random_string("phone2", 20), notes=random_string("notes", 20))
    for i in range(5)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)






