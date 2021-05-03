ratings = [7, 5, 3, 3, 2]
j = 0
for j in range(3):
    number_rating = float(input('Введите новый элемент рейтинга'))
    if number_rating <= (ratings[0]) and number_rating > (ratings[-1]):
            i = -1
            while (number_rating) > (ratings[i]):
                i -= 1
            i += 1
            ratings.insert(i, number_rating)
    elif number_rating <= (ratings[-1]): ratings.append(number_rating)
    elif number_rating > (ratings[0]): ratings.insert(0, number_rating)
    print(ratings)
    j+=1

