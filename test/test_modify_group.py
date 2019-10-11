from model.group import Group
import random


def test_modify_group_name(app, db, json_groups, check_ui):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create()
        app.group.fill(Group(name="test"))
        app.group.submit()
        app.group.open_groups_page()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = new_groups[index]
    # assert len(old_groups) == len(new_groups)
    old_groups[index] = new_groups[index]
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


'''
def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill(Group(header="test"))
        app.group.submit()
        app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.edit()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
'''
