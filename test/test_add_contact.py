# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_new_contact import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session_new_contact.login(username="admin", password="secret")
    app.group_new_contact.create_c(Contact(firstname="Fill", middlename="Midd", lastname="Last", title="Title", company="Com", address="Address", home="1", mobile="2", workphon="3", fax="4", email="e", email2="e2", email3="e3",
                                           homepage= "home", bday= "7", bmonth= "July", byear= "1990", aday="12", ayear="2010", amonth="February", address2= "ADDRESS", phone2= "Home", notes="Notes",
                                           nickname="Nivada"))
    app.session_new_contact.logout()


