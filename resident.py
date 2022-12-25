import db as dbConn
import pandas as pd
import names
from datetime import datetime
import random
import numpy as np

class RH:
    """Info RH"""
    def __init__(self,identifiant_rh=None, nom=None, prenom=None, salaire=None, working_at_hospital=None,date_recrutement=None):
        
        self.identifiant_rh = identifiant_rh
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.working_at_hospital = working_at_hospital
        self.date_recrutement = date_recrutement

    
    def save_rh_to_db(self):
        """
        Enregistrer les RH en base de données
        """
        try:
            con = dbConn.Connection()
            
            req = ("INSERT INTO rh (identifiant_rh,nom,prenom,salaire,working_at_hospital,date_recrutement) VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE identifiant_rh=values({self.identifiant_rh}),nom=values({self.nom}),prenom=values({self.prenom}),salaire=values({self.salaire}),groupe_sanguin=values({self.groupe_sanguin}),working_at_hospital=values({self.working_at_hospital}),date_recrutement=values({self.date_recrutement})")
            con.cur.execute(req)
            
            print("RH enrégistré en base")
        except:
             print("Quelques choses n'a pas marché, veillez vérifiez")

        finally:
           # Close the connection
           con.cur.close()
        
        
class Patient:

    def __init__(self=None,identifiant_patient=None, nom=None, prenom=None, groupe_sanguin=None, is_in_hospital=None, date_entree=None):
        
        self.identifiant_patient = identifiant_patient
        self.nom = nom
        self.prenom = prenom
        self.groupe_sanguin = groupe_sanguin
        self.is_in_hospital = is_in_hospital
        self.date_entree = date_entree
    
    
    def entrer_a_l_hopital(self):

        # Connexion BDD
        con = dbConn.Connection()
                
        try:
            #self.date_entree = date_entree
            query = "Insert Into CHU_Caen.patients(identifiant_patient, nom, prenom,groupe_sanguin,is_in_hospital, date_entree) Values(%s,%s,%s,%s,%s,%s)" 
            
            # Execute the sql query
            con.cur.execute(query, [self.identifiant_patient, self.nom, self.prenom, self.groupe_sanguin, self.is_in_hospital, self.date_entree])

            # Commit the data
            
            
            print('Patient enregistré avec succès')

        except:
                print("Quelques choses n'a pas marcher, veillez vérifiez")

        finally:
            # Close the connection
            con.cur.close()

    
    def sortir_de_l_hopital(self,identifiant_patient,date_entree):
        self.identifiant_patient = identifiant_patient
        self.date_entree = date_entree
        # Connexion BDD
        con = dbConn.Connection()
                
        try:
            # Archivage avant suppression de patients
            sql = "Insert Into CHU_Caen.archives (identifiant_resident, date_entree) Values(%s,%s)"  
            con.cur.execute(sql, [identifiant_patient, date_entree])

            query = "delete from CHU_Caen.patients where identifiant_patient = %s"
            con.cur.execute(query, [self.identifiant_patient])
            
            print('Patient supprimé avec succès')

        except:
            print("Quelques choses n'a pas marcher, veillez vérifiez")

        finally:
            # Close the connection
            con.cur.close()
    

    def count_patients_in_db(self):
        """
        Compte les patients inscrits en base de données
        """
        con = dbConn.Connection()
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(identifiant_patient) FROM patients")
    
    def afficher_les_patients_streamlit(self):
        req = "select * from patients"
        con = dbConn.Connection()
        con.cur.execute(req)
        result = con.cur.fetchall()
        data = pd.DataFrame(result,columns=['Identifiant Patient','Nom','Prenom','Groupe Sanguin','is_in_hospital','Date Entree'])
        return data


