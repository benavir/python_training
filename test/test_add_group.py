# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create()
    app.group.fill(Group(name="qwerty", header="qwerty", footer="qwertyqwerty"))
    app.group.submit()


def test_add_empty_group(app):
    app.group.create()
    app.group.fill(Group(name="", header="", footer=""))
    app.group.submit()
