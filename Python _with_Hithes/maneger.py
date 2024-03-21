
# Practice------------------------------------------------------- 1.0)



# import json

# def load_data():
#     try:
#         with open('text.txt', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []
    
# def save_data(videos):
#     with open('text.txt', 'w') as file:
#         json.dump(videos,file)


# def list_all_videos(videos):
#     print('\n')
#     print('*' * 70)
#     for index, video in enumerate(videos, start=1):
#         print(f'{index}. {video['name']} , Duration : {video['time']}')

# def add_video(videos):
#     name = input('Enter the video name ---')
#     time = input('Enter the video time ----')
#     videos.append({"name" : name, 'time': time})
#     save_data(videos)

# def update_video(videos):
#     list_all_videos(videos)
#     index = int(input('Enter the video number to update. --'))
#     if 1 <= index <= len(videos):
#         name = input('Enter new video name__')
#         time = input('Enter video time. --')
#         videos[index -1] = {'name' : name, 'time': time}
#         save_data(videos)

# def delete_video(videos):
#     list_all_videos(videos)
#     index = int(input('Enter the video no to delete. --'))
#     if 1 <= index <= len(videos):
#         del videos[index - 1]
#     else:
#         print('Enter vaild video number--!!')



# def main():
#     videos = load_data()
#     while True:
#         print(' \n YouTube video manager || chosen option .')
#         print('1. List all youtube video.')
#         print('2. Add videos.')
#         print('3. Update Video')
#         print('4. Delete Video.')
#         print('5. Exit the app.')
#         choice = input('Enter your choice.--')
        
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
#                 print('Enter Vaild option !')
                
# if __name__ == '__main__':
#     main()