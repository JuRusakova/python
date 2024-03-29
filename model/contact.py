from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, title=None, company=None, address=None,
                 home=None, mobile=None, workphone=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, ayear=None, amonth=None, address2=None,
                 phone2=None, notes=None, nickname=None, id = None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.ayear = ayear
        self.amonth = amonth
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.nickname = nickname
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s" % (self.id, self.firstname, self.lastname, self.address, self.email, self.email2, self.email3,
                             self.home, self.workphone, self.mobile, self.phone2)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize