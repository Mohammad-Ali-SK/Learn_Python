from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/mypractice")
db = client['Practice']
colection = db['videos']

def list_all_video():
    print('*' * 70)
    all_video = colection.find()
    for video in all_video:
        print(f'ID : {video['_id']}, Name : {video['name']} Time:{video['time']}')
def add_video(video_id,i_name,i_time):
    colection.insert_one({'_id':int(video_id), 'name':i_name, 'time':i_time})

def update_video(new_id,new_vid,new_time):
    colection.update_one(
        {'_id':new_id},
        {"$set" : {'name':new_vid,'time':new_time}}
    )
    

def delete_video(video_id):
    colection.delete_one({"_id":video_id})


def main():
    while True:
        print('\n Youtube Manage || Chosen Option.')
        print('1. List all youtube video.')
        print('2. Add video.')
        print('3. Update video.')
        print('4. Delete video.')
        print('5. Exit the app')
        choice = input('Enter your choice__')
        
        if choice == '1':
            list_all_video()
        elif choice == '2':
            video_id = input('Enter video id._')
            name = input('Enter video name.__')
            time = input('Enter the video time.__')
            
            add_video(video_id,name,time)
        elif choice == '3':
            new_id = input('Enter vid id to update.__')
            new_videoName = input('Enter the new vid name.__')
            new_time = input('Enter the new vid time.__')
            update_video(new_id,new_videoName,new_time)
        elif choice == '4':
            vid_id = input('Enter vid id to delete._')
            delete_video(vid_id)
        elif choice == '5':
            break
        else:
            print('Enter the vaild option !!')


if __name__ == '__main__':
    main()
            