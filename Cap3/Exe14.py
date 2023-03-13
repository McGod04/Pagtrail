'''Imagine que em uma escola foi realizada uma pesquisa com o objetivo de levantar 
dados sobre os esportes que os alunos praticam. Ao fim da pesquisa foram criados 4 conjuntos:

Praticantes de vôlei: {'artur', 'bruna', 'david', 'julia', 'max', 'paulo'}
Praticantes de futebol: {'artur', 'cleia', 'david', 'lucas', 'mateus', 'rafael'}
Praticantes de natação: {'bianca', 'cielo', 'cleia', 'lucas', 'phelps', 'tulio'}

Crie um script que retorne as respostas para as seguintes questões:

Alunos que praticam vôlei ou futebol
Alunos que praticam futebol e natação
Alunos que praticam vôlei mas não praticam futebol'''

volei = {'artur', 'bruna', 'david', 'julia', 'max', 'paulo'}
futebol = {'artur', 'cleia', 'david', 'lucas', 'mateus', 'rafael'}
natacao = {'bianca', 'cielo', 'cleia', 'lucas', 'phelps', 'tulio'}

fn = futebol & natacao
fv = futebol | volei
vf = volei - futebol

print(f'Alunos que praticam vôlei ou futebol: {fv}\n')
print(f'Alunos que praticam futebol e natação: {fn}\n')
print(f'Alunos que praticam vôlei mas não praticam futebol: {vf}')
