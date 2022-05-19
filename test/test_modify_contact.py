from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count_cont() == 0:
        app.contact.create(Contact(firstname="test new contact"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_contact_middlname(app):
    if app.contact.count_cont() == 0:
        app.contact.create(Contact(firstname="test new contact"))
    app.contact.modify_first_contact(Contact(middlename="New middlname"))

