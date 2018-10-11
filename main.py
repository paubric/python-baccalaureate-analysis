import csv
import matplotlib.pyplot as plt

file = open('2017-09-25-date-deschise-2017-i.csv')
print('[*] Loading data...')
elevi = list(csv.DictReader(file))

# Cat la suta din cei care dau la info sunt fete?
stats = {
    'F': {
        'URBAN': 0,
        'RURAL': 0
    },
    'M': {
        'URBAN': 0,
        'RURAL': 0
    },
    'total':{
        'URBAN': 0,
        'RURAL': 0
    }
}

materii=['Informatica', 'Biologie', 'Chimie', 'Fizica', 'Sociologie', 'Psihologie', 'Geografie', 'Logica']

for materie in materii:
    for elev in elevi:
        if elev['Subiect ed'][:5] == materie[:5]:
            stats[elev['Sex']][elev['Mediu candidat']] += 1
            stats['total'][elev['Mediu candidat']] += 1

    print('[*] Generating figure for', materie)
    fig, ax = plt.subplots(figsize=(16, 9))

    plt.suptitle('Demografica elevilor care au ales ca proba la alegere: '+materie, fontsize=24)
    labels = ['Baieti', 'Fete']

    plt.subplot(121)
    plt.title('Urban')
    plt.pie([stats['M']['URBAN']/stats['total']['URBAN'], stats['F']['URBAN']/stats['total']['URBAN']], labels=labels, autopct='%.2f%%')
    plt.gca().set_aspect('equal', adjustable='box')
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.subplot(122)
    plt.title('Rural')
    plt.pie([stats['M']['RURAL']/stats['total']['RURAL'], stats['F']['RURAL']/stats['total']['RURAL']], labels=labels, autopct='%.2f%%')
    plt.gca().set_aspect('equal', adjustable='box')
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.savefig(materie+'.png', bbox_inches='tight')
