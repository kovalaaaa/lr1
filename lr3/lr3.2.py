
def find_common_participants(first, second, razdel=','):
   first_ = first.split(razdel)
   second_ = second.split(razdel)
   group = set(first_).intersection(second_)
   return sorted(group)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
razdel = '|'

# TODO Провеьте работу функции с разделителем отличным от запятой
groups = find_common_participants(participants_first_group, participants_second_group, razdel)
print(groups)
