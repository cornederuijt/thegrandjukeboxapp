import pickle as pk
from question import Question

questionlist = []

questionlist.append(Question("Kies een genre", False ,["Disco", "Rock", "Soul", "Latin", "Nederlandstalig", "Funk", "Top 40"]))

questionlist.append(Question("Kies een artiest", False ,["Stevie Wonder", "Earth wind and fire", "ABBA",
                                          "Amy Whinehouse", "Bruno Mars", "Gloria Estafan", "Queen"]))

#q3 = Question("Wat is jouw guilty pleasure?", True)

questionlist.append(Question("Wat is jouw lievelingskleur?", False, ["Paars", "Blauw", "Zwart", "Roze", "Rood", "Geel"]))

questionlist.append(Question("Wat heb je liever?", False, ["Een paar in de gang",
                                                           "Een vent na middernacht",
                                                           "Iemand om lief te hebben",
                                                           "Een schat",
                                                           "Een goede god"]))

pk.dump(questionlist, open("questionlist.p", "wb"))