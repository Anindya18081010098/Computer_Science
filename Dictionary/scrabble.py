letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
zipped = zip(letters,points)
letter_to_points = {key:val for key, val in zipped}
letter_to_points[' ']=0
def score_word(word):
  score = 0
  for letter in word:
    letter = letter.upper()
    score += letter_to_points.get(letter, 0)
  return score
print(score_word('BROWNIE'))
player_to_words = {'player1':['BLUE','TENNIS', 'EXIT'], 'wordNerd':['EARTH','EYES','MACHINE'], 'Lexi Con': ['ERASER','BELLY', 'HUSKY'], 'Prof Reader':['ZAP', 'COMA', 'PERIOD']}
print(player_to_words)
player_to_points = {}
for key, values in player_to_words.items():
  player_points = 0
  for word in values:
    player_points += score_word(word)
  player_to_points[key]=player_points

print(player_to_points)

def play_word(word, player):
  if player in player_to_words.keys():
    player_to_words[player].append(word)
  else:
    print('There is no player with that name')
  return player_to_words
play_word('ANIN','anin')
print(player_to_words)