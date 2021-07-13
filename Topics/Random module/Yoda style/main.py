import random
sentence = input().split()
random.seed(43)
random.shuffle(sentence)
' '.join(sentence)
print(' '.join(sentence))
