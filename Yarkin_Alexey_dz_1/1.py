duration  = int(input('Введите количество секунд: '))

if duration < 60:
    print(duration, 'сек')
elif 60 < duration < 3600:
    m = duration // 60
    s = duration % 60
    print(m, 'мин', s, 'сек')
elif 3600 < duration < 86400:
    h = duration // 3600
    m = (duration % 3600) // 60
    s = duration % 60
    print(h, 'час', m, 'мин', s, 'сек')
else:
    d = duration // 86400
    h = (duration % 86400) // 3600
    m = (duration % 3600) // 60
    s = duration % 60
    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
    