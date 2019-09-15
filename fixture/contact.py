from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    def fill(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.FirstName)
        self.change_field_value("middlename", contact.MiddleName)
        self.change_field_value("lastname", contact.LastName)
        self.change_field_value("title", contact.Title)
        self.change_field_value("company", contact.Company)
        self.change_field_value("address", contact.Address)

    def update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cash = None

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cash = None

    def delete(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cash = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # fill contact form
        self.fill(new_contact_data)
        # submit modification
        self.update()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//tr[@name='entry']/td[@class='center']/a/img[@alt='Edit']")[index].click()
        # fill contact form
        self.fill(new_contact_data)
        # submit modification
        self.update()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()
#            wd.get("http://localhost/addressbook/index.php")

    def count(self):
        wd = self.app.wd
        self.home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.home_page()
            self.contact_cash = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                adress = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_emails = cells[4].text.splitlines()
                all_phones = cells[5].text.splitlines()
                self.contact_cash.append(Contact(FirstName=firstname, LastName=lastname, Address=adress, id=id,
                                                 email=all_emails[0], email2=all_emails[1], email3=all_emails[2],
                                                 homephone=all_phones[0], mobilephone=all_phones[1],
                                                 workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cash)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(FirstName=firstname, LastName=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

'''
    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.home_page()
            self.contact_cash = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                text = element.find_element_by_xpath("td[3]").text
                text_last = element.find_element_by_xpath("td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cash.append(Contact(FirstName=text, LastName=text_last, id=id))
        return list(self.contact_cash)
'''