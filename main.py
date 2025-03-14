import streamlit as st
import pandas as pd
import random

# Sample book data
data = {
    "Title": ["1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick", "War and Peace"],
    "Author": ["George Orwell", "Harper Lee", "F. Scott Fitzgerald", "Herman Melville", "Leo Tolstoy"],
    "Genre": ["Dystopian", "Classic", "Classic", "Adventure", "Historical"],
    "Rating": [4.8, 4.9, 4.7, 4.5, 4.6],
    "Read": [False, True, False, True, False]
}

# Convert to DataFrame
df = pd.DataFrame(data)

st.title("📚 Personal Digital Bookshelf")
st.write("Manage your personal book collection easily Made by M Saeed!")

# New Feature: Random Book Recommendation
if st.button("📖 Recommend me a book!"):
    recommended_book = df.sample(1).iloc[0]
    st.success(f"**{recommended_book['Title']}** by {recommended_book['Author']} (Genre: {recommended_book['Genre']})")

# Display books
tab1, tab2 = st.tabs(["📚 All Books", "📌 Add Book"])

with tab1:
    st.subheader("Your Bookshelf")
    st.dataframe(df)

with tab2:
    st.subheader("Add a New Book")
    new_title = st.text_input("Book Title")
    new_author = st.text_input("Author")
    new_genre = st.text_input("Genre")
    new_rating = st.slider("Rating", 0.0, 5.0, 4.0, 0.1)
    read_status = st.checkbox("Mark as Read")
    
    if st.button("➕ Add Book"):
        new_book = pd.DataFrame({
            "Title": [new_title],
            "Author": [new_author],
            "Genre": [new_genre],
            "Rating": [new_rating],
            "Read": [read_status]
        })
        df = pd.concat([df, new_book], ignore_index=True)
        st.success(f"Added '{new_title}' to your bookshelf!")
