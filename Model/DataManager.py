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