from model.group import Group


def test_edit_first_group(app):
    app.group.edit()
    app.group.fill(Group(name="QAZ", header="wsx", footer="QAZwsxQAZ"))
    app.group.update()
