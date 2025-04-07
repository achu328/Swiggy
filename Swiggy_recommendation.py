import streamlit as st
import pandas as pd

df = pd.read_csv(r"C:\Users\achu1\Documents\GUVI\Project - 4\cleaned_data.csv")

unique_cities = ["All"] + sorted(df["city"].dropna().unique())
unique_cuisines = ["All"] + sorted(df["cuisine"].dropna().unique())

st.title("Swiggy Recommendation System")
city = st.selectbox("Select City:", unique_cities)
cuisine = st.selectbox("Select Cuisine:", unique_cuisines)
min_rating = st.slider("Rating:", min_value=0.0, max_value=5.0, step=0.1)
max_price = st.slider("Price(₹):", min_value=0, value=5000, step=100)

# Recommendation logic
def recommendations(user_input, df):
    
    if user_input["city"] != "All":
        df = df[df["city"] == user_input["city"]]
    
    if user_input["cuisine"] != "All":
        df = df[df["cuisine"] == user_input["cuisine"]]
    
    df = df[
        (df["rating"] >= user_input["min_rating"]) &
        (df["cost"] <= user_input["max_price"])
    ]
    
    return df[["name", "city", "cuisine", "rating", "cost"]].head(30)

if st.button("Get Your Restaurants"):
    user_input = {
        "city": city,
        "cuisine": cuisine,
        "min_rating": min_rating,
        "max_price": max_price
    }
    recommendations = recommendations(user_input, df)

    if recommendations.empty:
        st.warning("No matching restaurants found.")
    else:
        st.success(f"Here's your Favourite Restraurants:")
        st.dataframe(recommendations)
