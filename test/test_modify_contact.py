# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create()
        app.contact.fill(Contact(FirstName="Test"))
        app.contact.submit()
    app.contact.edit()
    app.contact.modify_first_contact(Contact(FirstName="New First name"))


def test_modify_contact_middle_name(app):
    if app.contact.count() == 0:
        app.contact.create()
        app.contact.fill(Contact(MiddleName="Test"))
        app.contact.submit()
    app.contact.edit()
    app.contact.modify_first_contact(Contact(MiddleName="New Middle name"))
