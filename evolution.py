import random as r
import time as t
chance = 0
creatures = {}
# Template for creature: name: [type(plants, micrabes, animals), genes]
genes = ["Small", "Big", "Energy Efficient", "ATP User", "Glucose User"]
while True:
    if len(creatures) == 0:
        creatures["Creature 1"] = ["Microbe", "Small"]
    else:
        chance = r.randint(1, 10)
        if chance == 1:
            creaturechoice = r.choice(list(creatures))
            print ("{} is now extinct".format(creaturechoice))
            del creatures[creaturechoice]
        else:
            creaturename = "Creature " + str(len(creatures) + 1)
            creatures[creaturename] = []
            print ("{} has now been created".format(creaturename))
            chance = 1
            if chance == 1:
                x = r.choice(list(creatures))
                genesofcrature = list(creatures[x])
                newgene = r.choice(genes)
                if "Big" in genesofcrature and "Small" in genesofcrature:
                    t.sleep(1)
                    choice = r.randint(1, 2)
                    if choice == 1:
                        newgene = "Big"
                        cause = "Small"
                    else:
                        newgene = "Small"
                        cause = "Big"
                    print ("{} has now lost the {} gene cause of the {} gene".format(x, newgene, cause))
                    genesofcrature.remove(newgene)
                elif "ATP User" in genesofcrature and "Glucose User" in genesofcrature:
                    t.sleep(1)
                    choice = r.randint(1, 2)
                    if choice == 1:
                        newgene = "ATP User"
                        cause = "Glucose User"
                    else:
                        newgene = "Glucose User"
                        cause = "ATP User"
                    print ("{} has now lost the {} gene cause of the {} gene".format(x, newgene, cause))
                    genesofcrature.remove(newgene)
                elif newgene in genesofcrature:
                    t.sleep(1)
                    print ("{} has now lost the {} gene".format(x, newgene))
                    genesofcrature.remove(newgene)
                else:
                    t.sleep(1)
                    print ("{} has now have the {} gene".format(x, newgene))
                    genesofcrature.append(newgene)
                creatures[x] = genesofcrature
    t.sleep(1)
