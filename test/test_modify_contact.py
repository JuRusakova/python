from model.contact import Contact


def test_modify_contact_firstname(app):
    app.group.modify_first_contact(Contact(firstname="New firstname"))

#def test_modify_contact_middlname(app):
    #app.group.modify_first_contact(Contact(middlename="New middlname")