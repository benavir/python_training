from sys import maxsize


class Contact:

    def __init__(self, FirstName=None, MiddleName=None, LastName=None, id=None,
                 Title=None, Company=None, Address=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None):
        self.FirstName = FirstName
        self.MiddleName = MiddleName
        self.LastName = LastName
        self.Title = Title
        self.Company = Company
        self.Address = Address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.FirstName, self.LastName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.FirstName == other.FirstName and self.LastName == other.LastName

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
