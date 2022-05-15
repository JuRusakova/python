from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_contact(Contact(firstname="1", middlename="2", lastname="Last", title="3", company="Com", address="Address", home="1", mobile="2", workphon="3", fax="4", email="e", email2="e2", email3="e3",
                                           homepage= "home", bday= "10", bmonth= "July", byear= "1990", aday="12", ayear="2010", amonth="February", address2= "ADDRESS", phone2= "Home", notes="Notes",
                                           nickname="Nivada"))
    app.session.logout()