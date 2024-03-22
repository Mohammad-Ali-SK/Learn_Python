# import requests

# def fetch_freeApi():
#     url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
#     response = requests.get(url)
#     data = response.json()
    
#     if data['success'] and 'data' in data:
#         user_data = data['data']
#         jock_id = user_data['data'][0]['id']
#         jock = user_data['data'][0]['content']
#         return jock_id,jock
#     else:
#         raise Exception('Faild to catch')

# def main():
#     try:
#         jock_id,jock = fetch_freeApi()
#         print(f'{jock},{jock_id}')
#     except Exception as e:
#         print(e)

# if __name__ == '__main__':
#     main()


    
    
    
