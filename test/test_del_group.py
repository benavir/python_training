from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill(Group(name="test"))
        app.group.submit()
        app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.delete()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
