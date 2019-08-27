# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create()
    app.contact.fill(Contact(FirstName="First", MiddleName="Middle", LastName="Last", Title="TitleTest", Company="CompanyTest", Address="TestAddress, 1"))
    app.contact.submit()
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create()
    app.contact.fill(Contact(FirstName="", MiddleName="", LastName="", Title="", Company="", Address=""))
    app.contact.submit()
    app.session.logout()
