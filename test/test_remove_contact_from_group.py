from model.contact import Contact
from model.group import Group
import random


def test_info_contacts_on_home_page(app, db, orm):

    if len(db.get_contact_list()) == 0:
        app.contact.create()
        app.contact.fill(Contact(FirstName="Test", LastName="Test", Address="adress1",
                                 homephone="111-111", mobilephone="8(800)000-00-00", workphone="22-22-22", secondaryphone="+79000007788",
                                 email="email1@email.ru", email2="email2@email.ru", email3="email3@email.ru"))
        app.contact.submit()

    if len(db.get_group_list()) == 0:
        app.group.create()
        app.group.fill(Group(name="test_group"))
        app.group.submit()
        app.group.return_to_home_page()
    # Выбрать рандомный контакт и подготовить список всех групп
    all_groups = orm.get_group_list()
    contact = random.choice(orm.get_contact_list())
    groups_with_contact = []
    for group in all_groups:
        if len(orm.get_contacts_in_group(group)) != 0:
            groups_with_contact.append(group)
    # Если нет, то добавить
    if len(groups_with_contact) == 0:
        group = random.choice(all_groups)
        app.contact.add_contact_to_group_by_id(contact.id, group.id)
        groups_with_contact.append(group)
    # Выбрать группу и соответствующий контакт для удаления
    group = random.choice(groups_with_contact)
    contact = random.choice(orm.get_contacts_in_group(group))
    # Удалить контакт из группы
    app.contact.remove_contact_from_group_by_id(contact.id, group.id)
    # Проверить, что контакт удален
    if orm.check_if_contact_is_in_group(group, contact):
        raise Exception('Contact was not deleted from group')
