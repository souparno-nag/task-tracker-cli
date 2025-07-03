import os
import json
from pprint import pprint
from faker import Faker

# get all data from json file
FILEPATH = 'city.json'
def get_json_data():
    with open(FILEPATH) as json_file:
       data = json.load(json_file)
    return data

# CRUD: READ All
def get_all_cities():

    data = get_json_data() 

    # print(data)
    return data

#store data to json file
def store_json_data(data):
    with open(FILEPATH, 'w') as outfile:
         json.dump(data, outfile)
         
#adding one data to the file
def add_city(city, state):
    current_data = {
        "name"  : city,
        "state" : state
    }
    data = get_json_data()
    # print(data)
    data[city] = current_data
    store_json_data(data)
    
#reading single data from the file
def get_single_city(city_name):
    data = get_json_data()
    if(city_name in data):
        return data[city_name]
        # print(data)
    return None

#updating data in the file
def update_single_city(city_name, city_state):
    data = get_json_data()
    if(city_name in data):
        city_data = {
        'name' : city_name,
        'state' : city_state
        }
    data[city_name] = city_data
    store_json_data(data)
    
#delete single data from the file
def delete_single_city(city_name):
    data = get_json_data()
    if(city_name in data):
        data.pop(city_name)
    store_json_data(data)
    
#delete all data from the file
def delete_all_cities():
# get all keys and pop each
    data = get_json_data()
    city_list = list(data.keys())
    for current_city in city_list:
        print(current_city)
        data.pop(current_city)
    store_json_data(data)
    
#effective delete all data
def delete_all_cities_efficient():
    current_dict = {}
    store_json_data(current_dict)
    
    
#add multiple data to the file
fake = Faker()

def add_multiple_cities_test():
    Faker.seed(0)
    for c_index in range(1000):
        current_city = fake.city()
        current_state = fake.state()
        # print(current_city, current_state)
        add_city(current_city, current_state)
        print(f'{c_index} Added: ', current_city, current_state)
        
# Check if the file exists
if not os.path.exists(FILEPATH):
    # Create the file with default content (e.g., empty dictionary)
    with open(FILEPATH, 'w') as f:
        json.dump({}, f)
    print(f"{FILEPATH} created.")
else:
    print(f"{FILEPATH} already exists.")
        
def startpy():
    # pass
    
    print("CRUD started!")
    
    # add_multiple_cities_test()
    
    # CRUD: Add City
    # city    = "Madurai"
    # state   = "Tamilnadu"
    # add_city(city, state)
    
    # CRUD: READ all
    # cities = get_all_cities()
    # pprint(cities)
    
    # CRUD: READ single
    # city_name = 'Waterloo'
    # single_city = get_single_city(city_name)
    # print(single_city)
    
    # CRUD: UPDATE
    # city_name = 'Madurai'
    # city_state = 'Tamilnadu'
    # update_single_city(city_name, city_state)

    # CRUD: DELETE Single
    # city_name = 'Montreal'
    # delete_single_city(city_name)

    # CRUD: DELETE All
    # start_time = time.time()
    # delete_all_cities()
    # executionTime = (time.time() - start_time)
    # print('[delete_all_cities]Execution time in seconds: ' + str(executionTime))

    # # # CRUD: DELETE All Efficient
    # start_time = time.time()
    # delete_all_cities_efficient()
    # executionTime = (time.time() - start_time)
    # print('[delete_all_cities_efficient]Execution time in seconds: ' + str(executionTime))
    
    print('\nCRUD Done!')

if __name__ == '__main__':
    startpy()