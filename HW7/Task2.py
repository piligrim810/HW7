def castomSplit(data):
    return tuple(data.split("="))


print("Enter data")
data = input().split()

tp = tuple(map(castomSplit, data))
