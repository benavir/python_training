def test_delete_first_contact(app):
    app.contact.home_page()
    app.contact.delete()
