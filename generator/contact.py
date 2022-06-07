from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", title="", company="", address="",
            home="", mobile="", workphone="", fax="", email="", email2="", email3="",
            homepage="", bday="", bmonth="", byear="", aday="", ayear="", amonth="",
            address2="", phone2="", notes="", nickname="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 15), lastname=random_string("lastname", 15),
            nickname=random_string("nickname", 10), title=random_string("title", 15), company=random_string("company", 20), address=random_string("address", 10),
            home=random_string("58", 15), mobile=random_string("5828", 15), workphone=random_string("wrkph", 15), fax=random_string("fax", 15),
            email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20),
            homepage=random_string("homepage", 20), bday="7", bmonth= "July", byear= "1990", aday="12", ayear="2010", amonth="February",
            address2=random_string("address2", 10), phone2=random_string("phone2", 20), notes=random_string("notes", 20))
    for i in range(n)
    ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))