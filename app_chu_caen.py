# Core pkg
import streamlit as st
import administration as ad
from resident import RH,Patient
import resident as r

# EDA pkgs
#import pandas as pd

def main():
	#st.image('/home/diaby/IA_dev_Python/py-sql/Streamlit_CRUD/logo-chucaenbf.png', width=100)
	st.image(r'C:\Users\utilisateur\Documents\Microsoft_IA\Exercices\STREAMLIT_CRUD\logo-chucaenbf.png', width=100)
	#st.set_page_config(layout="wide")
	#st.title("RH CHU-CAEN")
	menu = st.sidebar.selectbox("Menu",["Ajout Patient","Suppression Patient","Ajout RH","Suppression RH","Patients Aléatoires","Archives"])
	#menu = ["Ajout Patient","Ajout RH","Affichage Console","Affichage Streamlit"]
	#choix = st.sidebar.selectbox("Menu",menu)
	if menu == "Ajout Patient":
		st.subheader("Mise à jour de Données Patient")
		# Layout
		col1, col2 = st.columns(2)
		with col1:
			nom = st.text_input("Nom")
			prenom = st.text_input("Prenom")
			date_entree = st.date_input("Date Entree")
			
			
		with col2:
			groupe_sanguin = st.selectbox("Groupe Sanguin",["O-","O+","A-","A+","B-","B+","AB-","AB+"])
			is_in_hospital = st.selectbox("Présence à l'hospital",["False","True"])
			espace = st.text_input("")
			
			if st.button("Mettre à Jour"):
				identifiant_patient = (nom+prenom+groupe_sanguin+str(date_entree))+" 00:00:00_PA"
				
				patient = ad.Patient(identifiant_patient, nom, prenom, groupe_sanguin, is_in_hospital, str(date_entree))
				patient.entrer_a_l_hopital()
				#ad.Patient.entrer_a_l_hopital(identifiant_patient, nom, prenom, groupe_sanguin, is_in_hospital, str(date_entree))
				st.success("Base de données mise à jour avec succès")

			

	if menu == "Suppression Patient":
		st.subheader("Mise à jour de Données Patient")
		# Layout
		col1,col2 = st.columns(2)
		
		with col1:
			identifiant_patient = st.text_input("Identifiant Patient")
		
		with col2:
			date_entree = st.date_input("Date Entree")
			
		if st.button("Supprimer"):
			sortie_patient = ad.Patient(identifiant_patient,date_entree)
			sortie_patient.sortir_de_l_hopital(identifiant_patient,date_entree)
			st.success("Base de données mise à jour avec succès")
		
		if st.button("Lister"):
			stream_patient = ad.Patient(identifiant_patient=None, nom=None, prenom=None, groupe_sanguin=None, is_in_hospital=None, date_entree=None)
			stream_patient = ad.Patient()
			data = stream_patient.afficher_les_patients_streamlit()
			#data = st.dataframe(data,use_container_width=True)
			st.write(data)

	elif menu == "Ajout RH":
		st.subheader("Mise à jour de Données RH")
		# Layout
		col1, col2 = st.columns(2)
		with col1:
			nom = st.text_input("Nom")
			prenom = st.text_input("Prenom")
			groupe_sanguin = st.selectbox("Groupe Sanguin",["O-","O+","A-","A+","B-","B+","AB-","AB+"])
		with col2:
			salaire = st.number_input("Salaire")
			working_at_hospital = st.selectbox("Travail à l'hospital",['True','False'])
			date_recrutement = st.date_input("Date Recrutement")
		if st.button("Mettre à Jour"):
			identifiant_rh = nom+prenom+groupe_sanguin+str(date_recrutement)+"_RH"
			rh = ad.RH(identifiant_rh,nom,prenom,salaire,working_at_hospital,date_recrutement,groupe_sanguin)
			rh.debuter_CDD_CDI()
			st.success("Base de données mise à jour avec succès")
	
	if menu == "Suppression RH":
		st.subheader("Mise à jour de Données RH")
		# Layout
		col1,col2 = st.columns(2)
		
		with col1:
			identifiant_rh = st.text_input("Identifiant RH")
		
		with col2:
			date_recrutement = st.date_input("Date Recrutement")
			
		if st.button("Supprimer"):
			rh = ad.RH(identifiant_rh,date_recrutement)
			rh.quitter_CDD_CDI(identifiant_rh,date_recrutement)
			st.success("Base de données mise à jour avec succès")
		
		if st.button("Lister"):
			stream_patient = ad.RH(identifiant_rh=None, nom=None, prenom=None, salaire=None, working_at_hospital=None, date_recrutement=None,groupe_sanguin=None)
			stream_patient = ad.RH()
			data = stream_patient.afficher_rh_streamlit()
			st.write(data)

	if menu == "Archives":
		arch = ad.Archive()
		data = arch.afficher_les_archives_streamlit()
		st.write(data)
	#else:
		#st.subheader("Affichage Console")

	if menu == "Patients Aléatoires":
		if st.button("Patients Aléatoires"):
			r.aleatoires.patient_aleatoire()
			#pa.patient_aleatoire()


		if st.button("Lister"):
			stream_patient = ad.Patient(identifiant_patient=None, nom=None, prenom=None, groupe_sanguin=None, is_in_hospital=None, date_entree=None)
			stream_patient = ad.Patient()
			data = stream_patient.afficher_les_patients_streamlit()
			st.write(data)


if __name__ == '__main__':
	main()