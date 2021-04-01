#課題1
def linear_search(search, lists):
    try:
        print(lists.index(search))
    except:
        print(None)

#課題2
def global_linear_search(search, origin):
    print([i for i, x in enumerate(origin) if x == search])


#確認
abc = ['a', 'b', 'c']
linear_search('a', abc)

global_linear_search('a', 'abdcag')      
