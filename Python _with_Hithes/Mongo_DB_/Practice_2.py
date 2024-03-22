# import json

# def load_video():
#     try:
#         with open('text.txt', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []
    
# def save_data(videos):
#     with open('text.txt','w') as file:
#         json.dump(videos,file)

# def list_all_videos(videos):
#     print('*' * 70)
#     print('\n')
#     for index,vid in enumerate(videos,start=1):
#         print(f'{index}, {vid['name']}, Duration : {vid['time']}')

# def add_video(videos):
#     name = input('Enter the video name__')
#     time = input('Enter the video time.__')
#     videos.append({'name':name, 'time':time})
#     save_data(videos)

# def update_video(videos):
#     index = int(input('Enter the video id to update__'))
#     if 1 <= index <= len(videos):
#         name = input('Enter the name__')
#         time = input('Enter the new vid tme__')
#         videos[index-1] = {'name':name, 'time':time}
#         save_data(videos)
#     else:
#         print('Enter the thik input__')
# def delete_video(videos):
#    index = int(input('Enter the video id to update__'))
#    if 1 <= index <= len(videos):
#        del videos[index -1]
#        save_data(videos)
#    else:
#        print('Wrong input__')


# def main():
#     videos = load_video()
#     while True:
#         print('\n Youtube Manage || Chosen Option.')
#         print('1. List all youtube video.')
#         print('2. Add video.')
#         print('3. Update video.')
#         print('4. Delete video.')
#         print('5. Exit the app')
#         choice = input('Enter your choice__')
        
#         match choice:
#             case '1':
#                 list_all_videos(videos)
#             case '2':
#                 add_video(videos)
#             case '3':
#                 update_video(videos)
#             case '4':
#                 delete_video(videos)
#             case '5':
#                 break
#             case _:
#                 print('Enter vaild option !!')

# if __name__ == '__main__':
#     main()


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/mypractice")
db = client['Practice']
col = db['videos']

all_vid = col.find()
for i in all_vid:
    print(f'Id : {i['_id']} Name : {i['name']}')
    