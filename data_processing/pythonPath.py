import os

pythonpath = os.environ.get('PYTHONPATH')

if pythonpath:
    print(f'A variável de ambiente PYTHONPATH está definida como: {pythonpath}')
else:
    print('A variável de ambiente PYTHONPATH não está definida.')
