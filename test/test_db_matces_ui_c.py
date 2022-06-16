
from model.contact import Contact

def test_contact_list(app,db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Testing", lastname="testing"))
    contacts_ui = app.contact.get_contact_list()
    contacts_db = db.get_contact_list_all()
    assert sorted(contacts_ui, key=Contact.id_or_max) == sorted(contacts_db, key=Contact.id_or_max)