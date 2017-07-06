def print_board(board):
  print(board['T-L'] + '|' + board['T-M'] + '|' + board['T-R'])
  print('-+-+-')
  print(board['M-L'] + '|' + board['M-M'] + '|' + board['M-R'])
  print('-+-+-')
  print(board['B-L'] + '|' + board['B-M'] + '|' + board['B-R'])
    
def addItem(board,place,item):
  board[place] = item
    
def stroke(turn,board):
  global It
  if turn % 2 == 0:
    print('Now X`s stroke: ')
    It = 'X'
  else:
    print('Now O`s stroke: ')
    It = 'O'
    
  inp = ''
      
  while inp not in board.keys() or inp in made:
    inp = input()
    if inp == 'exit': break
    
    
  made.append(inp)
  return inp
    
def checkWin(board):
  winname = ''
    
  if board['T-L'] == board['T-M']:  #There we check a rows
    if board['T-M'] == board['T-R']:
      if board['T-R'] == 'X':
        winname = name1
      elif board['T-R'] == 'O':
        winname = name2
  if board['M-L'] == board['M-M']:
    if board['M-M'] == board['M-R']:
      if board['M-R'] == 'X':
        winname = name1
      elif board['M-R'] == 'O':
        winname = name2
  if board['B-L'] == board['B-M']:
    if board['B-M'] == board['B-R']:
      if board['B-R'] == 'X':
        winname = name1
      elif board['B-R'] == 'O':
        winname = name2
          
  if board['T-L'] == board['M-L']:  # There we check a columns
    if board['M-L'] == board['B-L']:
      if board['B-L'] == 'X':
        winname = name1
      elif board['B-L'] == 'O':
        winname = name2
          
  if board['T-M'] == board['M-M']:
    if board['M-M'] == board['B-M']:
      if board['B-M'] == 'X':
        winname = name1
      elif board['B-M'] == 'O':
        winname = name2
          
  if board['T-R'] == board['M-R']:
    if board['M-R'] == board['B-R']:
      if board['B-R'] == 'X':
        winname = name1
      elif board['B-R'] == 'O':
        winname = name2
          
  if board['T-L'] == board['M-M']: #There we check diagonals
    if board['M-M'] == board['B-R']:
      if board['B-R'] == 'X':
        winname = name1
      elif board['B-R'] == 'O':
        winname = name2
          
  if board['T-R'] == board['M-M']: 
    if board['M-M'] == board['B-L']:
      if board['B-L'] == 'X':
        winname = name1
      elif board['B-L'] == 'O':
        winname = name2
          
          
  return winname
        
    
theboard = {'T-L':' ','T-M':' ','T-R':' ',
          'M-L':' ', 'M-M':' ','M-R':' ',
          'B-L':' ', 'B-M':' ', 'B-R':' '}
          

made = []


print('Hello! Welcom to X-O game!')
print()
name1 = input('Enter first player name: ')
name2 = name1
while name2 == name1:
  name2 = input('Enter second player name: ')
print()
print('Great!')
print()
print('Print',end =' ')
for i in theboard.keys():
  print(i, end = ', ')
print(' to stroke.')
print()
print('Game is starting...')
print()


print_board(theboard)

count = 0
win = ''
while count <9:
  strok = stroke(count,theboard)
  if strok == 'exit':
    break
  addItem(theboard, strok, It) 
  print_board(theboard)
  
  win = checkWin(theboard)
  
  if  win != '':
    break
  count +=1
  
if win != '':
  print('Congratulations! ' + win + ' wins!')
else:
  print('Nichya!')




