# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

first_group = participants_first_group.split('|')
second_group = participants_second_group.split('|')
common = []
for i in range(len(first_group)):
    for n in range(len(second_group)):
        if first_group[i] == second_group[n]:
            common.append(first_group[i])

print('Список общих участников',common)


