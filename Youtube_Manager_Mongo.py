from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("mongodb+srv://YouTube_Manager:*******@cluster0.p67aqtd.mongodb.net/", tlsAllowInvalidCertificates = True)
print(client)
db = client["ytmanager"]
video_collection = db["videos"]

def List_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})

def main():
    while True:
        print("\n YouTube_Manager")
        print("1. List all videos.")
        print("2. Add a video.")
        print("3. update a video.")
        print("4. delete a video.")
        print("5. Exit from the app.")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                List_all_videos()
            case '2':
                name = input("Enter video name: ")
                time = input("Enter video length: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the video id to update: ")
                name = input("Enter video name: ")
                time = input("Enter video length: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the video id to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _ :
                print("Invalid Choice.")

if __name__ == "__main__":
    main()