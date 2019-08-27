# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create()
    app.group.fill(Group(name="qwerty", header="qwerty", footer="qwertyqwerty"))
    app.group.submit()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create()
    app.group.fill(Group(name="", header="", footer=""))
    app.group.submit()
    app.session.logout()
