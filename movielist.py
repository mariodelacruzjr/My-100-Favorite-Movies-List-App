import psycopg2
import requests

def add_movie_to_DB(movie_id1,mov_name):

    hostname='localhost'
    database='movielist'
    username='postgres'
    pwd='123'
    port_id=5432
    conn=None
    cur=None
    try:

        conn= psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)
        cur=conn.cursor()
        create_script= ''' CREATE TABLE IF NOT EXISTS my_movies (
            
            movie_id int,
            movie_name VARCHAR(50)
         
            
            
            )


            '''
        cur.execute(create_script)
        insert_script = 'INSERT INTO my_movies (movie_id, movie_name) VALUES (%s, %s)'
        insert_values = (movie_id1, mov_name)
        cur.execute(insert_script, insert_values)
        conn.commit()


    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()



response = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=3372059c7957b772cf7c72b570ae110f&language=en-US")
tmdb_api_response=response.json()
print("Welcome to Top 100 Movie List App")
print("Pick By Genre: 1")
print("EXIT: -1")
user_choice = input()
genre_list=tmdb_api_response["genres"]
while user_choice != '-1':


    while user_choice == '1':


        for gen in genre_list:
            print("{}: Id: {}".format(gen['name'], gen['id']))
        print("Please Select a Genre by Id")
        print('EXIT: -1')
        user_choice_gendre = input()
        
        
        temp_page=1
        
        response2 = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=3372059c7957b772cf7c72b570ae110f&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={}&with_genres={}&with_watch_monetization_types=flatrate'.format(temp_page, user_choice_gendre))
        if int(user_choice_gendre) != -1:
            
            

            while int(user_choice_gendre) >0:
                
                movie_by_selected_genre_response=response2.json()
                movie_by_selected_genre_list=movie_by_selected_genre_response["results"]
                page_number = movie_by_selected_genre_response["page"]
                total_pages = movie_by_selected_genre_response["total_pages"]
                total_results = movie_by_selected_genre_response["total_results"]
                for movie in movie_by_selected_genre_list:

                    print("{}: Id: {}".format(movie['title'], movie['id']))
                print("You are on page {} out of {}".format(page_number, total_pages))
                print("Total results: {}".format(total_results))
                print("SELECT AN OPTION")
                print("TYPE THE PAGE YOU WOULD LIKE TO GO TO")
                print("ADD A MOVIE TO LIST: 'A ID' ")
                print("TYPE -1 TO EXIT TO MENU")
                genre_id_selected=input()
                while genre_id_selected != '-1':
                    response2 = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=3372059c7957b772cf7c72b570ae110f&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={}&with_genres={}&with_watch_monetization_types=flatrate'.format(genre_id_selected, user_choice_gendre))

                    
                    if genre_id_selected[0]=='A':

                        user_page_response_add_movie_id = int(genre_id_selected[2::])


                        for movie1 in movie_by_selected_genre_list:

                            if movie1['id'] == user_page_response_add_movie_id:
                                add_movie_to_DB(movie1['id'], movie1['title'])
                                print("THE MOVIE: {} HAS BEEN ADDED TO YOUR LIST".format(movie1['title']))
                    genre_id_selected = '-1'
                    


    
    else:
        print("Done")


