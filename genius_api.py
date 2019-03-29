#/usr/bin/python3
# CSE6242 6Street
# TODO: Modify this for Genius API

import http.client
import json
import time
import sys
import collections
import csv
import time

API_KEY = ""
API_DB_URI = "api.themoviedb.org"

# 40 requests per 10 seconds...
# so 4 request per second..
def get_movies(page):
    connection = http.client.HTTPSConnection(API_DB_URI)
    payload = "{}"
    connection.request("GET", "/3/discover/movie?with_genres=18&primary_release_date.gte=2004&page=" + str(page) + "&include_video=false&include_adult=false&sort_by=popularity.desc&language=en-US&api_key=" + API_KEY, payload)
    response = connection.getresponse()
    data = response.read()
    return data 


def get_movies_alt_solution(page):
    connection = http.client.HTTPSConnection(API_DB_URI)
    payload = "{}"
    connection.request("GET", "/3/discover/movie?with_genres=18&primary_release_date.gte=2004&page=" + str(page) + "&sort_by=popularity.desc&language=en-US&api_key=" + API_KEY, payload)
    response = connection.getresponse()
    data = response.read()
    return data

# seems like 20 results per call and i need 350 entries.. so 18 calls..
# total appx. api call: 18
def do_part_b():
    result_list = []
    page = 1   
    while (len(result_list) < 350):
        data = get_movies_alt_solution(page)
        json_data = json.loads(data.decode("utf-8"))
        for result in json_data['results']:
            result_list.append({'movie-ID': result['id'], 'movie-name': result['title']})
            # TEST: include popularity and other factors
            #result_list.append({'release_date': result['release_date'], 'movie-ID': result['id'], 'movie-name': result['title'], 'orig-title': result['original_title'], 'popularity': result['popularity']}) 
        page += 1
    #print("# of results: " + str(len(result_list)))
    result_list = result_list[0:350]
    #print("# of results: " + str(len(result_list)))

    with open('movie_ID_name.csv', 'w', newline='') as csvfile:
        fieldnames = ['movie-ID', 'movie-name']
        # TEST: include popularity and other factors
        #fieldnames = ['release_date', 'movie-ID', 'movie-name', 'orig-title', 'popularity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        for result in result_list:
            writer.writerow(result)
    time.sleep(10)


def get_similar_movie(movie_id):
    time.sleep(.245)
    connection = http.client.HTTPSConnection(API_DB_URI)
    payload = "{}"
    connection.request("GET", "/3/movie/" + str(movie_id) + "/similar?page=1&language=en-US&api_key=" + API_KEY, payload)
    response = connection.getresponse()
    data = response.read()
    return data


# need to make 350 calls
# i can only make up to 4 calls per second... it will take 87.5 seconds in total
def do_part_c():
    result_list = []
    movie_id_list = []
    with open('movie_ID_name.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for movie in reader:
            movie_id_list.append(int(movie[0]))
    movie_id_list = sorted(movie_id_list)

    # duplicates
    # A < B ? keep A B
    for movie_id in movie_id_list:
        data = get_similar_movie(movie_id)
        json_data = json.loads(data.decode("utf-8"))
        five_results = json_data['results'][0:5]
        for result in five_results:
            # TEST: all results with duplicates
            #result_list.append({ 'movie-ID': int(movie_id), 'similar-movie-ID': int(result['id']) })
            similar_movie_id = int(result['id'])
            # collision/duplicate checker
            if (similar_movie_id not in movie_id_list) or (movie_id < similar_movie_id):
                result_list.append({ 'movie-ID': int(movie_id), 'similar-movie-ID': similar_movie_id })

    with open('movie_ID_sim_movie_ID.csv', 'w', newline='') as csvfile:
        fieldnames = ['movie-ID', 'similar-movie-ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        for result in result_list:
            writer.writerow(result)


def test_part_c():
    result_list = []
    # TEST: list of duplicates
    with open('movie_ID_sim_movie_ID_with_dupes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for movie in reader:
            result_list.append({ 'movie-ID': int(movie[0]), 'similar-movie-ID': int(movie[1]) })

    sorted_list = [ (result) 
        if result['movie-ID'] < result['similar-movie-ID'] 
        else ({ 'movie-ID': result['similar-movie-ID'], 'similar-movie-ID': result['movie-ID'] }) 
        for result in result_list
        ]
    result_list = sorted(sorted_list, key=lambda d: (d['movie-ID'], d['similar-movie-ID']))

    with open('dupe_list_from_with_dupes.csv', 'w', newline='') as csvfile:
        fieldnames = ['movie-ID', 'similar-movie-ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        for result in result_list:
            writer.writerow(result)


def main(argv):
    print(time.ctime())
    global API_KEY
    API_KEY = argv[0]
    print(API_KEY)
    do_part_b()
    do_part_c()
    print(time.ctime())
    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])


