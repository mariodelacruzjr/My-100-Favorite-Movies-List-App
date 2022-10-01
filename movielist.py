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
def add_movie_to_list_from_movie_list_from_genre(user_choice,selected_genre_temp,movie_list_from_genre_temp):
                    
    while user_choice != '-1':
    
                        
        print("ENTER MOVIE ID")
        user_movie_id_to_add = int(input())                
        
    
    
        for movie1 in movie_list_from_genre_temp:
                            
            if movie1['id'] == user_movie_id_to_add:
                add_movie_to_DB(movie1['id'], movie1['title'])
                print("THE MOVIE: {} HAS BEEN ADDED TO YOUR LIST".format(movie1['title']))
                print("Press any key to continue...")
                pause=input()
        user_choice = '-1'    
def visit_different_page_from_movie_list_from_genre(user_choice,selected_genre_temp):
    while user_choice != '-1':
        print("ENTER PAGE NUMBER TO VISIT")
        user_page_number = input()
        if user_page_number == '-1':
            return '-1'
        else:

        #response2 = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=3372059c7957b772cf7c72b570ae110f&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={}&with_genres={}&with_watch_monetization_types=flatrate'.format(user_page_number, selected_genre_temp)
            movie_list_from_genre(user_choice, selected_genre_temp,user_page_number)
        #user_choice = '-1'


def main_menu():
    user_choice=0
    while user_choice != '-1':
        print("\nWelcome to Top 100 Movie List App")
        print("Pick By Genre: 1")
        print("EXIT: -1")

        user_choice = input()
        if user_choice == '1':
            genre_menu(user_choice)
def movie_list_from_genre(user_choice2, userchoicegendre_var,temp_page=1):

        while int(user_choice2) > 0:
        
        

            
            
            
            
            response2 = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=3372059c7957b772cf7c72b570ae110f&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={}&with_genres={}&with_watch_monetization_types=flatrate'.format(temp_page, userchoicegendre_var))
            if userchoicegendre_var != '-1':
                
                
            
                while userchoicegendre_var != '-1':
                    
                    movie_by_selected_genre_response=response2.json()
                    movie_by_selected_genre_list=movie_by_selected_genre_response["results"]
                    page_number = movie_by_selected_genre_response["page"]
                    total_pages = movie_by_selected_genre_response["total_pages"]
                    total_results = movie_by_selected_genre_response["total_results"]
                    for movie in movie_by_selected_genre_list:
                    
                        print("{}: Id: {}".format(movie['title'], movie['id']))
                    print("\nYou are on page {} out of {}".format(page_number, total_pages))
                    print("Total results: {}".format(total_results))
                    print("SELECT AN OPTION")
                
                    print("1: ADD A MOVIE TO LIST")
                    print("2: GO TO DIFFERENT PAGE")
                
                    print("-1: EXIT TO LAST MENU")
                    
                    user_choice_movie_list_by_genre=input()
                    #print(user_choice_movie_list_by_genre)
                    if user_choice_movie_list_by_genre == '1':
                        add_movie_to_list_from_movie_list_from_genre(user_choice_movie_list_by_genre,userchoicegendre_var,movie_by_selected_genre_list)
                    elif user_choice_movie_list_by_genre == '2':
                        visit_different_page_from_movie_list_from_genre(user_choice_movie_list_by_genre,userchoicegendre_var)
                        #1
                        #if user_choice_movie_list_by_genre
                         
                    elif user_choice_movie_list_by_genre == '-1':
                        userchoicegendre_var = '-1'
                        user_choice2='-1'                        

                        print("exiting...")


            
        else:
            print("done")

def genre_menu(user_choice1):
    response = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=3372059c7957b772cf7c72b570ae110f&language=en-US")
    tmdb_api_response=response.json()
    genre_list=tmdb_api_response["genres"]
    while user_choice1 != '-1':
        for gen in genre_list:
            print("{}: Id: {}".format(gen['name'], gen['id']))
        print("\nPlease Select a Genre by Id")
        print('EXIT: -1')
        user_choice_gendre = input()
        if user_choice_gendre != '-1':


            movie_list_from_genre(user_choice1,user_choice_gendre)
        else:
            print("exiting...")
            user_choice1 = '-1'

main_menu()