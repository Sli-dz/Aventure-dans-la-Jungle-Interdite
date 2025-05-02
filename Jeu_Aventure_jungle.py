import streamlit as st
st.set_page_config(page_title="Aventure jungle", page_icon="🌴")
# Initialisation
if "étape" not in st.session_state:
   st.session_state.étape = 1
   st.session_state.score = 0
def recommencer():
   st.session_state.étape = 1
   st.session_state.score = 0
st.title("🌴 Aventure dans la Jungle Interdite")
st.markdown(f"**Étape {st.session_state.étape}/30**")
# Étape 1
if st.session_state.étape == 1:
   st.markdown("Tu es perdu dans une jungle. Tu arrives à une bifurcation.")
   choix = st.radio("Quel chemin prends-tu ?", ["", "Gauche : vers les cris", "Droite : vers le silence"])
   if st.button("Valider"):
       if "Droite" in choix:
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu t’es fait repérer par une bête !")
           recommencer()
# Étape 2
elif st.session_state.étape == 2:
   st.markdown("Tu trouves un pont fragile et un tronc d’arbre pourri.")
   choix = st.radio("Que choisis-tu ?", ["", "Traverser le pont", "Marcher sur le tronc"])
   if st.button("Valider"):
       if choix == "Traverser le pont":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Le tronc se casse et tu tombes dans l’eau.")
           recommencer()
# Étape 3
elif st.session_state.étape == 3:
   st.markdown("Devant toi, un mur avec trois symboles.")
   choix = st.radio("Quel symbole actives-tu ?", ["", "Serpent", "Soleil", "Clé"])
   if st.button("Valider"):
       if choix == "Clé":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Un piège se déclenche !")
           recommencer()
# Étape 4
elif st.session_state.étape == 4:
   st.markdown("Un ravin bloque le passage. Tu peux escalader un arbre ou tenter de sauter.")
   choix = st.radio("Que fais-tu ?", ["", "Sauter", "Grimper à l’arbre", "Contourner"])
   if st.button("Valider"):
       if choix == "Grimper à l’arbre":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu tombes et perds connaissance...")
           recommencer()
# Étape 5
elif st.session_state.étape == 5:
   st.markdown("Il fait noir. Tu peux allumer une torche, utiliser ton téléphone ou continuer dans le noir.")
   choix = st.radio("Choix :", ["", "Continuer dans le noir", "Utiliser la torche", "Utiliser le téléphone"])
   if st.button("Valider"):
       if choix == "Utiliser la torche":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu trébuches et te blesses...")
           recommencer()
# Étape 6
elif st.session_state.étape == 6:
   st.markdown("Tu trouves un sac. Tu peux l’ouvrir ou l’ignorer.")
   choix = st.radio("Choix :", ["", "Ouvrir le sac", "L’ignorer"])
   if st.button("Valider"):
       if choix == "Ouvrir le sac":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Le sac contenait une carte importante !")
           recommencer()
# Étape 7
elif st.session_state.étape == 7:
   st.markdown("Tu rencontres un singe qui bloque ton chemin. Il semble avoir faim.")
   choix = st.radio("Que fais-tu ?", ["", "Lui donner une banane", "L’effrayer", "L’ignorer"])
   if st.button("Valider"):
       if choix == "Lui donner une banane":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Le singe devient agressif...")
           recommencer()
# Étape 8
elif st.session_state.étape == 8:
   st.markdown("Une rivière se dresse devant toi.")
   choix = st.radio("Comment traverses-tu ?", ["", "Nager", "Construire un radeau", "Chercher un gué"])
   if st.button("Valider"):
       if choix == "Chercher un gué":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu te fais emporter par le courant !")
           recommencer()
# Étape 9
elif st.session_state.étape == 9:
   st.markdown("Tu entends des voix humaines. Tu peux approcher discrètement ou fuir.")
   choix = st.radio("Choix :", ["", "Approcher discrètement", "Fuir", "Crier pour appeler à l’aide"])
   if st.button("Valider"):
       if choix == "Approcher discrètement":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu es repéré par un groupe hostile.")
           recommencer()
