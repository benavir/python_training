from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.home_page()
    app.contact.edit()
    app.contact.fill(Contact(FirstName="Qaz", MiddleName="Wsx", LastName="QazWsx", Title="qwerty", Company="QAZqwerty", Address="Qwerty, 123"))
    app.contact.update()
