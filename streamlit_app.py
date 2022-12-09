import streamlit as st

# Créez la page d'accueil d'Amazon
st.title("Bienvenue sur Amazon")
st.markdown("**Explorez notre large sélection de produits**")

# Affichez les catégories de produits
st.sidebar.title("Catégories de produits")
categories = ["Livres", "Électronique", "Vêtements", "Jouets", "Meubles"]
selected_category = st.sidebar.selectbox("Choisissez une catégorie", categories)

# Affichez les produits dans la catégorie sélectionnée
if selected_category == "Livres":
    st.subheader("Livres")
    st.markdown("Affichage des livres disponibles dans cette catégorie")
elif selected_category == "Électronique":
    st.subheader("Électronique")
    st.markdown("Affichage des produits électroniques disponibles dans cette catégorie")
elif selected_category == "Vêtements":
    st.subheader("Vêtements")
    st.markdown("Affichage des vêtements disponibles dans cette catégorie")
elif selected_category == "Jouets":
    st.subheader("Jouets")
    st.markdown("Affichage des jouets disponibles dans cette catégorie")
else:
    st.subheader("Meubles")
    st.markdown("Affichage des meubles disponibles dans cette catégorie")
