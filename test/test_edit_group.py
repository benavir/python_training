from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill(Group(name="test"))
        app.group.submit()
        app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.edit()
    app.group.fill(Group(name="QAZ", header="wsx", footer="QAZwsxQAZ"))
    app.group.update()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)