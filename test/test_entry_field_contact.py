import re
from random import randrange
from model.contact import Contact

def test_entry_field_contact(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def test_db_matces_ui_contact(app,db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Testing", lastname="testing"))
    contacts_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_db = sorted(db.get_contact_list_all(), key=Contact.id_or_max)
    assert sorted(contacts_ui, key=Contact.id_or_max) == sorted(contacts_db, key=Contact.id_or_max)
    for i in range(len(contacts_ui)):
        assert contacts_ui[i].lastname == contacts_db[i].lastname
        assert contacts_ui[i].firstname == contacts_db[i].firstname
        assert contacts_ui[i].address == contacts_db[i].address
        assert contacts_ui[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_db[i])
        assert contacts_ui[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_db[i])

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.home, contact.mobile, contact.workphone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))