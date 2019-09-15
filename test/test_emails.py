import re
from random import randrange


def test_emails_on_home_page(app):
    index = select_random_contact(app)
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def select_random_contact(app):
    equal_emails_on_home_page = app.contact.get_contact_list()
    index = randrange(len(equal_emails_on_home_page))
    return index


def test_emails_on_contact_view_page(app):
    index = select_random_contact(app)
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.email == contact_from_edit_page.email
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join([contact.email, contact.email2, contact.email3])
