import streamlit as st

# Page title
st.title("Offre d'emploi : Stage en Intelligence Artificielle et Machine Learning")

# Introduction
st.write("""
Bienvenue ! 👋  
Pour accéder au lien de l'offre d'emploi, abonnez-vous à ma chaîne YouTube : [Data-2-d3k](https://www.youtube.com/@Data-2-d3k).  
""")

# Subscription Verification (Manual input for demonstration)
st.write("👉 **Vérifiez votre abonnement à ma chaîne YouTube !**")

is_subscribed = st.radio(
    "Êtes-vous abonné à ma chaîne YouTube ?",
    ("Non", "Oui")
)

if is_subscribed == "Oui":
    st.success("Merci pour votre abonnement ! Voici le lien de l'offre :")
    st.markdown(
        "[Accéder à l'offre de stage en IA et ML](https://www.stagiaires.ma/offres-de-stages-et-premier-emploi-maroc/549524-stage-intelligence-artificielle-ia-et-machine-learning-ml-rabat/)",
        unsafe_allow_html=True
    )
else:
    st.warning("Vous devez vous abonner pour accéder au lien. 😊")

# Footer
st.write("Rejoignez-nous pour découvrir plus d'opportunités et contenus liés à l'IA et au Machine Learning ! 🚀")