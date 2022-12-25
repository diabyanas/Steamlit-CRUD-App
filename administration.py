import db as dbConn
from resident import RH,Patient,aleatoires
import pandas as pd


class Archive:
    """Archivage """ 
    
    def __init__(self=None,identifiant_resident=None,date_entree=None,date_sortie=None):
        self.identifiant_resident = identifiant_resident
        self.date_entree = date_entree
        self.date_sortie = date_sortie

    # Archives ##########################
    def enregister_en_base():
        pass

    @staticmethod
    def afficher_les_archives_console():
        req = "select * from archives"
        con = dbConn.Connection()
        con.cur.execute(req)

    
    def afficher_les_archives_streamlit(self):
        req = "select * from archives"
        con = dbConn.Connection()
        con.cur.execute(req)
        result = con.cur.fetchall()
        data = pd.DataFrame(result,columns=['Identifiant Resident','Date Entree','Date Sortie'])
        return data


    # Patient ###########################
    def entrer_a_l_hopital():
        Patient.entrer_a_l_hopital()
        

    def sortir_de_l_hopital():
        Patient.sortir_de_l_hopital()

    def patient_aleatoire():
        aleatoires.patient_aleatoire()

    
    # RH ################################
    def debuter_CDD_CDI():
        RH.debuter_CDD_CDI()

    def quitter_CDD_CDI():
        RH.quitter_CDD_CDI()



































