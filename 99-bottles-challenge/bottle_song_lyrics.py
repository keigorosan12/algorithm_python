def bottle_song_lyrics(number):
    for i in range(number,0,-1):
        if i == 1:
            print("{} bottles of beer on the wall, {} bottle of beer.".format(i,i))
        else:
            print("{} bottles of beer on the wall, {} bottles of beer.".format(i,i))
        
        val = i - 1
        if val == 0:
            print("Take one down, pass it around, no more bottles of beer on the wall!")
            break
        elif val == 1:
            print("Take one down, pass it around, {} bottle of beer on the wall! \n".format(val))
        else:
            print("Take one down, pass it around, {} bottles of beer on the wall! \n".format(val))