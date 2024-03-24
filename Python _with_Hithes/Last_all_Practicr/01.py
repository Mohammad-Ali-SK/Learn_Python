
# How to works enumerate------------------------------- 1.0)

# x = ('A','B', 'C')
# c = enumerate(x)
# print(list(c))

# Files opening in python ----------------------------2.0)

# There are two types of file opening.

# file = open('text.txt','w')

# try:
#     file.write('How are you baby')
# finally:
#     file.close()

# Method two open file-----

# with open('text.txt','w') as file:
#     file.write('Helo fr lok')

# Project Youtube Manager -------------------------------3.0)

import json

def load_videos():
    try:
        with open('ytmanage.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_video(videos):
    with open('ytmanager.txt', 'w') as file:
        json.dump(videos,file)

def list_video(videos):
    print('*' * 70)
    print('\n')
    for index, vid in enumerate(videos, start=1):
        print(f'{index}. Name: {vid['name']} Duration : {vid['time']}')

def add_video(videos):
    name = input('Enter the vid name__')
    time = input('Enter the vid time__')
    videos.append({'name' : name, 'time' :time})
    save_video(videos)

def update_video(videos):
    list_video(videos)
    index = int(input('Enter the id to update __'))
    if 1 <= index <= len(videos):
        name = input('Enter the vid name __')
        time = input('Enter vid time ___')
        videos[index - 1] = {'name':name, 'time': time}
        save_video(videos)
    else:
        print('Enter valid vid Id __')
        

def delete_video(videos):
    list_video(videos)
    index = int(input('Enter the id to update __'))
    if 1 <= index <= len(videos):
       del videos[index - 1]
       save_video(videos)
    else:
       print('Enter valid num to delete__')




def main():
    videos = load_videos()
    while True:
        print(f' \n YouTube manager || Chosen Option')
        print('1. List all youtube video.')
        print('2. Add video.')
        print('3. Update Vidoe')
        print('4. Delete video.')
        print('5. Exit the app .')
        choice = input('Enter your option__')
        match choice:
            case '1':
                list_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('Enter the valid option !!')
                
if __name__ == '__main__':
    main()