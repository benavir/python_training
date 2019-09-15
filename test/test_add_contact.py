# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(FirstName="", MiddleName="", LastName="", Title="", Company="", Address="")] + [
    Contact(FirstName=random_string("First", 5), MiddleName=random_string("Middle", 5), LastName=random_string("Last", 5),
            Title=random_string("TitleTest", 10), Company=random_string("CompanyTest", 10),
            Address=random_string("TestAddress, 1", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    pass
    old_contacts = app.contact.get_contact_list()
    app.contact.create()
    app.contact.fill(contact)
    app.contact.submit()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

