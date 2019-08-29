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

    def edit(self):
        wd = self.app.wd
        self.select_first_contact()
        # push the button "Edit contact"
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def delete(self):
        wd = self.app.wd
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

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
        wd.find_element_by_link_text("home").click()
