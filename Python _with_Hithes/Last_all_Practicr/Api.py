# Api handling in python ----------------------------
# How to work API in python


import requests
from pymongo import MongoClient

def get_user_data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data['success'] and "data" in data:
        user_data = data['data']
        user_id = user_data['id']
        user_name = user_data['login']['username']
        user_country = user_data['location']['country']
        return user_id,user_name,user_country
        
    else:
        raise Exception('Faild to fetch data__')

client = MongoClient("mongodb+srv://mohammadpy:mohammadpy@machinelearning.hbo9rte.mongodb.net/ytmanager")
db = client['user_Data']
collection = db['Information']


def list_all_user():
    print('*' * 70)
    print('\n')
    all_user = collection.find()
    for user in all_user:
        print(f'ID : {user['_id']} Name : {user['name']} and Country : {user['country']} ')

def add_new_user(user_id,user_name,user_country):
     collection.insert_one({'_id' : user_id, 'name' :user_name, 'country':user_country})

def update_user_data(user_id_1,user_name_1,user_country_1):
    
    collection.update_one(
        {'_id': user_id_1},
        {"$set":{'name':user_name_1, 'country' : user_country_1}}
    )

def delete_data(user_id_2):
    collection.delete_one({'_id' : user_id_2})

def user_details(user_id_3):
    get_data = collection.find_one({'_id' : user_id_3})
    print(get_data)





def main():
    user_id,user_name,user_country = get_user_data()
    while True:
        print('\n Random User Information || Chosen Option')
        print('1. List all user.')
        print('2. Add new user.')
        print('3. Update User data.')
        print('4. Delete user info.')
        print('5. Exit the app.')
        print('6. Any User details.__')
        choice = input('Enter the option:__')
        
        if choice == '1':
          list_all_user()
        elif choice == '2':
            add_new_user(user_id,user_name,user_country)
        elif choice == '3':
            user_id_1 = int(input('User id to update__'))
            user_name_1 = input('Enter new user name __')
            user_country_1 = input('Enter new user country __')
            update_user_data(user_id_1,user_name_1,user_country_1)
        elif choice == '4':
            user_id_2 = int(input('Enter the id to delete__'))
            delete_data(user_id_2)
        elif choice == '5':
            break
        elif choice == '6':
            user_id_3 = int(input('Enter user id to get details__'))
            user_details(user_id_3)
        else:
            print('Enter valid Option.')
    
    
    



if __name__ == '__main__':
    main()
