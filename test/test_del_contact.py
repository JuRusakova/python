from model.contact import Contact


def test_delete_first_contact(app):
   if app.contact.count_cont() == 0:
      app.contact.create(Contact(firstname="test new contact"))
   app.contact.delete_first_contact()



