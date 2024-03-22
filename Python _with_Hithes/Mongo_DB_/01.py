from pymongo import MongoClient
# mongodb+srv://mohammadpy:<password>@machinelearning.hbo9rte.mongodb.net/
client = MongoClient("mongodb+srv://mohammadpy:mohammadpy@machinelearning.hbo9rte.mongodb.net/")
db = client["ytmanager"]
video_colection = db['videos']


def list_all_video():
    print("*" * 70)
    all_video = video_colection.find()
    for video in all_video:
        print(f'ID : {video['_id']}, Name : {video['name']}, Time:{video['time']}')

def add_video(name,time,video_id):
    video_colection.insert_one({'_id' : video_id , 'name':name,'time':time})

def update_video(id,name,time):
    video_colection.update_one(
        {'_id':id},
        {"$set":{'name':name,'time':time}}
    )

def delete_video(video_id):
    video_colection.delete_one({'_id':video_id})

def main():
    while True:
        print('\n Youtube Manager || Chosen option.')
        print('1. List all videos')
        print('2. Add videos.')
        print('3. Update videos.')
        print('4. Delete Videos.')
        print('5. Exit the app.')
        choice = input('Enter your option___')
        
        
        if choice == '1':
            list_all_video()
        elif choice == '2':
            name = input('Enter the vid name__')
            time = input('Enter vid time__')
            video_id = input('Enter video id__')
            add_video(name,time,video_id)
        elif choice == '3':
            index = input('Enter the vid id to update__')
            name = input('Enter the vid name__')
            time = input('Enter the vid time __')
            update_video(index,name,time)
        elif choice == '4':
            index = input('Enter the vid id to delete__')
            delete_video(index)
        elif choice == '5':
            break
        else:
            print('Enter the vaild num !!')


if __name__ == '__main__':
    main()