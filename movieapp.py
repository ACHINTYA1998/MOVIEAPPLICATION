import imdb
A=imdb.IMDb()
movie_name=input("enter a movie name:")
movies=A.search_movie(movie_name)
index=movies[0].getID()
movie=A.get_movie(index)
title=movie['title']
year=movie['year']
genre=movie['genres']
plot=movie['plot'][:2]
cast=movie['cast']
casts=','.join(map(str,cast))
writers=movie['writers']
directors=movie['directors']
movie_writers=','.join(map(str,writers))
movie_directors=','.join(map(str,directors))
print('\n','Movie Title:',title,'\n')
print('Year Of Release:',year,'\n')
print('Genre:',genre,'\n')
print('Plot:',plot,'\n')
print('Full Cast:',casts,'\n')
print('Director:',movie_directors,'\n')
print("Writer:",movie_writers)
