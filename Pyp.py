def print_board(board):
  print(board['Top-L'] + '|' + board['Top-M'] + '|' + board['Top-R'])
  print('-+-+-')
  print(board['Mid-L'] + '|' + board['Mid-M'] + '|' + board['Mid-R'])
  print('-+-+-')
  print(board['Bot-L'] + '|' + board['Bot-M'] + '|' + board['Bot-R'])
    
def addItem(board,place,item):
  board[place] = item
    
def stroke(turn,board):
  global It
  if turn % 2 ==0:
    print('Now ' + name1 + '`s stroke!')
    print('Put \'X\' on some place: ')
    It = 'X'
  else:
    print('Now ' + name2 + '`s stroke!')
    print('Put \'O\' on some place: ')
    It = 'O'
    
  inp = ''
      
  while inp not in board.keys() or inp in made:
    inp = input('Please type place: ')
    if inp == 'exit': break
    
    
  made.append(inp)
  return inp
    
def checkWin(board):
  winname = ''
    
  if board['Top-L'] == board['Top-M']:  #There we check a rows
    if board['Top-M'] == board['Top-R']:
      if board['Top-R'] == 'X':
        winname = name1
      elif board['Top-R'] == 'O':
        winname = name2
  if board['Mid-L'] == board['Mid-M']:
    if board['Mid-M'] == board['Mid-R']:
      if board['Mid-R'] == 'X':
        winname = name1
      elif board['Mid-R'] == 'O':
        winname = name2
  if board['Bot-L'] == board['Bot-M']:
    if board['Bot-M'] == board['Bot-R']:
      if board['Bot-R'] == 'X':
        winname = name1
      elif board['Bot-R'] == 'O':
        winname = name2
          
  if board['Top-L'] == board['Mid-L']:  # There we check a columns
    if board['Mid-L'] == board['Bot-L']:
      if board['Bot-L'] == 'X':
        winname = name1
      elif board['Bot-L'] == 'O':
        winname = name2
          
  if board['Top-M'] == board['Mid-M']:
    if board['Mid-M'] == board['Bot-M']:
      if board['Bot-M'] == 'X':
        winname = name1
      elif board['Bot-M'] == 'O':
        winname = name2
          
  if board['Top-R'] == board['Mid-R']:
    if board['Mid-R'] == board['Bot-R']:
      if board['Bot-R'] == 'X':
        winname = name1
      elif board['Bot-R'] == 'O':
        winname = name2
          
  if board['Top-L'] == board['Mid-M']: #There we check diagonals
    if board['Mid-M'] == board['Bot-R']:
      if board['Bot-R'] == 'X':
        winname = name1
      elif board['Bot-R'] == 'O':
        winname = name2
          
  if board['Top-R'] == board['Mid-M']: 
    if board['Mid-M'] == board['Bot-L']:
      if board['Bot-L'] == 'X':
        winname = name1
      elif board['Bot-L'] == 'O':
        winname = name2
          
          
  return winname
        
    
theboard = {'Top-L':' ','Top-M':' ','Top-R':' ',
          'Mid-L':' ', 'Mid-M':' ','Mid-R':' ',
          'Bot-L':' ', 'Bot-M':' ', 'Bot-R':' '}
          

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




