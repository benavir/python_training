from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit()
    app.group.fill_group_form(Group(name="QAZ", header="wsx", footer="QAZwsxQAZ"))
    app.group.update_group()
    app.session.logout()
