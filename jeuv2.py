import streamlit as st
def start_game():
   st.title("Mission : Évasion du Labyrinthe Informatique")
   st.write("Tu es coincé dans un monde numérique. Tu dois utiliser la logique pour t'en échapper.")
   # Étape 1
   choix1 = st.radio("Tu arrives à un panneau avec deux portes : une bleue, une rouge. Laquelle choisis-tu ?", ["Bleue", "Rouge"])
   if choix1 != "Bleue":
       st.error("La porte rouge te ramène à la case départ. Recommence.")
       return
   # Étape 2
   st.success("Bonne porte ! Tu avances.")
   choix2 = st.radio("Un robot te demande un mot de passe logique. Lequel est valide ?", ["12345", "open_sesame", "azerty", "motdepasse"])
   if choix2 != "open_sesame":
       st.error("Mot de passe invalide. Recommence.")
       return
   # Étape 3
   st.success("Mot de passe accepté.")
   choix3 = st.radio("Tu trouves une devinette : 'Je suis un nombre pair entre 10 et 14'. Que réponds-tu ?", ["11", "12", "13", "14"])
   if choix3 != "12":
       st.error("Mauvaise réponse. Recommence.")
       return
   # Étape 4
   st.success("Bonne réponse.")
   choix4 = st.radio("Une intelligence artificielle te pose une question : 'Si A = 1, B = 2... Quelle est la somme de C + D ?'", ["5", "6", "7", "8"])
   if choix4 != "7":
       st.error("Erreur de calcul. Recommence.")
       return
   # Étape 5
   st.success("Bonne réponse !")
   choix5 = st.radio("Tu arrives devant un écran : 'Pour continuer, trouve l'intrus : HTML, CSS, Python, JPEG'", ["HTML", "CSS", "Python", "JPEG"])
   if choix5 != "JPEG":
       st.error("Mauvaise réponse. Recommence.")
       return
   st.balloons()
   st.success("Félicitations ! Tu as terminé le jeu avec logique et réflexion !")
# Lancement du jeu
start_game()