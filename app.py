import streamlit as st
import requests

# Configuration
YOUTUBE_CHANNEL_ID = "UCID_YOUR_CHANNEL"  # Remplacez par l'ID de votre chaîne YouTube
API_KEY = "YOUR_YOUTUBE_API_KEY"  # Remplacez par votre clé API
JOB_LINK = "https://www.stagiaires.ma/offres-de-stages-et-premier-emploi-maroc/549524-stage-intelligence-artificielle-ia-et-machine-learning-ml-rabat/"


def check_subscription(api_key, channel_id, user_channel_id):
    """
    Vérifie si un utilisateur est abonné à la chaîne YouTube.
    """
    url = (
        f"https://www.googleapis.com/youtube/v3/subscriptions"
        f"?part=snippet&forChannelId={channel_id}&mine=true&key={api_key}"
    )
    headers = {"Authorization": f"Bearer {user_channel_id}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            return True
    return False


def main():
    st.title("Accédez à l'offre en vous abonnant à notre chaîne YouTube 🎥")

    # Étape 1: Lien vers la chaîne YouTube
    st.write("👉 **Abonnez-vous à notre chaîne YouTube :** [Data-2-d3k](https://www.youtube.com/@Data-2-d3k)")

    # Étape 2: Entrée utilisateur pour vérifier l'abonnement
    st.write("### Vérifiez votre abonnement")
    user_channel_id = st.text_input("Entrez votre identifiant YouTube ou connectez-vous")

    if st.button("Vérifier l'abonnement"):
        if user_channel_id:
            subscribed = check_subscription(API_KEY, YOUTUBE_CHANNEL_ID, user_channel_id)
            if subscribed:
                st.success("Vous êtes abonné ! Voici le lien de l'offre :")
                st.write(f"[Cliquez ici pour accéder à l'offre]({JOB_LINK})")
            else:
                st.error("Vous n'êtes pas encore abonné à la chaîne. Veuillez vous abonner et réessayer.")
        else:
            st.error("Veuillez entrer un identifiant YouTube valide.")

    # Étape 3: Message supplémentaire
    st.info(
        "Pour toute difficulté, contactez-nous via les commentaires de notre chaîne YouTube."
    )


if __name__ == "__main__":
    main()
