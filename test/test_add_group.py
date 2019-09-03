# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create()
    app.group.fill(Group(name="qwerty", header="qwerty", footer="qwertyqwerty"))
    app.group.submit()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create()
    app.group.fill(Group(name="", header="", footer=""))
    app.group.submit()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
