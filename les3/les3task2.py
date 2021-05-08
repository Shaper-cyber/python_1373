def accept(name, last_name, year_bir, state, email, teleph):
    return f'{name} {last_name}, {year_bir} года рождения, из города {state}, мой емайл: {email} и телефон {teleph}'


print(accept(name='Дамир', last_name='Арасланов', year_bir=1985, state='Ижевск',
             email='aras@ya.ru', teleph=+7999999999))
