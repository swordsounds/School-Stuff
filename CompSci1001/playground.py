def thingy(x):
    print(id(x[1]))
    for i in range(0, len(x)):
        x[i] +=100
        
def main():
    scores = [2400, 2500, 2600]
    thingy(scores)
    player = scores[1]
    # print(id(player))
    # thingy(scores)
    print(player)
    print(id(scores[1]), id(player))
main()
        