# Movie-recommendation

app.py：

  guess_like(user_id)  
  
  - Recommend a list to users
  
  query_movie_related_rec(movie_id)  
  
  - Recommend related movies to movies
  
embedding_manager.py：

  Management embedding   

  -Establish key to embedding index, you can query directly
  
  -Establish faiss index of embedding, nearest neighbor query

movie_info.py：

  Movie Information Management
  
user_rating.py：

  List of movie IDs that the user has watched

Problems to be solved (try to solve) :

how to add new users (cold start)?

We have completed a virtual new user recommendation system and are trying to modify the web page.

Here's what we think：
1. first vectorize the genre of each movie
2. When a new user signs up, there are 20 (or less) options
3. The new user's selected movie genre is marked as 1, and the unselected one is marked as 0
4. vectorize the new user's selection and perform cosine similarity calculation with all movies
5. Recommend the five most similar movies to the new user based on the result of the cosine similarity calculation

