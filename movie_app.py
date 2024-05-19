import streamlit as st
import requests

# Define the API endpoint and your API key
OMDB_API_URL = "http://www.omdbapi.com/"
OMDB_API_KEY = "d14e4f43"  # Replace with your actual OMDb API key

def get_movie_data(movie_title):
    # Make a request to the OMDb API
    params = {
        't': movie_title,
        'apikey': OMDB_API_KEY
    }
    response = requests.get(OMDB_API_URL, params=params)
    return response.json()

# Add custom CSS for background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://example.com/your-background-image.jpg");
             background-size: cover;
             background-repeat: no-repeat;
             background-attachment: fixed;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def main():
    # Call the function to add background
    add_bg_from_url()

    st.title("Movie Information App")
    
    # Get user input
    movie_title = st.text_input("Enter a movie title:")
    
    if movie_title:
        movie_data = get_movie_data(movie_title)
        
        if movie_data.get('Response') == 'True':
            st.subheader(movie_data['Title'])
            st.image(movie_data['Poster'])
            st.write("**Year:**", movie_data['Year'])
            st.write("**Rated:**", movie_data['Rated'])
            st.write("**Released:**", movie_data['Released'])
            st.write("**Runtime:**", movie_data['Runtime'])
            st.write("**Genre:**", movie_data['Genre'])
            st.write("**Director:**", movie_data['Director'])
            st.write("**Writer:**", movie_data['Writer'])
            st.write("**Actors:**", movie_data['Actors'])
            st.write("**Plot:**", movie_data['Plot'])
            st.write("**Language:**", movie_data['Language'])
            st.write("**Country:**", movie_data['Country'])
            st.write("**Awards:**", movie_data['Awards'])
            st.write("**IMDB Rating:**", movie_data['imdbRating'])
            st.write("**IMDB Votes:**", movie_data['imdbVotes'])
            st.write("**Type:**", movie_data['Type'])
        else:
            st.write("Movie not found. Please check the title and try again.")

if __name__ == "__main__":
    main()
