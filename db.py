# Connexion BDD ####################
import mysql.connector as mysqlpy





class Connection:
    def __init__(self):
        self.db=mysqlpy.connect(user = 'root',password = 'example',host = 'localhost',port = '3307',database = 'CHU_Caen')
        self.db.autocommit=True
        #self.db.set_character_set('utf8mb4')
        self.cur=self.db.cursor(buffered=True)
        