# Étape 10
elif st.session_state.étape == 10:
   st.markdown("Tu découvres un camp abandonné avec de la nourriture et une radio cassée.")
   choix = st.radio("Que fais-tu ?", ["", "Manger", "Réparer la radio", "Tout fouiller"])
   if st.button("Valider"):
       if choix == "Réparer la radio":
           st.success("Tu réussis à envoyer un signal de détresse !")
           st.balloons()
           st.write(f"Score : {st.session_state.score}/10")
           if st.button("Continuer vers l’étape 11"):
               st.session_state.étape += 1
       else:
           st.error("Tu perds du temps et la nuit tombe...")
           recommencer()
# Étape 11
elif st.session_state.étape == 11:
   st.markdown("Un brouillard dense t’empêche de voir. Tu peux avancer lentement, attendre ou faire demi-tour.")
   choix = st.radio("Que fais-tu ?", ["", "Avancer lentement", "Attendre", "Faire demi-tour"])
   if st.button("Valider"):
       if choix == "Avancer lentement":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu perds du temps, et la météo empire...")
           recommencer()
# Étape 12
elif st.session_state.étape == 12:
   st.markdown("Un serpent bloque le chemin. Tu peux l’éviter, l’attaquer ou attendre qu’il parte.")
   choix = st.radio("Choix :", ["", "L’éviter", "L’attaquer", "Attendre qu’il parte"])
   if st.button("Valider"):
       if choix == "L’éviter":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu te fais mordre !")
           recommencer()
# Étape 13
elif st.session_state.étape == 13:
   st.markdown("Tu découvres une grotte. Tu peux y entrer, l’inspecter ou passer ton chemin.")
   choix = st.radio("Que fais-tu ?", ["", "Entrer", "Inspecter", "Passer ton chemin"])
   if st.button("Valider"):
       if choix == "Inspecter":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Une chauve-souris te surprend et tu fuis paniqué.")
           recommencer()
# Étape 14
elif st.session_state.étape == 14:
   st.markdown("Dans la grotte, tu trouves un coffre fermé. Tu peux forcer la serrure, chercher une clé ou abandonner.")
   choix = st.radio("Choix :", ["", "Forcer la serrure", "Chercher une clé", "Abandonner"])
   if st.button("Valider"):
       if choix == "Chercher une clé":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu déclenches un piège caché.")
           recommencer()
# Étape 15
elif st.session_state.étape == 15:
   st.markdown("Tu entends des tambours. Un ancien temple est proche.")
   choix = st.radio("Tu décides de :", ["", "Observer de loin", "Entrer sans hésiter", "Contourner"])
   if st.button("Valider"):
       if choix == "Observer de loin":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Des gardiens t’aperçoivent !")
           recommencer()
# Étape 16
elif st.session_state.étape == 16:
   st.markdown("Une dalle s’enfonce sous tes pieds. Tu dois choisir une direction rapidement.")
   choix = st.radio("Direction ?", ["", "Nord", "Est", "Ouest"])
   if st.button("Valider"):
       if choix == "Est":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu tombes dans un piège.")
           recommencer()
# Étape 17
elif st.session_state.étape == 17:
   st.markdown("Tu trouves un manuscrit ancien dans une salle secrète.")
   choix = st.radio("Que fais-tu ?", ["", "Le lire", "L’emporter", "Le brûler"])
   if st.button("Valider"):
       if choix == "Le lire":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Une malédiction se déclenche !")
           recommencer()
# Étape 18
elif st.session_state.étape == 18:
   st.markdown("Une série de statues pointe vers une direction.")
   choix = st.radio("Que fais-tu ?", ["", "Suivre leur direction", "Aller à l’opposé", "Ignorer"])
   if st.button("Valider"):
       if choix == "Suivre leur direction":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu t’égares dans un labyrinthe.")
           recommencer()
# Étape 19
elif st.session_state.étape == 19:
   st.markdown("Tu arrives devant une porte gravée de symboles. Trois combinaisons possibles.")
   choix = st.radio("Quel symbole choisis-tu ?", ["", "Lune-Feu-Clé", "Feu-Clé-Lune", "Clé-Feu-Lune"])
   if st.button("Valider"):
       if choix == "Clé-Feu-Lune":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("La porte explose !")
           recommencer()
