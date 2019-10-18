import matplotlib.pyplot as plt
import pandas as pd 

a = pd.read_csv('lok_sabha_2019_winners_affidavit.csv')

#print(a.columns)
#print(a['Party'])
parties={}

for i in a.iterrows() :
    print()
    if i[1]['Party'] not in parties.keys() :
        parties[i[1]['Party']]=[]
    parties[i[1]['Party']].append(i[1]['Candidate'])
partiesC={}
for k, v in parties.items()[]:
    partiesC[k]=len(v)
plt.plot(partiesC.keys(),partiesC.values())
plt.show()

 