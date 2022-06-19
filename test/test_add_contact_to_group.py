import random
import data.contacts
import data.groups



def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(data.contacts.testdata[0])
    if len(db.get_group_list()) == 0:
        app.group.create(data.groups.testdata[0])
    if len(db.get_contact_not_in_group()) == 0:
        app.contact.create(data.contacts.testdata[0])
    if len(db.get_group_without_contacts()) == 0:
        app.group.create(data.groups.testdata[0])
    group = random.choice(db.get_group_without_contacts())
    contact = random.choice(db.get_contact_not_in_group())
    old_contact_list_in_group = db.get_contact_in_group()
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    new_contact_list_in_group = db.get_contact_in_group()
    assert len(old_contact_list_in_group) +1 == len(new_contact_list_in_group)



