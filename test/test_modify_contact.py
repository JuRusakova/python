from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    contact = Contact(firstname="New firstname", lastname="New lastname")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    contact_random = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact_random.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts_db = db.get_contact_list()
    new_contacts_ui = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts_db)
    if check_ui:
        assert sorted(new_contacts_db, key=Contact.id_or_max) == sorted(new_contacts_ui, key=Contact.id_or_max)

