from model.contact import Contact
import random
import string


constant = [
    Contact(FirstName="FirstName1", MiddleName="MiddleName1", LastName="LastName1"),
    Contact(FirstName="FirstName2", MiddleName="MiddleName2", LastName="LastName2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(FirstName="", MiddleName="", LastName="", Title="", Company="", Address="")] + [
    Contact(FirstName=random_string("First", 5), MiddleName=random_string("Middle", 5), LastName=random_string("Last", 5),
            Title=random_string("TitleTest", 10), Company=random_string("CompanyTest", 10),
            Address=random_string("TestAddress, 1", 10))
    for i in range(5)
]