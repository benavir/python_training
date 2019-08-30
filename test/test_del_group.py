from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill(Group(name="test"))
        app.group.submit()
        app.group.open_groups_page()
    app.group.delete()
