import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute(''' 
            CREATE TABLE IF NOT EXISTS videos(
                Id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
                
            )
''')


def list_videos():
    pass

def add_video(name,time):
    pass

def update_video(vid_id,name,time):
    pass

def delete_video(vid_id):
    pass


def main():
    while True:
        print(f' \n YouTube manager || Chosen Option')
        print('1. List all youtube video.')
        print('2. Add video.')
        print('3. Update Vidoe')
        print('4. Delete video.')
        print('5. Exit the app .')
        choice = input('Enter your option__')
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input('Enter the vid name__')
            time = input('Enter the vid time__')
            add_video(name,time)
        elif choice == '3':
            vid_id = int(input('Enter the vid id__:'))
            name = input('Enter the vid name_')
            time = input('Enter the vid time___')
            update_video(vid_id,name,time)
        elif choice == '4':
            vid_id = int(input("Enter the vid id to delete___"))
            delete_video(vid_id)
        elif choice == '5':
            break
        else:
            print('Enter the valid option__')
            

if __name__ == '__main__':
    main()
