# Create youtube manager using DB-----

# import sqlite3

# conn = sqlite3.connect('youtube_videos.db')

# cur = conn.cursor()

# cur.execute('''
#             CREATE TABLE IF NOT EXIXTIS VIDEOS (
                
#             )
            
# ''')

# def list_all_videos(videos):
#     pass

# def add_video(name,time):
#     pass

# def main():
#     while True:
#         print('\n YouTube manager app with DB')
#         print('1. List VIdeos.')
#         print('2. Add videos.')
#         print('3. Update VIdoes.')
#         print('4. Delete Videos.')
#         print('5. Exit app.')
       
#         choice = input('Enter your choice.')
        
#         if choice == '1':
#             list_all_videos()
#         elif choice == '2':
#             name = input('Enter the video name.__')
#             time = input('Enter the video time.__')
#             add_video(name,time)
     





# if __name__ == '__main__':
#     main()

import json

def load_video():
    try:
        with open('text.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open('text.txt', 'w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print('*' * 70)
    print('\n')
    for index, vid in enumerate(videos, start=1):
        print(f'{index}, {vid['name']}, Duration : {vid['time']} ')
    
def add_video(videos):
    name = input('Enter the video name : ')
    time = input('Enter the v time : ')
    videos.append({'name':name, 'time': time})
    save_data(videos)
def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the num to update : _'))
    if 1 <= index <= len(videos):
        name = input('Enter the new video name : ')
        time = input('Enter the new vid time : - ')
        videos[index-1] = {'name':name, 'time':time}
        save_data(videos)
    else:
        print('Please enter the vaild num !!')
def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the vid num to deleted : _'))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data(videos)
    else:
        print('Please enter the vaild num to delete !!')



def main():
    videos = load_video()
    while True:
        print('\n Youtube Video Manager || Chosen option.')
        print('1. List all youtube videos.')
        print('2. Add youtube videos.')
        print('3. Update video.')
        print('4. Delete video.')
        print('5. Exit the app.')
        choice = input('Enter your choice.')
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('please enter the vaild Option')

if __name__ == '__main__':
    main()