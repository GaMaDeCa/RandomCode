# Small Tic Tac Toe by https://github.com/GaMaDeCa(made in 30 minutes)
print("Small Tic Tac Toe Function\n\n Type 2 numbers between 1 and 3. Anything else may crash.\nExample(the middle of Tic Tac Toe grid): 22")
def tictac(m='         ',v='X'):
    t=lambda x:''.join([f'{m[i*3]}|{m[(i*3)+1]}|{m[(i*3)+2]}\n' for i in range(3)])
    j=[int(c)-1 for c in input(t(0)+f'P={v}\nyx:')]
    m=list(m)
    i=j[1]+(j[0]*3)
    if m[i]==' ':
        m[i]=v
    else:
        return tictac(''.join(m),v)
    if any([all(n==v for n in m[i:i+3]) for i in range(0,9,3)]) or any([all(n==v for n in (m[i]+m[i+3]+m[i+6])) for i in range(3)]) or m[0]+m[4]+m[8]==v*3 or m[2]+m[4]+m[6]==v*3:
        print(f'{t(0)} {v} is the winner! 😄')
        return 0
    elif not ' ' in m:
        print('#Draw ;_;')
        return 1
    return tictac(''.join(m),'O' if v=='X' else 'X')
  
drawGame=tictac()
#print(drawGame)