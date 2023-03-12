name = 'Obi-Wan'
day = 'Today'
print(f'Good day {name}! {day} is a perfect day to learn some Python.')
phrase = 'Good day {}! {} is a perfect day to learn some Python.'
print(phrase.format(name, day))
print('Good day %s! %s is a perfect day to learn some Python.' % (name, day))