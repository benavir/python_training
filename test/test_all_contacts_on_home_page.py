import re
from model.contact import Contact
# from fixture.orm import ORMFixture


def test_info_contacts_on_home_page(app, db, orm):
    app.contact.home_page()
    #if len(db.get_contact_list()) == 0:
    if len(orm.get_contact_list()) == 0:
        app.contact.create()
        app.contact.fill(Contact(FirstName="Test", LastName="Test", Address="adress1",
                                 homephone="111-111", mobilephone="8(800)000-00-00", workphone="22-22-22", secondaryphone="+79000007788",
                                 email="email1@email.ru", email2="email2@email.ru", email3="email3@email.ru"))
        app.contact.submit()
    contacts_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    # db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    #contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    for c in contacts_from_db:
        c.all_phones_from_home_page = merge_phones_like_on_home_page(c)
        c.all_emails_from_home_page = merge_emails_like_on_home_page(c)
    list_of_phones_from_db = []
    list_of_emails_from_db = []
    list_of_phones_from_home_page = []
    list_of_emails_from_home_page = []
    for i in range(0, len(contacts_from_db)):
        list_of_phones_from_db.append(contacts_from_db[i].all_phones_from_home_page)
        list_of_emails_from_db.append(contacts_from_db[i].all_emails_from_home_page)
        list_of_phones_from_home_page.append(contacts_from_homepage[i].all_phones_from_home_page)
        list_of_emails_from_home_page.append(contacts_from_homepage[i].all_emails_from_home_page)
    assert contacts_from_db == contacts_from_homepage
    assert list_of_phones_from_db == list_of_phones_from_home_page
    assert list_of_emails_from_db == list_of_emails_from_home_page


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))