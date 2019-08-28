# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit()
    app.contact.modify_first_contact(Contact(FirstName="New First name"))
    app.session.logout()


def test_add_contact_middle_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit()
    app.contact.modify_first_contact(Contact(MiddleName="New Middle name"))
    app.session.logout()
