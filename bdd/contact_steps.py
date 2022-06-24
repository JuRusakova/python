from pytest_bdd import given, when, then, parsers
from model.contact import Contact
import random


@given(parsers.parse('a contact list'), target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()


@given(parsers.parse('a contact with {firstname} and {lastname}'), target_fixture="new_contact")
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when(parsers.parse('I add the contact to the list'), target_fixture="add_new_contact")
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then(parsers.parse('the new contact list is equal to the old contact list with the added contact'), target_fixture="verify_contact_added")
def verify_contact_added(db, contact_list, new_contact, check_ui):
    old_contacts_list = contact_list
    new_contacts_list = db.get_contact_list()
    old_contacts_list.append(new_contact)
    assert sorted(new_contacts_list, key=Contact.id_or_max) == sorted(old_contacts_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.id_or_max) == sorted(db.get_contacts_list(), key=Contact.id_or_max)


@given(parsers.parse('a non-empty contact list'), target_fixture="non_empty_contact_list")
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='firstname1'))
    return db.get_contact_list()


@given(parsers.parse('a random contact from the list'), target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when(parsers.parse('I delete the contact from the list'), target_fixture="delete_contact")
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then(parsers.parse('the new contact list is equal to the old contact list without the deleted contact'), target_fixture="verify_group_deleted")
def verify_group_deleted(app, db, non_empty_contact_list, random_contact, check_ui):
    old_contacts_list = non_empty_contact_list
    new_contacts_list = db.get_contact_list()
    old_contacts_list.remove(random_contact)
    assert sorted(new_contacts_list, key=Contact.id_or_max) == sorted(old_contacts_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.id_or_max) ==\
               sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

@given(parsers.parse('new <firstname> and <lastname>'), target_fixture="contact_modified")
def contact_modified(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when(parsers.parse('I modify the contact from the list'), target_fixture="modify_contact_by_id")
def modify_contact_by_id(app, contact_modified, random_contact):
    app.contact.modify_contact_by_id(random_contact.id, contact_modified)


@then(parsers.parse('the new contact list is equal to the old contact list with the modified contact'), target_fixture="verify_contact_modified")
def verify_contact_modified(app, db, non_empty_contact_list, contact_modified, random_contact, check_ui):
    index = int(non_empty_contact_list.index(random_contact))
    contact_modified.id = random_contact.id
    non_empty_contact_list[index] = contact_modified
    old_contacts_list = non_empty_contact_list
    new_contacts_list = db.get_contact_list()
    assert sorted(new_contacts_list, key=Contact.id_or_max) == sorted(old_contacts_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)