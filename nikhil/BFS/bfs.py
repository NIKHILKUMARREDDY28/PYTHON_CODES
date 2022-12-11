# program to get any my connections with name nani
from collections import deque
search_queue = deque()
visited = []
friends = {}
friends["Nikhil"] = ["Ramgopal varma", "puri jagan"]
friends["Ramgopal varma"] = ["Amitabh","mumbai"]
friends["puri jagan"] = ["Liger","Charmi"]
friends["Amitabh"] = ["Abhishek"]
friends["mumbai"]=["Telugu"]
friends["Liger"] = ["nani"]
friends["Charmi"] = []
friends["Telugu"] =[]
friends["Abhishek"] = []
search_queue += friends["Nikhil"]
while search_queue:
    friend = search_queue.popleft()
    if friend == "nani":
        print("This is nani")
    else:
        search_queue += friends[friend]
    visited.append(friend)
print(visited)
