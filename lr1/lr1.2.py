# TODO Найдите количество книг, которое можно разместить на дискете
simv_1_bait = 4
simv = 25
stroki = 50
stranic = 100
All_V_mbait = 1.44

V_1book = (simv_1_bait*simv*stroki*stranic)/1024**2
All_book = int(All_V_mbait//V_1book)
print("Количество книг, помещающихся на дискету:", All_book)