import streamlit as st

# URL de l'offre d'emploi
offer_url = "https://www.stagiaires.ma/offres-de-stages-et-premier-emploi-maroc/549524-stage-intelligence-artificielle-ia-et-machine-learning-ml-rabat/"

# Lien direct vers la chaîne YouTube
youtube_channel_url = "https://www.youtube.com/@Data-2-d3k"

# Titre de l'application
st.title("Postuler à l'offre - Abonnement requis")

# Demander à l'utilisateur de s'abonner à la chaîne YouTube
st.write("Avant de postuler à l'offre, vous devez vous abonner à notre chaîne YouTube.")

# Ajouter un lien direct vers la chaîne YouTube
st.write(f"Vous pouvez vous abonner à notre chaîne YouTube ici : [Abonnez-vous à notre chaîne YouTube]({youtube_channel_url})")

# Demander à l'utilisateur de confirmer son abonnement
abonne = st.checkbox("J'ai bien abonné à la chaîne YouTube")

# Si l'utilisateur coche la case, afficher le lien vers l'offre
if abonne:
    st.success("Vous êtes abonné ! Vous pouvez maintenant accéder à l'offre.")
    st.markdown(f"[Cliquez ici pour accéder à l'offre]( {offer_url} )")
else:
    st.warning("Vous devez vous abonner à la chaîne YouTube pour postuler à l'offre.")

