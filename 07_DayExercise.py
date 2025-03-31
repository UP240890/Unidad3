# Exercises: Level 1#
#exercises1#
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#exercises2#
print(f"The lenght of it companies is {len(it_companies)}")
#exercises3#
it_companies.add("Twitter")
print(it_companies)
#exercises4#
it_companies.update(["Youtube","Linux","Opera"])
print(it_companies)
#exercise5#
it_companies.discard("Youtube")
print(it_companies)
print("The discard() method removes the specified element from the set. Unlike the remove() method, discard() does not raise an error if the specified element is not present.")
# Exercises: Level 2#
#exercises1#
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#exercises2#
C = A.union(B)
print(C)
#exercises3#
print(A.intersection(B))
print(A.isdisjoint(B))
#exercises4,5,6#
AB = A.union(B)
BA = B.union(A)
print(AB,BA)
print(A.symmetric_difference(B))
#exercises7#
del A,B
# Exercises: Level 3#
#exercises1#
age_list = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age_list)

#exercises2#
if len(age_set) == len(age_list):
    print('The set and the list are equal')

elif len(age_set) > len(age_list):
    print('Set is bigger')

else:
    print('List is bigger')

'''
String: Text-based data.
List: Ordered, mutable collection of items.
Tuple: Ordered, immutable collection of items.
Set: Unordered collection of unique items.

'''

sentence = 'I am a teacher and I love to inspire and teach people'
words = set(sentence.split())
print(f'The number of unique words is {len(words)}')