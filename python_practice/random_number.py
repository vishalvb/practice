#random number generation

import random

value = random.random()
print('random value is ', value)

value = random.uniform(1,10)
print('using random.uniform', value)

value = random.randint(1,6)
print('using random.int', value) 

my_list = ['hi', 'hello', 'how areyou', 'welcome']
print('using random.choice', random.choice(my_list))

colors = ['red', 'green', 'blue']
print('using random.choices', random.choices(colors, weights = [1,1,1], k=10))

deck = list(range(1,53))
print('deck is', deck)
random.shuffle(deck)
print('after shuffle', deck)

print('using random.sample', random.sample(deck, k = 5))