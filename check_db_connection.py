# import pymysql.cursors
from fixture.orm import ORMFixture


# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
#    groups = db.get_group_list()
    l = db.get_contact_list()
    # l = db.get_group_list()
    for item in l:
        print(item)
    print(len(l))
    '''
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
    '''
finally:
    pass
#    connection.close()
#    db.destroy()
