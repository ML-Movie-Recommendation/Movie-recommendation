# Movie-recommendation

app.py：
  guess_like(user_id)    - Recommend a list to users
  query_movie_related_rec(movie_id)    - Recommend related movies to movies
  
embedding_manager.py：
  Management embedding    -Establish key to embedding index, you can query directly
                          -Establish faiss index of embedding, nearest neighbor query

movie_info.py
  Movie Information Management
  
user_rating.py：
  List of movie IDs that the user has watched
