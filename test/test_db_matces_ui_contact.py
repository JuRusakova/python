
from model.contact import Contact

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
        assert contacts_ui[i].all_email_from_home_page == merge_email_like_on_home_page(contacts_db[i])
        assert contacts_ui[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_db[i])

    def merge_phones_like_on_home_page(contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home, contact.mobile, contact.workphone, contact.phone2]))))

    def merge_emails_like_on_home_page(contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))