heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]

print(len(heroes))
heroes.append("black panther")
popped = heroes.pop()
heroes.insert(3, popped)
heroes[1:3] = ["doctor strange"]
print(heroes)
heroes.sort()

print(dir(heroes))
