from model.contact import Contact


def test_delete_first_contact(app):
   if app.group.count_cont() == 0:
      app.group.create_contact(Contact(firstname="test new contact"))
   app.group.delete_first_contact()



