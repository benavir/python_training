from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(FirstName="Qaz", MiddleName="Wsx", LastName="QazWsx", Title="qwerty", Company="QAZqwerty", Address="Qwerty, 123"))
    app.session.logout()
