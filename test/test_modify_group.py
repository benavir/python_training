from model.group import Group
from random import randrange


def test_modify_group_name(app, json_groups):
    group = json_groups
    if app.group.count() == 0:
        app.group.create()
        app.group.fill(Group(name="test"))
        app.group.submit()
        app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
#    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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
