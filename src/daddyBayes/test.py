from coalas import csvReader as c 
from sklearn.metrics import accuracy_score

c.importCSV('s.csv')
print(f'{c.col.BOLD}Accuracy{c.col.ENDC}')
print(f'Trained: {accuracy_score(c.trained,c.naiveB)}')
print(f'Best: {accuracy_score(c.trained,c.Best)}')
print(f'Worst: {accuracy_score(c.trained,c.Worst)}')

