
import data.groups
import data.contacts
import random


def test_del_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(data.contacts.testdata[0])
    if len(db.get_group_list()) == 0:
        app.group.create(data.groups.testdata[0])
    if len(db.get_contacts_in_groups_list()) == 0:
        contact = random.choice(db.get_contacts_not_in_any_group())
        group = random.choice(db.get_group_without_contacts())
        app.contact.add_contact_to_group_by_id(contact.id, group.name)
    contact = random.choice(db.get_contact_in_group())
    group = random.choice(db.get_group_with_contacts())
    old_contact_list = db.get_contact_not_in_group()
    app.contact.delete_contact_from_group_by_id(contact.id, group.id)
    new_contact_list = db.get_contact_not_in_group()
    assert len(old_contact_list) + 1 == len(new_contact_list)