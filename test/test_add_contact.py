# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.create_contact(Contact(firstname="Fill", middlename="Midd", lastname="Last", title="Title", company="Com", address="Address", home="1", mobile="2", workphon="3", fax="4", email="e", email2="e2", email3="e3",
                                           homepage= "home", bday= "7", bmonth= "July", byear= "1990", aday="12", ayear="2010", amonth="February", address2= "ADDRESS", phone2= "Home", notes="Notes",
                                           nickname="Nivada"))
    app.session.logout()


