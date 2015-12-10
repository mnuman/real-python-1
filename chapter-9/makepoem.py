import random
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = [ "furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

def selectn(list,n):
    selection = []
    while (len(selection) != n):
        w = random.choice(list)
        if w not in selection:
            selection.append(w) 
    return selection
    
def makePoem():
    """Choose random words from the appropriate list using the random.choice() function,
storing each choice in a new string. Select three nouns, three verbs, three adjectives,
one adverb, and two prepositions. Make sure that none of the words are repeated.
(Hint: Use a while loop to repeat the selection process until you get a new word.)
"""
    my_nouns = selectn(nouns,3)
    my_verbs = selectn(verbs,3)
    my_adj   = selectn(adjectives,3)
    my_adverb= selectn(adverbs,1)
    my_prepo = selectn(prepositions,2)

    """
    {A/An} {adjective1} {noun1}
    2
    3 {A/An} {adjective1} {noun1} {verb1} {preposition1} the {adjective2}
    {noun2}
    4 {adverb1}, the {noun1} {verb2}
    5 the {noun2} {verb3} {preposition2} a {adjective3} {noun3}
    """
    print "{} {} {}".format("A",my_adj[0],my_nouns[0])
    print ""
    print "{} {} {} {} {} the {} {}".format("A",my_adj[0], my_nouns[0], my_verbs[0], my_prepo[0], my_adj[1], my_nouns[1])
    print "{}, the {} {}".format(my_adverb[0], my_nouns[0], my_verbs[1])
    print "the {} {} {} a {} {}".format(my_nouns[1], my_verbs[2], my_prepo[1], my_adj[2], my_nouns[2])
makePoem()    
