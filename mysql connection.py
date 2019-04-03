import mysql.connector
from mysql.connector import errorcode

def test():
    try:
        db = mysql.connector.connect( host = '127.0.0.1',
                                      user = 'root',
                                      passwd = 's1mGzi6JZz4W^su',
                                      database = 'test')
       
        mycursor = db.cursor()
##        q1 = "INSERT INTO discordMembers (userid, warn) VALUES (6543234567, 0);"
##        mycursor.execute(q1)
##        db.commit()
##        
##        q2 = "UPDATE discordMembers SET warn = '3' WHERE userID = 2345678909876543"
##        mycursor.execute(q2)
##        db.commit()
##        q3 = "DELETE FROM discordMembers WHERE userid = 559929852808134666"
##        mycursor.execute(q3)
##        db.commit()
        q4 = "SELECT warn FROM discordMembers;"
        mycursor.execute(q4)
        data = mycursor.fetchone()[0]
        db.close()
        return data

    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)

print(test())

