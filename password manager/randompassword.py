def rand_password():
    import random
    import linecache

    rand_adj = random.randint(2 , 229)
    rand_noun = random.randint(233 , 604)
    rand_verb = random.randint(607 , 2110)
    rand_adverb = random.randint(2113 , 2442)

    adjective = linecache.getline('storage/source.txt',rand_adj)
    noun = linecache.getline('storage/source.txt',rand_noun)
    verb = linecache.getline('storage/source.txt',rand_verb)
    adverb = linecache.getline('storage/source.txt',rand_adverb)

    password = str(adjective) + str(noun) + str(verb) + str(adverb)
    password = str.join(' ', password.splitlines())
    password = password.replace(' ', '')
    password = password.lower()

    return password
