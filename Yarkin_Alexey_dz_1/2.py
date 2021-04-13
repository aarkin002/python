usr_lst = []
over_sum_first = 0
over_sum_final = 0

for i in range(1, 1001):
    if i % 2 != 0:
        usr_lst.append(i**3)

for i in range(len(usr_lst)):
    sum_i = 0
    over_sum_i = usr_lst[i]
    while over_sum_i > 0:
      sum_i += (over_sum_i % 10)
      over_sum_i = over_sum_i // 10
    if sum_i % 7 == 0:
        over_sum_first += usr_lst[i]

for j in range(len(usr_lst)):
    sum_j = 0
    usr_lst[j] += 17
    over_sum_j = usr_lst[j]
    while over_sum_j > 0:
      sum_j += (over_sum_j % 10)
      over_sum_j = over_sum_j // 10
    if sum_j % 7 == 0:
        over_sum_final += usr_lst[j]
    
print(over_sum_first)
print(over_sum_final)