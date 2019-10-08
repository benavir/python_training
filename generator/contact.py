from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
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
#    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(FirstName="", MiddleName="", LastName="", Title="", Company="", Address="",
                    homephone="", mobilephone="", workphone="", secondaryphone="", email="", email2="", email3="")] + [
    Contact(FirstName=random_string("First", 5), MiddleName=random_string("Middle", 5), LastName=random_string("Last", 5),
            Title=random_string("TitleTest", 10), Company=random_string("CompanyTest", 10), Address=random_string("TestAddress, 1", 10),
            homephone=random_phone("+7(495)", 10), mobilephone=random_phone("+7", 10),
            workphone=random_phone("+7(495)", 10), secondaryphone=random_phone("+7", 10),
            email=random_string("email", 5), email2=random_string("email", 5), email3=random_string("email", 5))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
