from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import csv
from django.views.static import serve
from django.conf import os


@csrf_exempt
def index(request, param):
    if request.method == "POST":
        lst_data=[]
        #getting people count as input
        people = int(request.GET.get('people_count'))
        if people:
            for i in range(1,people+1):
                #getting json data from url
                user_data = requests.get(url='https://swapi.co/api/people/'+str(i)+'/')
                # print(user_data.json())
                #storing data to dictionary
                dct_data={}
                dct_data['name'] = user_data.json()['name']
                dct_data['height'] = user_data.json()['height']
                dct_data['mass'] = user_data.json()['mass']
                dct_data['hair_color'] = user_data.json()['hair_color']
                dct_data['skin_color'] = user_data.json()['skin_color']
                dct_data['eye_color'] = user_data.json()['eye_color']
                dct_data['birth_year'] = user_data.json()['birth_year']
                dct_data['gender'] = user_data.json()['gender']
                dct_data['created'] = user_data.json()['created']
                dct_data['edited'] = user_data.json()['edited']
                #fetching nested json data
                lst_films=[]
                for data in (user_data.json()['films']):
                    film_data = requests.get(url=''+data+'')
                    lst_films.append(film_data.json()["title"])
                dct_data['films'] = lst_films

                lst_homeworld = []
                homeworld_data = requests.get(url=''+user_data.json()['homeworld']+'')
                lst_homeworld.append(homeworld_data.json()["name"])
                dct_data['homeworld'] = lst_homeworld
                lst_species=[]
                for data in (user_data.json()['species']):
                    species_data = requests.get(url='' + data + '')
                    lst_species.append(species_data.json()["name"])
                dct_data['species'] = lst_species
                lst_vehicles=[]
                for data in (user_data.json()['vehicles']):
                    vehicles_data = requests.get(url='' + data + '')
                    lst_vehicles.append(vehicles_data.json()["name"])
                dct_data['vehicles'] = lst_vehicles
                lst_starships = []
                for data in (user_data.json()['starships']):
                    starships_data = requests.get(url='' + data + '')
                    lst_starships.append(starships_data.json()["name"])
                dct_data['starships'] = lst_starships


                lst_data.append(dct_data)
                # print(people)
            # print(lst_data)
            # import pdb;
            # pdb.set_trace()
            #csv file creation
            keys = lst_data[0].keys()
            try:
                with open('test\people.csv', 'w') as csv_file:
                    dict_writer = csv.DictWriter(csv_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(lst_data)
                filepath = 'test\people.csv'
                return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
                # return HttpResponse("users\\test\people.csv")
            except Exception as io:
                return HttpResponse(io)

        else:
            # print("no data")
            return HttpResponse("no data")
    else:
        lst_data = []
        # getting people count as input
        people = int(request.GET.get('people_count'))
        if people:
            for i in range(1, people + 1):
                # getting json data from url
                user_data = requests.get(url='https://swapi.co/api/people/' + str(i) + '/')
                # print(user_data.json())
                # storing data to dictionary
                dct_data = {}
                dct_data['name'] = user_data.json()['name']
                dct_data['height'] = user_data.json()['height']
                dct_data['mass'] = user_data.json()['mass']
                dct_data['hair_color'] = user_data.json()['hair_color']
                dct_data['skin_color'] = user_data.json()['skin_color']
                dct_data['eye_color'] = user_data.json()['eye_color']
                dct_data['birth_year'] = user_data.json()['birth_year']
                dct_data['gender'] = user_data.json()['gender']
                dct_data['created'] = user_data.json()['created']
                dct_data['edited'] = user_data.json()['edited']
                # fetching nested json data
                lst_films = []
                for data in (user_data.json()['films']):
                    film_data = requests.get(url='' + data + '')
                    lst_films.append(film_data.json()["title"])
                dct_data['films'] = lst_films

                lst_homeworld = []
                homeworld_data = requests.get(url='' + user_data.json()['homeworld'] + '')
                lst_homeworld.append(homeworld_data.json()["name"])
                dct_data['homeworld'] = lst_homeworld
                lst_species = []
                for data in (user_data.json()['species']):
                    species_data = requests.get(url='' + data + '')
                    lst_species.append(species_data.json()["name"])
                dct_data['species'] = lst_species
                lst_vehicles = []
                for data in (user_data.json()['vehicles']):
                    vehicles_data = requests.get(url='' + data + '')
                    lst_vehicles.append(vehicles_data.json()["name"])
                dct_data['vehicles'] = lst_vehicles
                lst_starships = []
                for data in (user_data.json()['starships']):
                    starships_data = requests.get(url='' + data + '')
                    lst_starships.append(starships_data.json()["name"])
                dct_data['starships'] = lst_starships

                lst_data.append(dct_data)
                # print(people)
            # print(lst_data)
            # import pdb;
            # pdb.set_trace()
            # csv file creation
            keys = lst_data[0].keys()
            # import pdb;
            # pdb.set_trace()
            try:
                with open('test\people.csv', 'w') as csv_file:
                    dict_writer = csv.DictWriter(csv_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(lst_data)
                filepath = 'test\people.csv'
                return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
                # return HttpResponse("users\\test\people.csv")
            except Exception as io:
                return HttpResponse(io)

        else:
            # print("no data")
            return HttpResponse("no data")
        return HttpResponse("do post request")
