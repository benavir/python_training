from model.contact import Contact
from random import randrange


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create()
        app.contact.fill(Contact(FirstName="Test"))
        app.contact.submit()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(FirstName="New First name")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


'''
def test_modify_contact_middle_name(app):
    app.contact.home_page()
    if app.contact.count() == 0:
        app.contact.create()
        app.contact.fill(Contact(MiddleName="Test"))
        app.contact.submit()
    old_contacts = app.contact.get_contact_list()
    app.contact.edit()
    app.contact.modify_first_contact(Contact(MiddleName="New Middle name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
'''