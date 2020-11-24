import pandas as pd
import numpy as np
import scipy.stats.distributions as sp
import sys


def arrume(path):
    skip = 0
    temp = pd.read_csv(path)
    for r in range(len(temp['Season'])):
        if temp['Season'][r] == 2020:
            skip = r
            break

    df = pd.read_csv(path, skiprows=skip, index_col=False)
    df.to_csv(path, index=False, header=['Country', 'League', 'Season', 'Date', 'Time', 'HomeTeam',
                                         'AwayTeam', 'FTHG', 'FTAG', 'Res', 'PH', 'PD', 'PA', 'MaxH', 'MaxD', 'MaxA', 'AvgH', 'AvgD', 'AvgA'])
    val = pd.read_csv(path)
    return val


try:
    val1 = str(sys.argv[1])
    print(val1)
except:
    val1 = input('digite a liga')

if val1 == 'b':
    #Bundesliga

    val = pd.read_csv(r'C:\Users\Dell\Downloads\D1.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\D12019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'p':
    #Liga portuguesa

    val = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\P1.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\P12019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'b2':
    #Bundesliga 2

    val = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\D2.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\D22019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 't':
    #Liga Turca

    val = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\T1.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\T12019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'g':
    #Liga Grega

    val = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\G1.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\G12019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'Be':
    #Liga Belga

    DF1 = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\B1.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\B12019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'h':
    #liga Holandesa

    DF1 = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\N1.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\N12019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'e':

    #liga espanha primeira divisão

    val = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\SP1.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\SP12019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'e2':
    #liga espanha segunda divisão

    val = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\SP2.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\SP22019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'i':

    #primeira divisão italia

    val = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\I1.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\I12019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'i2':
    #segunda divisão italia

    val = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\I2.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\documentos\I22019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'pl':
    # PL (Premier League)

    val = pd.read_csv(r'C:\Users\Dell\Downloads\documentos\E0.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\E02019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)

elif val1 == 'ch':
    #Championship

    val = pd.read_csv(r'C:\Users\Dell\Downloads\E1.csv')
    #DF2=pd.read_csv(r'C:\Users\Dell\Downloads\E12019.csv')
    #val=DF1.append(DF2,ignore_index=True,sort=False)
elif val1 == 'bras':

    val = arrume(r'C:\Users\Dell\Downloads\BRA(2).csv')

elif val1 == 'arg':

    val = arrume(r'C:\Users\Dell\Downloads\ARG.csv')

away_total_goals = val['FTAG']
home_total_goals = val['FTHG']
cont, game_played = 0, 0
teams, games_home, games_away = [], [], []
for r in val["HomeTeam"]:
    if r.lower() in teams:
        pass
    else:
        teams.append(r.lower())
valor_gol = 0
valor_gol1 = 0
gol_teams_home, gol_teams_away, gol_conced_home, gol_conced_away = [], [], [], []
for l in teams:
    for r in range(len(val["HomeTeam"])):
        if (val['HomeTeam'][r].lower()) == l.lower():
            valor_gol = val["FTHG"][r]
            valor_gol1 = valor_gol1+valor_gol
    gol_teams_home.append(valor_gol1)
    valor_gol1 = 0

for l in teams:
    for r in range(len(val["HomeTeam"])):
        if (val['AwayTeam'][r].lower()) == l.lower():
            valor_gol = val["FTAG"][r]
            valor_gol1 = valor_gol1+valor_gol
    gol_teams_away.append(valor_gol1)
    valor_gol1 = 0

for l in teams:
    for r in range(len(val["HomeTeam"])):
        if (val['HomeTeam'][r].lower()) == (l.lower()):
            valor_gol = val["FTAG"][r]
            valor_gol1 = valor_gol1+valor_gol
    gol_conced_home.append(valor_gol1)
    valor_gol1 = 0

for l in teams:
    for r in range(len(val["HomeTeam"])):
        if (val['AwayTeam'][r].lower()) == l.lower():
            valor_gol = val["FTHG"][r]
            valor_gol1 = valor_gol1+valor_gol
    gol_conced_away.append(valor_gol1)
    valor_gol1 = 0

for l in teams:
    for r in range(len(val['HomeTeam'])):
        if (val['HomeTeam'][r].lower()) == (l.lower()):
            game_played = game_played+1
    games_home.append(game_played)
    game_played = 0
games_home = np.array(games_home)

for l in teams:
    for r in range(len(val["HomeTeam"])):
        if (val["AwayTeam"][r].lower()) == l.lower():
            game_played = game_played+1
    games_away.append(game_played)
    game_played = 0
games_away = np.array(games_away)

avg_away_goal = np.mean(away_total_goals)
avg_home_goal = np.mean(home_total_goals)

gol_conced_away = (np.array(gol_conced_away)/games_away)/avg_home_goal
gol_conced_home = (np.array(gol_conced_home)/games_home)/avg_away_goal

gol_teams_away = (np.array(gol_teams_away)/games_away)/avg_away_goal
gol_teams_home = (np.array(gol_teams_home)/games_home)/avg_home_goal
prob_win, prob_draw, prob_lose, prob_big, prob_under, prob_und, prob_ov, prob_both, prob_none = 0, 0, 0, 0, 0, 0, 0, 0, 0

team_home, team_away = 'a', 'a'

print(teams)
print("digite q para sair")

while team_home != 'q' or team_away != 'q':

    team_home = input("Digite o Time que joga em casa").lower()

    if team_home == 'q':
        break
    else:
        pass

    team_home_str = team_home
    team_home = teams.index(team_home)

    team_away = input("Digite o Time Visitante").lower()
    if team_away == 'q':
        break
    else:
        pass

    team_away_str = team_away
    team_away = teams.index(team_away)

    mi_team_home = avg_home_goal * \
        (gol_conced_away[team_away])*(gol_teams_home[team_home])
    mi_team_away = avg_away_goal * \
        (gol_conced_home[team_home])*(gol_teams_away[team_away])
    print("As probabilidades de resultado para o jogo " +
          teams[team_home]+'-' + teams[team_away], "\n")
    maximj, maximk = 0, 0
    maximin = 0
    for j in range(7):
        result_gol_home = sp.poisson.pmf(j, mi_team_home)
        for k in range(7):
            prob = result_gol_home*(sp.poisson.pmf(k, mi_team_away))
            if prob > maximin:
                maximj = j
                maximk = k
                maximin = prob
            if (j > k):
                prob_win = prob+prob_win
            elif (j == k):
                prob_draw = prob+prob_draw
            elif (j < k):
                prob_lose = prob+prob_lose
            if j+k > 2.5:
                prob_big = prob+prob_big
            elif j+k < 2.5:
                prob_under = prob+prob_under
            if j+k > 3.5:
                prob_ov = prob+prob_ov
            elif j+k < 3.5:
                prob_und = prob+prob_und
            if j > 0.5 and k > 0.5:
                prob_both = prob+prob_both
            else:
                prob_none = prob+prob_none

    print("probabilidade - de 2.5 gols", str(prob_under)
          [:8], '---5%-----', 1.05/prob_under, '\n')
    print("probabilidade + de 2.5 gols", str(prob_big)
          [:8], '-----5%----', 1.05/prob_big, '\n')
    print("probabilidade - de 3.5 gols", str(prob_und)
          [:8], "-------5%-------", 1.05/prob_und, '\n')
    print("probabilidade + de 3.5 gols", str(prob_ov)
          [:8], "-----5%-------", 1.05/prob_ov, "\n")
    print("probabilidade do clube: " + team_home_str + " de ganhar ",
          str(prob_win)[:8], '------5%-----', 1.05/prob_win, '\n')
    print("probabilidade empate", str(prob_draw)[
          :8], '-----5$------', 1.05/prob_draw, '\n')
    print("probabilidade do clube: " + team_away_str + " de ganhar",
          str(prob_lose)[:8], '------5%-------', 1.05/prob_lose, '\n')
    print("Probabilidade para ambos marcarem é", str(prob_both)
          [:8], '---------5%--------', 1.05/prob_both, '\n')
    print("Probabilidade para ambos não marcarem é", str(prob_none)
          [:8], '---------5%--------', 1.05/prob_none, '\n')
    print(str(maximj)+'-', str(maximk)+'  '+str(maximin))
    print(teams)
    prob_win, prob_lose, prob_draw, prob_big, prob_under, prob_ov, prob_und, prob_both, prob_none = 0, 0, 0, 0, 0, 0, 0, 0, 0
print("Tchau!!!")
