import readchar

# Signal handling: Catch Ctrl-C in Python
# https://code-maven.com/catch-control-c-in-python

def handler(signum, frame):
    msg = 'Digita S para encerrar ou N para continuar: '
    print(msg, end='', flush=True)
    res = readchar.readchar()
    if res == 'S':
        print('')
        exit(1)
    else:
        print('', end='\r', flush=True)
        print(' ' * len(msg), end='', flush=True) # Clear the printed line
        print('    ', end='\r', flush=True)