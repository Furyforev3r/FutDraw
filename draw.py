import numpy as np
import pandas as pd
import random


def draw(teams):

    random.shuffle(teams)

    teamsPoint = len(teams) // 2

    homeTeams = teams[:teamsPoint]
    awayTeams = teams[teamsPoint:]

    dataframe = pd.DataFrame(data={'- Home': homeTeams, '-': 'x',  '- Away': awayTeams})

    return dataframe
