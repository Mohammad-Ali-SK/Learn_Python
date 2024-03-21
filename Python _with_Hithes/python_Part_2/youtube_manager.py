# Enumerate in python---------------------------0.1)

# x = ('Masala','lemon','ginger')
# y = enumerate(x)
# print(list(y))

# Open FIle in Python---------------------------0.2)
# file = open('text.txt','w')

# try:
#     file.write('Hello')
# finally:
#     file.close()


# Another Method and very easy method--------------------

# with open('tex 
# import json

# Create a new project in python new way---------------
# def load_data():
#     try:
#         with open('youtube.txt', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []
    

# def save_data_helper(videos):
#     with open('youtube.txt', 'w') as file:
#         json.dump(videos,file)
        

# def list_all_videos(videos):
#     print('\n')
#     print("*" * 70)
#     for index, video in enumerate(videos, start=1):
#         print(f'{index}. {video['name']},Duration: {video['time']}')
    
# def add_videos(videos):
#     name = input('Enter video name_')
#     time = input('Enter video time_')
#     videos.append({'name' : name, 'time': time})
#     save_data_helper(videos)

# def update_video(videos):
#     list_all_videos(videos)
#     index = int(input("Enter the video number to update.--"))
#     if 1 <= index <= len(videos):
#         name = input("Enter the new video name.--")
#         time = input('Enter the new video time.--')
#         videos[index-1] = {'name': name, 'time':time}
#         save_data_helper(videos)
#     else:
#         print('Invaild index selected.')
    
# def delete_video(videos):
#     list_all_videos(videos)
#     index = int(input('Enter the video number to be deleted.'))
#     if 1 <= index <= len(videos):
#         del videos[index-1]
#         save_data_helper(videos)
#     else:
#         print('Invaild index selected--')

# def main():
#     videos = load_data()

#     while True:
#         print(f'\n Youtube Manager | choose an option')
#         print('1. List all youtube videos')
#         print('2. Add a youtube videos')
#         print('3. Update a youtube video details')
#         print('4. Delete a youtube video ')
#         print('5. Exit the app !')
#         choice = input('Enter your Choice__')
#         # print(videos)
        
#         match choice:
#             case '1':
#                 list_all_videos(videos)
#             case '2':
#                 add_videos(videos)
#             case '3':
#                 update_video(videos)
#             case '4':
#                 delete_video(videos)
#             case '5':
#                 break
#             case _:
#                 print('Please Enter vaild Choice.')
                
# if __name__ == '__main__':
#     main()