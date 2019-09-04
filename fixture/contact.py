from model.contact import Contact


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

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cash = None

    def delete(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
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
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.home_page()
            self.contact_cash = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cash.append(Contact(id=id))
        return list(self.contact_cash)
