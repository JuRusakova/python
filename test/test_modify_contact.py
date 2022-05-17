from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.group.count_cont() == 0:
        app.group.create_contact(Contact(firstname="test new contact"))
    app.group.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_contact_middlname(app):
    if app.group.count_cont() == 0:
        app.group.create_contact(Contact(firstname="test new contact"))
    app.group.modify_first_contact(Contact(middlename="New middlname"))

