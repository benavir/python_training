import re
from random import randrange
from model.contact import Contact


def test_phones_on_home_page(app):
    equal_contacts = app.contact.get_contact_list()
    index = randrange(len(equal_contacts))
    contact = Contact(FirstName="firstname", LastName="lastname", Address="adress",
                      email="all_emails"[0], email2="all_emails"[1], email3="all_emails"[2],
                      homephone="all_phones"[0], mobilephone="all_phones"[1],
                      workphone="all_phones"[2], secondaryphone="all_phones"[3])
    contact.id = equal_contacts[index].id
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.email == contact_from_edit_page.email
    assert contact_from_home_page.email2 == contact_from_edit_page.email2
    assert contact_from_home_page.email3 == contact_from_edit_page.email3
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)
