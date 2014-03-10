from glob import glob

soups = glob('./Soups/*.tex')
dishes = glob('./MainDishes/*.tex')
breads = glob('./Breads/*.tex')
dessert = glob('./Dessert/*.tex')

all = soups + dishes + breads + Dessert


def write_inputs(a_glob):
    for i in a_glob:
        f.write('\input{' + i[:-4] + '}\n')

f = file('SkousenLyonCookbook.tex', 'w')

f.write('\input{preamble}')
f.write('\n' * 2)

f.write('\\nosection{Soups}\n')
write_inputs(soups)
f.write('\n')

f.write('\\nosection{Breads}\n')
write_inputs(breads)
f.write('\n')

f.write('\\nosection{Main Dishes}\n')
write_inputs(dishes)
f.write('\n')

f.write('\\nosection{Desserts}\n')
write_inputs(dessert)
f.write('\n')

f.write('\\newpage \n')

f.write('\\printindex \n')

f.write('\end{document}\n')

f.close()
