import requests

# def fetch_random_user():
#     url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
#     response = requests.get(url)
#     whole_data = response.json()

#     if whole_data["success"] and "data" in whole_data:
#         user_data = whole_data["data"]
#         username = user_data["login"]["username"]
#         country = user_data["location"]["country"]
#         return username, country
#     else:
#         raise Exception("Failed to fetch user data")

# def main():
#     try:
#         username , country = fetch_random_user()
#         print(f"Username: {username} \nCountry: {country}")
#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()



# def fetch_random_quotes():
#     url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
#     response = requests.get(url)
#     complete_data = response.json()

#     if complete_data["success"] and "data" in complete_data:
#         user_data = complete_data["data"]
#         id = user_data["id"]
#         author = user_data["author"]
#         length = user_data["length"]
#         date = user_data["dateAdded"]
#         return id, date, author, length
#     else:
#         raise Exception("Fetching error.")

# def main():
#     try:
#         id, date, author, length = fetch_random_products()
#         print(f"ID: {id} \nDate_add: {date} \nAuthor:{author} \nNo. of words: {length}")
#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()



import random 

def fetch_random_products():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos?page=1&limit=10&query=javascript&sortBy=keep%20one%3A%20mostLiked%20%7C%20mostViewed%20%7C%20latest%20%7C%20oldest"
    response = requests.get(url)
    complete_data = response.json()

    if complete_data["success"] and "data" in complete_data:
        user_data = complete_data["data"]["data"]
        random_video = random.choice(user_data)
        publish_data = random_video["items"]["snippet"]["publishedAt"]
        video_title = random_video["items"]["snippet"]["title"]
        return video_title, publish_data
    else:
        raise Exception("Error Occured.")

def main():
    try:
        title, date =  fetch_random_products()
        print(f"Title of the video is: {title} \nPublished at: {date}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()



