class RH:
    
    def __init__(self,identifiant_rh=None, nom=None, prenom=None,salaire=None,working_at_hospital=None, date_recrutement=None,groupe_sanguin=None):
    
        self.identifiant_rh = identifiant_rh
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.groupe_sanguin = groupe_sanguin
        self.working_at_hospital = working_at_hospital
        self.date_recrutement = date_recrutement
        
    def debuter_CDD_CDI(self):

        # Connexion BDD
        con = dbConn.Connection()
            
        try:
            query = "Insert Into CHU_Caen.rh (identifiant_rh, nom, prenom, salaire, working_at_hospital, date_recrutement,groupe_sanguin) Values(%s,%s,%s,%s,%s,%s,%s)" 
            
            #Execute the sql query
            con.cur.execute(query, [self.identifiant_rh, self.nom, self.prenom,self.salaire,self.working_at_hospital, self.date_recrutement,self.groupe_sanguin])
            print('RH enregistré avec succès')

        except:
                print("Quelques choses n'a pas marcher, veillez vérifiez")

        finally:
            # Close the connection
            con.cur.close()


    def quitter_CDD_CDI(self,identifiant_rh,date_recrutement):
        self.identifiant_rh = identifiant_rh
        self.date_recrutement = date_recrutement
        # Connexion BDD
        con = dbConn.Connection()
            
        try:
            sql = "Insert Into CHU_Caen.archives (identifiant_resident, date_entree) Values(%s,%s)"  
            con.cur.execute(sql, [identifiant_rh, date_recrutement])
            
            query = query = ("delete from rh where identifiant_rh = %s") 

            # Execute the sql query
            con.cur.execute(query, [identifiant_rh])
            print('RH supprimé avec succès')

        except:
                print("Quelques choses n'a pas marcher, veillez vérifiez")

        finally:
            # Close the connection
            con.cur.close()


    def afficher_rh_streamlit(self):
        req = "select * from rh"
        con = dbConn.Connection()
        con.cur.execute(req)
        result = con.cur.fetchall()
        data = pd.DataFrame(result,columns=['Identifiant RH','Nom','Prenom','Salaire','Working_at_hospital','Date Rment','Groupe Sanguin'])
        return data



class aleatoires:

    def random_dates():
        N = 3 #N-samples
        dates = np.zeros([N,3])

        for i in range(0,N):
            year = random.randint(2021, 2022) 
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            #if you need to change it use variables :3
            dates[i] = [year,month,day]

        df = pd.DataFrame(dates.astype(int))
        df.columns = ['year', 'month', 'day']
        date = pd.to_datetime(df)
        return date
    

    def groupe_sanguin():
        """Génération de groupe sanguin aléatoire"""
        items = ["O-","O+","A-","A+","B-","B+","AB-","AB+"]
        liste_groupe_sanguin = []
        for i in range(3):
            sang = random.choice(items)
            liste_groupe_sanguin.append(sang)
        return liste_groupe_sanguin


    def presence_hospital():
        """Indique de façon aléatoire la présence ou non du patient à l'hôpital"""
        is_in_hp = ["True","False"]
        is_in_hospital = []
        for i in range(3):
            hospital = random.choice(is_in_hp)
            is_in_hospital.append(hospital)
        return is_in_hospital


    def patient_aleatoire():
        """Génération de patients aléatoire en utilisant la fonction names"""

        is_in_hospital = aleatoires.presence_hospital()
        liste_groupe_sanguin = aleatoires.groupe_sanguin()
        date = aleatoires.random_dates()


        # Connexion BDD
        con = dbConn.Connection()

        # Gneneration de noms alétoires
        noms = []
        prenoms = []
        liste_nom = []
        for i in range(3):
            nom = names.get_full_name()
            n = nom.split(" ")
            liste_nom.append(n)
            i += 1
            
        for i in range(len(liste_nom)):
            noms.append(liste_nom[i][0])
            prenoms.append(liste_nom[i][1])

            try:
                """Insertion en Base de données"""
                identifiant_patient = (noms[i]+prenoms[i]+liste_groupe_sanguin[i]+str(date[i]))+"_PA"

                query = "Insert Into CHU_Caen.patients(identifiant_patient, nom, prenom,groupe_sanguin,is_in_hospital, date_entree) Values(%s,%s,%s,%s,%s,%s)" 
                
                # Execute the sql query
                con.cur.execute(query, [identifiant_patient, noms[i], prenoms[i], liste_groupe_sanguin[i], is_in_hospital[i], date[i]])
                
                print('Patient enregistré avec succès')

            except:
                    print("Quelques choses n'a pas marcher, veillez vérifiez")

            finally:
                # Close the connection
                con.cur.close()