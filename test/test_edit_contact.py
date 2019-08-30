from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create()
        app.contact.fill(Contact(FirstName="Test"))
        app.contact.submit()
    app.contact.edit()
    app.contact.fill(Contact(FirstName="Qaz", MiddleName="Wsx", LastName="QazWsx", Title="qwerty", Company="QAZqwerty", Address="Qwerty, 123"))
    app.contact.update()
