# Exercício 1

# Crie um jogo que embaralhe uma palavra e a mostre ao jogador. O objetivo dele é
# acertar a palavra em no máximo 5 tentativas. Informe sempre quantas tentativas ele
# ainda tem. Se ele acertar, dê os parabéns; se errar dê uma palavra de ânimo (de
# preferência não fixa). Ao final, mostre a palavra correta e o número de tentativas que
# ele utilizou.

# Exercício 2
# Incluir escolha de temas para as palavras (cidades, cores, times, países, objetos, etc.)
# e níveis de dificuldade (ex: iniciante, intermediário, avançado).

from random import shuffle, choice

# Temas
cities = ["New York", "London", "Tokyo", "Paris", "Sydney", "Rome", "Dubai", "Moscow", "Toronto", "Berlin", "Cairo", "Mumbai", "Rio de Janeiro", "Seoul", "Amsterdam"]
countries = ["United States of America", "United Kindom", "Japan", "France", "Australia", "Italy", "UAE", "Russia", "Canada", "Germany", "Egypt", "India", "Brazil", "South Korea", "Netherlands"]

theme = int(input("Tema de palavras:(cidades = 1; países = 2): "))
difficulty = int(input("Qual a dificuldade das palavras?(iniciante = 1; intermediário = 2; avançado = 3): "))

# 1, 2, 3
def choose_word(theme, dif):
  if theme == 1:
    theme = cities
  elif theme == 2:
    theme = countries

  if dif == 1:
    arr = [word for word in theme if len(word) < 5]
    return choice(arr)
  elif dif == 2:
    arr = [word for word in theme if len(word) >= 5 and len(word) <= 8]
    return choice(arr)
  elif dif == 3:
    arr = [word for word in theme if len(word) > 8]
    return choice(arr)

def shuffled_word(word):
  word = list(word)
  shuffle(word)
  return ''.join(word)

word = choose_word(theme, difficulty)
shuffled = shuffled_word(word)
loop, chances, attempts = True, 3, 0

while loop == True:
  print(f"A palavra é {shuffled}, você tem {chances} tentativa(s)")
  chance = input("Tentativa: ")
  chances -= 1
  attempts += 1
  if chance != word and chances != 0:
    print(f"Errado! Tente novamente, você ainda tem {chances} tentativa(s)\n")
  elif chance != word and chances < 1 :
    print("Suas tentaivas acabaram! :(\n")
    loop = False
  elif chance == word:
    print("Você acertou! Parabéns!\n")
    loop = False
print(f"Palavra correta: {word}")
print(f"Número de tentativas utilizadas: {attempts}")