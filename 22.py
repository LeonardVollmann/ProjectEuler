letter_dict = {c:i+1 for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
names = sorted(open("22.txt", "rb").read().translate(None, "\"").split(","))
scores = [sum(map(letter_dict.get, name)) for name in names]
print(sum([score * (index+1) for index, score in enumerate(scores)]))