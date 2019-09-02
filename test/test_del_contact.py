from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.home_page()
    if app.contact.count() == 0:
        app.contact.create()
        app.contact.fill(Contact(FirstName="Test"))
        app.contact.submit()
    app.contact.delete()
