import pandas as pd
matches= pd.read_csv('matches.csv')
deliveries=pd.read_csv('deliveries.csv')
def allteams():
      uteams=matches.loc[:,'team1']
      rteams=[]
      for i in uteams:
          if i in rteams:
              continue
          else:
              rteams.append(i)
      return rteams
print('''Welcome to IPL dataset analysis!
      What do you want me to show based on all the matches of IPL till 2024:-
      1. Check home ground stats of a particular team
      2. See the standings of all the teams in a particular season
      3. Check all the information of a match using match id
      4. Check the most wins
      5. Check the result of a match''')
ch= int(input('enter your choice:-  '))
if (ch==1):
    rteams=allteams()
    for i,j in enumerate(rteams):
      print(f"{i+1}   {j}")
    ch1=int(input('enter your choice:-   '))
    win=0
    lose=0
    teams=dict(matches.loc[:,'team1'])
    winner={}
    for i in teams:
            if teams[i]==rteams[ch1-1]:
                  winner[i]=matches.loc[i,'winner']
    for i in dict(winner):
         if winner[i]==rteams[ch1-1]:
              win+=1
         else:
              lose+=1
    print(f"wins:  {win}\nloses: {lose}")

elif ch==2:
    year=int(input('enter the year:-   '))
    if (year>=2008 and year<=2024):
        date=matches.date
        winstanding={}
        losestanding={}
        wholestanding={}
        for i in dict(date):
            if (date[i].startswith(str(year))):
                if matches.loc[i,'team1'] in winstanding.keys():
                    if (matches.loc[i,'winner']==matches.loc[i,'team1']):
                        winstanding[matches.loc[i,'team1']]+=1
                    elif (matches.loc[i,'team1'] in losestanding.keys()):
                        losestanding[matches.loc[i,'team1']] += 1
                    else:
                        losestanding[matches.loc[i,'team1']] =1
                else:
                    if (matches.loc[i,'winner']==matches.loc[i,'team1']):
                        winstanding[matches.loc[i,'team1']]=1
                    elif (matches.loc[i,'team1'] in losestanding.keys()):
                        losestanding[matches.loc[i,'team1']] += 1
                    else:
                        losestanding[matches.loc[i,'team1']] =1
        teams=[]
        for i in winstanding:
            teams.append(i)
        for i in losestanding:
            if i not in teams:
                teams.append(i)
        table=pd.DataFrame( index=[teams], columns=['win','lose'])
        for i in winstanding:
            table.loc[i,'win']=winstanding[i]
        for i in losestanding:
            table.loc[i,'lose']=losestanding[i]
        pd.set_option('future.no_silent_downcasting', True)
        newtable=table.fillna(0)
        allnewtable=newtable.sort_values(by='win', ascending=False)
        print(allnewtable)
    else:
        print('invalid year')
elif ch==3:
    id=int(input('Enter the match id:-   '))
    ids=dict(matches.loc[:,'id'])
    for i in ids:
        if ids[i]==id:
            print(matches.loc[i])
elif ch==4:
    wins={}
    winners=matches.loc[:,'winner']
    for i in winners:
        if i in wins.keys():
            wins[i]+=1
        else:
            wins[i]=1
    ranks=pd.Series(wins)
    newranks=ranks.sort_values(ascending=False)
    print('Teams with most wins:-   ')
    l=[]
    for i in range(5):
        l.append((newranks.index[i],newranks.iloc[i]))
    rankings=pd.DataFrame(l,index=[x+1 for x in range(5)],columns=['Team','wins'])
    print(rankings)
elif ch==5:
    year=int(input('Enter the year of the match:-   '))
    dates=dict(matches.loc[:,'date'])
    fildates={}
    for i in dates:
        if dates[i].startswith(str(year)):
            fildates[i]=dates[i]
    fildates=dict(fildates)
    n=1
    print('These matches are found:-  ')
    for i in fildates:
        print(f"{n}  {matches.loc[i,'team1']} v/s {matches.loc[i,'team2']}\n{i}")
        n+=1
    chmatch=int(input('enter the code match you want to display records of:-   '))
    print(matches.loc[chmatch])