# Étape 20
elif st.session_state.étape == 20:
   st.markdown("Tu découvres un message : 'Celui qui sait attendre trouvera le chemin'.")
   choix = st.radio("Que fais-tu ?", ["", "T’attendre", "Courir droit devant", "Rebrousser chemin"])
   if st.button("Valider"):
       if choix == "T’attendre":
           st.success("Tu découvres un passage secret vers la sortie du temple !")
           st.balloons()
           st.write(f"Score : {st.session_state.score}/20")
           if st.button("Continuer vers l’étape 21"):
               st.session_state.étape += 1
       else:
           st.error("Tu tombes dans une trappe cachée.")
           recommencer()
# Étape 21
elif st.session_state.étape == 21:
   st.markdown("Un pont suspendu se dresse devant toi. Il a l’air fragile.")
   choix = st.radio("Que fais-tu ?", ["", "Traverser lentement", "Sauter dessus", "Faire un détour"])
   if st.button("Valider"):
       if choix == "Traverser lentement":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Le pont cède sous ton poids !")
           recommencer()
# Étape 22
elif st.session_state.étape == 22:
   st.markdown("Une rivière te bloque. Elle est rapide et large.")
   choix = st.radio("Comment la traverses-tu ?", ["", "Construire un radeau", "Nager", "Chercher un passage à gué"])
   if st.button("Valider"):
       if choix == "Chercher un passage à gué":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu es emporté par le courant !")
           recommencer()
# Étape 23
elif st.session_state.étape == 23:
   st.markdown("Tu arrives dans une clairière où un vieux sage t’attend.")
   choix = st.radio("Il te pose une énigme : 'Je parle sans bouche et j’entends sans oreilles. Qui suis-je ?'", ["", "Le vent", "L’écho", "Le silence"])
   if st.button("Valider"):
       if choix == "L’écho":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Le sage te renvoie au début du chemin.")
           recommencer()
# Étape 24
elif st.session_state.étape == 24:
   st.markdown("Tu découvres une stèle indiquant une direction en code ancien.")
   choix = st.radio("Quelle direction choisis-tu ?", ["", "Sud-Est", "Nord-Ouest", "Ouest"])
   if st.button("Valider"):
       if choix == "Nord-Ouest":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu tournes en rond...")
           recommencer()
# Étape 25
elif st.session_state.étape == 25:
   st.markdown("Une panthère t’observe depuis les feuillages.")
   choix = st.radio("Réaction :", ["", "Rester immobile", "Crier", "Lancer un objet"])
   if st.button("Valider"):
       if choix == "Rester immobile":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("La panthère t’attaque !")
           recommencer()
# Étape 26
elif st.session_state.étape == 26:
   st.markdown("Une statue ancienne tient une tablette. Tu peux la lire, la prendre ou l’ignorer.")
   choix = st.radio("Choix :", ["", "Lire la tablette", "La prendre", "L’ignorer"])
   if st.button("Valider"):
       if choix == "Lire la tablette":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Un piège magique s’active !")
           recommencer()
# Étape 27
elif st.session_state.étape == 27:
   st.markdown("Le chemin se divise en trois tunnels : un sombre, un éclairé, un très étroit.")
   choix = st.radio("Quel tunnel prends-tu ?", ["", "Le sombre", "L’éclairé", "Le très étroit"])
   if st.button("Valider"):
       if choix == "Le très étroit":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu es pris au piège.")
           recommencer()
# Étape 28
elif st.session_state.étape == 28:
   st.markdown("Tu tombes sur une fresque montrant trois symboles : serpent, soleil, montagne.")
   choix = st.radio("Quel symbole actives-tu ?", ["", "Soleil", "Montagne", "Serpent"])
   if st.button("Valider"):
       if choix == "Montagne":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Un piège se déclenche.")
           recommencer()
# Étape 29
elif st.session_state.étape == 29:
   st.markdown("Un dernier pont de cordes traverse un gouffre.")
   choix = st.radio("Tu :", ["", "Vérifies les cordes avant", "Cours dessus", "Attends la nuit"])
   if st.button("Valider"):
       if choix == "Vérifies les cordes avant":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Le pont cède.")
           recommencer()
# Étape 30
elif st.session_state.étape == 30:
   st.markdown("Tu arrives enfin au sommet de la montagne sacrée. Une lumière t’enveloppe.")
   st.success("FÉLICITATIONS ! Tu as terminé l’aventure.")
   st.balloons()
   st.write(f"Score final : {st.session_state.score}/30")
   if st.button("Recommencer l’aventure"):
       recommencer()