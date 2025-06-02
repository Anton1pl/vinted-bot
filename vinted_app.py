import streamlit as st
import requests

st.set_page_config(page_title="Alerte Vinted", page_icon="🧥")

st.title("🔎 Alerteur Vinted - Pull Ralph Lauren < 20€")

mot_cle = st.text_input("Mot-clé de recherche", value="pull ralph lauren")
prix_max = st.slider("Prix maximum (€)", 5, 100, 20)

if st.button("Rechercher maintenant"):
    with st.spinner("Recherche en cours sur Vinted..."):
        url = "https://www.vinted.fr/api/v2/catalog/items"
        params = {
            "search_text": mot_cle,
            "price_to": prix_max,
            "order": "newest_first",
            "per_page": 20
        }
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            if items:
                st.success(f"{len(items)} articles trouvés !")
                for item in items:
                    titre = item["title"]
                    prix = item["price"]
                    lien = "https://www.vinted.fr" + item["url"]
                    st.markdown(f"**{titre}** - {prix} €")
                    st.markdown(f"[Voir sur Vinted]({lien})")
                    st.markdown("---")
            else:
                st.warning("Aucun article trouvé.")
        else:
            st.error("Erreur lors de la connexion à Vinted.")
