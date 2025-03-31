#exercise1#
import statistics
import math
lst = list()
#exercise2#
sopa=['agua','sal','pasta','verdura','pollo']
#exercise3#
print(len(sopa))
#exercise4#
sopamid=len(sopa) // 2
print(sopa[0], sopa[sopamid], sopa[-1]) 
#exercise5#
MDT=['Jesus', '19', '1.72', 'solo', 'casa'] #MDT=mixed_data_types#
#exercise6#
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#exercise7#
print(it_companies)
#exercise8#
print(len(it_companies))
#exercise9#
it_companiesmid=len(it_companies) // 2
print(it_companies[0],it_companies[it_companiesmid],it_companies[-1])  
#exersie10#
it_companies[0]="Ponos"
print(it_companies)
#exercise11#
it_companies.append("IT")
print(it_companies)
#exercise12#
it_companies.insert(len(it_companies) // 2, "IT")
print(it_companies)
#exercise13#
it_companies[-1]="Github"
print(it_companies)
#exercise14#
hast = "#; ".join(it_companies)
print(hast)
#exercise15#
print("IBM" in it_companies)
#exercise16#
it_companies.sort()
print(it_companies)
#exercise17#
it_companies.reverse()
print(it_companies)
#exercise18,19,20#
print(it_companies[:3])  
print(it_companies[-3:])  
print(it_companies[len(it_companies) // 2 - 1: len(it_companies) // 2 + 1])
#exercise21#
it_companies.pop(0)
print(it_companies)
#exercise22#
it_companiesmid=len(it_companies) // 2
it_companies.pop(it_companiesmid)
print(it_companies)
#exercise23,24#
it_companies.pop(-1)
print(it_companies)
#exercise25#
it_companies.clear()
del it_companies
#exercise26#
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
#exercise27#
all=front_end + back_end
print(all)
#level2#
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

sorted_ages = sorted(ages)
print(sorted_ages)
minimum = min(sorted_ages)
maximum = max(sorted_ages)

print(f"The min value is {minimum}, the max value is {maximum}")


ages.append(minimum)
ages.append(maximum)
print(ages)


median_age = statistics.median(ages)
print(median_age)


average_age = sum(ages) / len(ages)
print(average_age)


age_range = max(ages) - min(ages)
print(age_range)

compare = abs(minimum - average_age) < abs(maximum - average_age)
print(compare)



countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe']

if len(countries) % 2 == 1:
    midValue = len(countries)
    mid2 = int(midValue // 2)
    mid1 = int(midValue // 2) -1
    print(countries[mid1],countries[mid2])
else:
    mid = int(len(countries))
    print(countries[mid])

n = len(countries)
    
if n % 2 == 1:
    middle = [countries[n // 2]]
else:
    middle = [countries[n // 2 - 1], countries[n // 2]]

first_half = countries[: (n + 1) // 2]
second_half = countries[(n + 1) // 2 :]

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
chn, rss, usa, *scandic = countries
print(chn)
print(rss)
print(usa)
print(scandic)