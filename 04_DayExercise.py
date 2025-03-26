#exercide1#
print('Thirty\tDays\tOf\tPython\n')
#exercise2#
print('Coding\tfor\tall')
#exercise3#
company='Coding\tFor\tAll'
#exercise4#
print(company)
#exercise5#
print(len(company))
#exercise6#
print(company.upper())#(para mayusculas)#
#exercise7#
print(company.lower())#(para minusculas)#
#exercise8#
print(company.capitalize())#(para la primera letra en mayuscula)#
print(company.title())
print(company.swapcase())
#exercise9#
print(company[0:6])
#exercise10#
print(company.index('Coding'))
#exercise11#
company2=print(company.replace('Coding','Python'))
#exercise12#
print(company.find('Coding'))
#exercise13#
print(company.split(' '))
#exercise14#
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))
#exercise15#
print(company.index('C'))
#exercise16#
print(company.index('A'))
#exercise17#
print(company.rindex('A'))
#exercise18#
index1 = company[0]
index2 = company[10]
print(index1,' - ',index2)
#exercise18#
acro1 = 'TDOP'
#EXERCISE19#
acro2 = 'CFA'
#exercise20#
print(company.index('C'))
#exercise21#
print(company.index('F'))
#exercise22#
print(company.index('l'))
#exercise23#
prhase = 'You cannot end a sentence with because because because is a conjunction'
print(prhase.index('because'))
#exercise24#
print(prhase.rindex('because'))
#exercise25#
print(prhase.replace('because',''))
#exercise26#
print(prhase.index('because'))
#exercise27#
print(prhase.replace('because',''))
#exercise28#
print(company.startswith('coding'))
#exercise29#
print(company.startswith('Coding'))
#exercie30#
dou = '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'
print(dou.replace('&nbsp;',''))
#exercise31#
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) 
#exercise32#
print('Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon', sep='\t#')
#exercise33#
print('I am enjoying this challenge.','I just wonder what is next.',sep='\t#')    
#exercise34#
print('Name\tAge\tCountry\tCity\tAsabeneh\t250\tFinland\tHelsinki')
#exercise35#
radius = 10
area = 3.14 * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result)
#exercise36#
r=8 + 6 
print(r.is_integer(),r)
r=8 - 6 
print(r.is_integer(),r)
r=8 * 6 
print(r.is_integer(),r)
r=8 / 6 
print(r.is_integer(),r)
r=8 % 6
print(r.is_integer(),r)
r=8 // 6 
print(r.is_integer(),r)
r=8 ** 6 
print(r.is_integer(),r)