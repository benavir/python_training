from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="QAZ", header="wsx", footer="QAZwsxQAZ"))
    app.session.logout()
