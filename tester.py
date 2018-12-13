"""Read/Write test"""

from operator import itemgetter

text_a = open("Text.txt", "w+")
text_r = open("Text.txt", "r")

Player1 = {"name":"Player1", "score":8}
Player2 = {"name":"Player5", "score":5}
Player3 = {"name":"Player4", "score":4}
Player4 = {"name":"Player2", "score":2}
Player5 = {"name":"Player7", "score":7}

listing= [Player1, Player2, Player3, Player4, Player5]

print(Player1)
print(Player2)

for iter_num in range(5):
    for idx in range(iter_num):
        if listing[idx]["score"] > listing[idx+1]["score"]:
            temps = listing[idx]["score"]
            tempn = listing[idx]["name"]
            listing[idx]["score"] = listing[idx+1]["score"]
            listing[idx]["name"] = listing[idx+1]["name"]
            listing[idx+1]["score"] = temps
            listing[idx+1]["name"] = tempn

listing = list(reversed(listing))

"""
newlist = newlist = sorted(listing, key=itemgetter("score"), reverse=True)
"""
print("score  name")
for inte in range(5):
    score1 = listing[inte]["score"]
    name = listing[inte]["name"]
    print (score1, "    ", name)
