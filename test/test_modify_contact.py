from model.contact import Contact
import random


def test_modify_contact_first_name(app, db, json_contacts, check_ui):
    contact_data = json_contacts
    if len(db.get_contact_list()) == 0:
        app.contact.create()
        app.contact.fill(Contact(FirstName="Test", LastName="Test"))
        app.contact.submit()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    app.contact.modify_contact_by_id(contact.id, contact_data)
    new_contacts = db.get_contact_list()
    # assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = new_contacts[index]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


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