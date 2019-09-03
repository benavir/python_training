# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
    app.contact.home_page()
    if app.contact.count() == 0:
        app.contact.create()
        app.contact.fill(Contact(FirstName="Test"))
        app.contact.submit()
    old_contacts = app.contact.get_contact_list()
    app.contact.edit()
    app.contact.modify_first_contact(Contact(FirstName="New First name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


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
