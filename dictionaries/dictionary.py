# code example is inspired by google python training
# how can i teach a bot, to take words from a dictionary?
# create a dictionary with vocabulary for the bot
d = { }

# create a small dictionary for language module
d["nouns"] = ("car", "bicycle", "bus")
d["verbs"] = ("do", "get", "drive")
d["adjectives"] = ("green", "big", "small")
d["adverbs"] = ("always", "everywhere", "slowly")
d["prepositions"] = ("under", "next to", "behind")

# create a loop for simple output
for i in sorted(d.keys()):
    print("key: ", i, d[i])


