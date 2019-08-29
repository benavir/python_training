# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
    app.contact.home_page()
    app.contact.edit()
    app.contact.modify_first_contact(Contact(FirstName="New First name"))


def test_modify_contact_middle_name(app):
    app.contact.home_page()
    app.contact.edit()
    app.contact.modify_first_contact(Contact(MiddleName="New Middle name"))
