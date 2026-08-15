s = input('Você é macho? (M) ou fêmea (F):').upper()
t = input('Tu estuda de manhã? (M) ou de tarde (V):').upper()

if s == 'M' and t == 'M':
    print('Bom dia, querido!')

elif s == 'M' and t == 'V':
    print('Boa tarde, querido!')

elif s == 'F' and t == 'M':
    print('Bom dia, querida!')

else:
    print('Boa tarde, querida!')