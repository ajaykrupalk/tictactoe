def play():
  grid={'1':' ','2':' ','3':' ',
        '4':' ','5':' ','6':' ',
        '7':' ','8':' ','9':' '}
  turn='X'#starts off with X
  count=0#counts the number of moves
  for i in range(10):
    print("\n-----"+turn+"'s turn-----")
    move=input('\nEnter a number b/w 1&9: ')
    if grid[move]==' ':#if the space is empty
      grid[move]=turn#store the X or O
      count+=1#increement the number of moves
      display(grid)#display the updated grid
    else:
      continue
    if count>=5:#only after 5 moves a prediction of win or loss can be made
      valid(grid,turn)
    if count==9:#if all the spaces are full, it's a tie
      print("It's a tie! Better luck next time")
    turn=decide_turn(turn)

def valid(grid,turn):
  if grid['1']==grid['2']==grid['3']!=' ':#upper row
    print("-----"+turn+" has won-----")
    exit()
  elif grid['4']==grid['5']==grid['6']!=' ':#middle row
    print("-----"+turn+" has won-----")
    exit()
  elif grid['7']==grid['8']==grid['9']!=' ':#below row
    print("-----"+turn+" has won-----")
    exit()
  elif grid['1']==grid['4']==grid['7']!=' ':#first column 
    print("-----"+turn+" has won-----")
    exit()
  elif grid['2']==grid['5']==grid['8']!=' ':#second column
    print("-----"+turn+" has won-----")
    exit()
  elif grid['3']==grid['6']==grid['9']!=' ':#third column
    print("-----"+turn+" has won-----")
    exit()
  elif grid['1']==grid['5']==grid['9']!=' ':#left to right diagonal
    print("-----"+turn+" has won-----")
    exit()
  elif grid['3']==grid['5']==grid['7']!=' ':#right to left diagonal
    print("-----"+turn+" has won-----")
    exit()
  
def decide_turn(turn):
  if turn=='X':
    return 'O'
  else:
    return 'X'

def display(grid):
  print()
  print("  "+grid['1']+" | "+grid['2']+" | "+grid['3'])
  print("-------------")
  print("  "+grid['4']+" | "+grid['5']+" | "+grid['6'])
  print("-------------")
  print("  "+grid['7']+" | "+grid['8']+" | "+grid['9'])

play()
