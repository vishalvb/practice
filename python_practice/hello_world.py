#python welcome

message = 'Hello World'
print(message)
print(len(message))
print(message[0:5])
print(message[:5])
print(message[6:])
print("lowercase ",message.lower())
print("upper", message.upper())
print("count l", message.count('l'))
print("find l",message.find('l'))

message = message.replace('World','my_World')
print("updated message", message)

add = 'More'

message = '{}, {}.'.format(message,add)
print("New Message",message)
add = 'Less'
message = f'{message.upper()}, {add}.'
print("updated Message",message)
