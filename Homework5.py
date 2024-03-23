my_list =['strawberry', 'banana', 'cherry', 'tomato', 'orange', 'aplle']
print(my_list)
print(my_list[0], my_list[-1], sep=', ')
new_list = []
for x in range(2, 5):
    new_list.append(my_list[x])
print(new_list)
my_list[2] = "watermelon"; print(my_list)

my_dict = {'hospital': 'больница', 'policeman': 'полицейский', 'food': 'еда', 'sword art online': 'мастера меча онлайн'}
print(my_dict)
mini_dict = ('hospital', 'policeman', 'food', 'sword art online') # mini_dict = (set(my_dict.keys())) - способ достать ключи, не выписывая вручную.
print('Я могу перевести следующие слова или сочетания слов с аглиского на русский:', mini_dict, 'выберите любое слово или сочитание.')
user_word = input('')
if user_word in mini_dict:
    print(my_dict[user_word])
else:
    print('Выбранно не верное слово, или в слове допущенна ошибка.') # поигрались и хватит)
my_dict['paper'] = 'бумага'
print(my_dict)
