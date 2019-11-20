from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


def test_info_contacts_on_home_page(app, db, orm):
    # if len(db.get_contact_list()) == 0:
    if len(orm.get_contact_list()) == 0:
        app.contact.create()
        app.contact.fill(Contact(FirstName="Test", LastName="Test", Address="adress1",
                                 homephone="111-111", mobilephone="8(800)000-00-00", workphone="22-22-22", secondaryphone="+79000007788",
                                 email="email1@email.ru", email2="email2@email.ru", email3="email3@email.ru"))
        app.contact.submit()
    # if len(db.get_group_list()) == 0:
    if len(orm.get_group_list()) == 0:
        app.group.create()
        app.group.fill(Group(name="test_group"))
        app.group.submit()
        app.group.return_to_home_page()
    # list_of_contacts = db.get_contact_list()
    # list_of_groups = db.get_group_list()
    list_of_contacts = orm.get_contact_list()
    list_of_groups = orm.get_group_list()
    contact = random.choice(list_of_contacts)

    # Проверить, в каких группах контакт не состоит
    groups_without_contact = []
    for group in list_of_groups:
        if not orm.check_if_contact_is_in_group(group, contact):
            groups_without_contact.append(group)
    # Если контакт входит во все группы, то создать новую группу
    if len(groups_without_contact) == 0:
        app.group.create()
        app.group.fill(Group(name="test_group"))
        app.group.submit()
        app.group.return_to_home_page()
        groups_without_contact = orm.get_group_list()
    # Выбрать группу из списка групп без контакта
    group = groups_without_contact[-1]
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    contacts_in_group_from_group_page = sorted(app.contact.get_contact_list_in_group(), key=Contact.id_or_max)
    # db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    # contacts_in_group_from_db = sorted(db.get_contacts_in_group(group), key=Contact.id_or_max)
    contacts_in_group_from_db = sorted(orm.get_contacts_in_group(group), key=Contact.id_or_max)
    assert contacts_in_group_from_db == contacts_in_group_from_group_page
