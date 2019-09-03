from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.home_page()
    if app.contact.count() == 0:
        app.contact.create()
        app.contact.fill(Contact(FirstName="Test"))
        app.contact.submit()
    old_contacts = app.contact.get_contact_list()
    app.contact.edit()
    app.contact.fill(Contact(FirstName="Qaz", MiddleName="Wsx", LastName="QazWsx", Title="qwerty", Company="QAZqwerty", Address="Qwerty, 123"))
    app.contact.update()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)