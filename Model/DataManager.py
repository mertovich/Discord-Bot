import sqlite3
# MARK - Creat and Add data
def addData(Name,Date,Age,User_Id):
    db = sqlite3.connect('ServerUserData.db')
    im = db.cursor()
    im.execute("CREATE TABLE IF NOT EXISTS User (name, date, age, user_Id)")
    insertData = f'''INSERT INTO User VALUES ("{Name}", "{Date}", "{Age}", "{User_Id}")'''
    im.execute(insertData)
    db.commit()
    db.close()
# MARK - Shows the information of all registered users in the database
def getUserAllData():
    db = sqlite3.connect('ServerUserData.db')
    im = db.cursor()
    im.execute("""SELECT * FROM User""")
    data = im.fetchall()
    db.close()
    return data
# MARK - Returns the user matching the entered user id
def getUser(user_Id):
    db = sqlite3.connect('ServerUserData.db')
    im = db.cursor()
    im.execute(f'''SELECT * FROM User WHERE user_Id = "{user_Id}"''')
    data = im.fetchall()
    db.close()
    return data