def dig_pow(n, p):
    n_ = list(str(n))
    count = 0
    for index, elem in enumerate(n_):
        count += int(elem) ** (p + index)
    count_ = count // n
    if count_ * n == count:
        return count_
    return -1


print(dig_pow(46288, 3))
print(dig_pow(92, 1))
dig_pow(46288, 5)
dig_pow(3456789, 1)

# def how_much_i_love_you(nb_petals):
#     word = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
#     return [word[elm % len(word)] for elm in range(nb_petals)][-1]
#
#
# count = 0
# for  i in range(int(input())):
#     count +=1
#     print(str(count) + ':', how_much_i_love_you(i+1))


# def solution(number):
#     count = 0
#     if number < 0:
#         return 0
#     else:
#         for i in range(number):
#             if i % 3 == 0 or i % 5 == 0:
#                 count += i
#     return count
#
#
# print(solution(10))
# print(solution(60))
# print(solution(-10))
# print(solution(0))
# print(solution(6))
# print(solution(3))


# def get_count(sentence: str):
#     sentence = sentence.count('a') + sentence.count('e') + sentence.count('u') + sentence.count('i') + sentence.count(
#         'o') + sentence.count('A') + sentence.count('E') + sentence.count('U') + sentence.count('I') + sentence.count('0')
#     return sentence
#
#
# print(get_count('This website is for losers LOL!'))
# print(get_count('What or you, I communst?'))


# def count_sheeps(sheep):
#     count = 0
#     for i in sheep:
#         if i:
#             count += 1
#     return count


# def disemvowel(string_: str):
#     for i in 'aeiouAEOIU':
#         string_ = string_.replace(i, '')
#
#     return string_


# def find_it(seq):
#     c = 0
#     for i in seq:
#         c += 1
#         da = seq.count(i)
#         if da % 2 != 0:
#             return seq[c - 1]
# return [i for i in seq if seq.count(i) % 2 == 1][0]


# print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))

# 5

# def R(number):
#     if number // 10 == 0:
#         return 0
#     res = 1
#     while (True):
#         res *= number % 10
#         number //= 10
#         if number == 0:
#             break
#     return R(res) + 1
#
#
# print(R(999))


# def number_of_pairs(gloves):
#     count = 0
#     for _ in range(len(gloves)):
#         for elem in gloves:
#             count_ = gloves.count(elem)
#             if count_ % 2 == 0:
#                 count += 1
#             gloves.remove(elem)
#     return count
#
#
# print(number_of_pairs(["red","red"]))
# print(number_of_pairs(["gray","black","purple","purple","gray","black"]))
# print(number_of_pairs(["red","green","blue"]))
# print(number_of_pairs([]))
# print(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]))


# def bears(number_: int, string_: str):
#     pairs, count = '', 0
#     i = 1
#     while i < len(string_):
#         if (string_[i - 1] == 'B' and string_[i] == '8') or (string_[i - 1] == '8' and string_[i] == 'B'):
#             pairs += string_[i - 1] + string_[i]
#             count += 2
#             i += 2
#         else:
#             i += 1
#     return [pairs, count >= number_]
#
#
# print(bears(6, 'EvHB8KN8ik8BiyxfeyKBmiCMj'))
# print(bears(3, '88Bifk8hB8BB8BBBB888chl8BhBfd'))  # ["8BB8B8B88B",True]
# print(bears(7, '8j8mBliB8gimjB8B8jlB'))  # ['8BB88BB88BB88B', False]


# def nines(n):
#     s, l = 0, len(str(n))
#     for i, v in enumerate(str(n)):
#         s *= 9
#         if v == '9':
#             return n - (s + 9) * 9 ** (l - i - 1) + 1
#         s += int(v)
#     return n - s
#
#
# print(nines(3950))


# def each_cons(lst, n):
#     return [lst[elem:elem+n] for elem in range(len(lst) - n + 1)]
#
# print(each_cons([1,2,3,4], 2))


# def between(a,b):
# lst =[]
# start = a
# while start != b + 1:
#     lst.append(start)
#     start += 1
# return lst
# return [number  for number in range(a, b+1)]

# print(between(1, 4))
# print(between(-2, 2))


# def sum_of_differences(arr):
#     arr.sort(reverse=True)
#     return sum([i - j for i, j in zip(arr, arr[1:])])
#
# print(sum_of_differences([1, 2, 10]))
# print(sum_of_differences([]))
# print(sum_of_differences([1]))


# def to_freud(sentence):
#     return ' '.join('sex' for i in sentence.split())
#
# print(to_freud("You're becoming a true freudian expert"))


# def square_or_square_root(arr):
#     return [number ** 0.5 if (number ** 0.5).is_integer() else number ** 2 for number in arr]
#
#
# print(square_or_square_root([4, 3, 9, 7, 2, 1]))


# import base64
#
# def hex_to_base64(hex: str) -> str:
#     decoding = base64.b16decode(hex, casefold=True)
#     encoding = base64.b64encode(decoding).decode('utf-8')
#     return encoding
#
#
# b16 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# b64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
# decoding = base64.b16decode(b16, casefold=True)
# print(decoding)
# decoding = base64.b64encode(decoding)
# print(decoding)
# print(hex_to_base64(b16))


# def array_diff(a, b):
#     lst = list(set(b))
#     for _ in range(len(a)):
#         for elem_1 in a:
#             for elem_2 in lst:
#                 if elem_2 == elem_1:
#                     a.remove(elem_2)
#     return a
#
#
# print(array_diff([1,2,2], [1]))
# print(array_diff([1,2,3], [1, 2]))
# print(array_diff([11, 10, -15, 10, 19], [0, 5, 1, -10, 11, 15, 11]))


# def divisible_count(x, y, k):
#     new = x
#     count = 0
#     for _ in range(y - x + 1):
#         if new % k == 0: count += 1
#         new += 1
#     return count
#
#
#
# print(divisible_count(6, 11, 2))
# print(divisible_count(6, 1121, 2))
# print(divisible_count(6, 12143124, 2))
# print(divisible_count(20, 20, 2))


# def no_space(x):
#     return x.replace(' ', '')
#
#
# print(no_space('8j aam'))


# def grow(arr):
#     a = 1
#     for i in arr:
#         a *= i
#     return a
#
#
# print(grow([1, 2, 3]))


# def even_or_odd(number):
#     if number % 2 == 0: return 'Even'
#     else: return 'Odd'
#     return 'Even' if number % 2 else 'Odd'


# def remove_char(s):
#     return s[1:-1]
#
# print(remove_char('daad'))


# def positive_sum(arr):
#     j = 0
#     for i in arr:
#         if i > 0:
#             j += i
#     return j
#     return sum(x for x in arr if x > 0)
#
#
# print(positive_sum([1, -4, 7, 12]))


# def find_uniq(arr):
#     count = 0
#     for elem in arr:
#         count_ = arr.count(elem)
#         if count_ == 1:
#             return elem
#
#     return [i for i in arr if arr.count(i) == 1][0]
#
#
# print(find_uniq([1, 1, 1, 2, 1, 1]))
# print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
# print(find_uniq([0, 1, 1, 1, 1, 1, 1, 1]))


# def divisible_count(x, y, k):
#     # b = (y // k) + 1
#     # a = (x // k) + 1
#     # print(a, b)
#     # if x % k == 0:
#     #     a -= 1
#     return (y // k) - ((x-1) // k)
#
#
# print(divisible_count(6,11,2))


# def to_jaden_case(string):
#     string = string.split(' ')
#     lst = []
#     for elem in string:
#         if not elem.istitle():
#             b = elem.capitalize()
#             lst.append(b)
#         else:
#             lst.append(elem)
#     return ' '.join(lst)
#     return ' '.join(w.capitalize for w in string.split(' '))
#
# quote = "How can mirrors be real if our eyes aren't real"
#
# print(to_jaden_case(quote))


# def high_and_low(numbers):
#     return str(max(map(int, numbers.split(' ')))) + ' ' + str(min(map(int, numbers.split(' '))))
#
#
# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))


# def fibonacci(n, b):
#     x, y = 0, 1
#     for i in range(n):
#         x, y = y, y + b * x
#     return x
#
#
# print(fibonacci(8, 12))


# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     return numbers[0] + numbers[1]
#
# print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))


# def find_short(s):
#     return len(sorted(s.split(), key=len)[0])
#
#
# a = "bitcoin take over the world maybe who knows perhaps"
# print(find_short(a))


# def filter_list(lst):
#     return [elem for elem in lst if type(elem) == int]
#
# print(filter_list([1, 2, 'a', 'b']))

# a = chr(a)
#


# def alphabet_position(text):
#     dic = {chr(ord('a') + i): str(i + 1) for i in range(26)}
#     text = text.lower()
#     lst = []
#     for elem in text:
#         if elem == ' ' or elem == '.' or elem == "'":
#             continue
#         lst.append(dic[elem])
#     return ' '.join(lst)
# #
# #
# print(alphabet_position("The sunset sets at twelve o' clock."))


# def find_needle(haystack):
#     for elem in haystack:
#         if elem == 'needle':
#             a = haystack.index(elem)
#             # return f'found the needle at position {haystack.index(elem)}'
#     return f'found the needle at position {[haystack.index(elem) for elem in haystack if elem == "needle"][0]}'
#
#
#
#
# print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
# # ('found the needle at position 3')


# def tower_builder(n_floors):
#     a = 1
#     lst = []
#     n_floors -= 1
#     while n_floors > -1:
#         lst_ = ' ' * n_floors + '*' * a + ' ' * n_floors
#         print(lst_)
#         lst.append(lst_)
#         a += 2
#         n_floors -= 1
#     return lst
#
#
# print(tower_builder(3))

# import math
#
# def get_sum(a,b):
#     minim, maxim = min(a, b), max(a, b)
#     sum = minim
#     for i in range(maxim + 1):
#         if sum < maxim:
#             sum += 1
#     return sum


# def get_sum(a, b):
#     if a == b:
#         return b
#     c = 0
#     for n in range(min(a, b), max(a, b) + 1):
#         c += n
#     return c
#
#
# print(get_sum(0, 1))
# print(get_sum(0, -1))


# def invert(lst):
#     return [-elem for elem in lst]
#
# print(invert([1,2,3,4,5]))


# def square_sum(numbers):
#     summa = 0
#     for elem in numbers:
#         summa = elem ** 2 + summa
#     return summa
#     return sum(elem ** 2 for elem in numbers)
#
# print(square_sum([1,2]))


# def is_isogram(string):
#     string = string.lower()
#     for elem in string:
#         if string.count(elem) >= 2 :
#             return False
#     return True
#
#
# print(is_isogram('moOse'))


# def is_narcissistic(n):
#     new_n = str(n)
#     sumir = 0
#     for elem in new_n:
#         sumir += int(elem) ** len(new_n)
#     return sumir == n
#
# print(is_narcissistic(153))


# def digitize(number):
#     return [int(elem) for elem in str(number)][::-1]
#
#
# print(digitize(35231))


# def order(sentence):
#     sentence = sentence.split()
#     new_lst = []
#     count = '1'
#     for _ in sentence:
#         for elem_2 in sentence:
#             if count in elem_2:
#                 new_lst.append(elem_2)
#         count = str(int(count) + 1)
#     return ' '.join(new_lst)
#
#
#
# print(order('4of Fo1r pe6ople g3ood th5e the2'))


# def likes(names):
#     if len(names) == 1: return f'{names[0]} likes this'
#     elif len(names) == 2: return f'{names[0]} and {names[1]} like this'
#     elif len(names) == 3: return f'{names[0]}, {names[1]} and {names[2]} like this'
#     elif len(names) >= 4: return f'{names[0]}, {names[1]} and {len(names) - 2} other like this'
#     return "no one likes this"
#
#
# print(likes([]))
# print(likes(['Jacob', 'Alex']))
# print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
# print(likes(['Alex', 'Jacob', 'Mark', 'Max', 'Dima', 'Petr']))
# print(likes(["Sylia Stingray", "Priscilla S. Asagiri", "Linna Yamazaki", "Nene Romanova", "Nigel",
#              "Macky Stingray", "Largo", "Brian J. Mason", "Sylvie", "Anri", "Leon McNichol", "Daley Wong",
#              "Galatea", "Quincy Rosenkreutz"]))


# def find_multiples(integer, limit):
# a = integer
# lst = []
# while a<=limit:
#     lst.append(a)
#     a += integer
# return lst
# return list(range(integer, limit + 1, integer))

#
# print(find_multiples(5, 25))
# print(find_multiples(4, 24))
# print(find_multiples(1, 2))


# def descending_order(num):
# a = list(str(num))
# a.sort(reverse=True)
# return int(''.join(a))
# return int(''.join(sorted(str(num), reverse=True)))

# a = 1234567890
# a = list(str(a))
# a.sort(reverse=True)
# print(''.join(a))
# print(descending_order(1234567890))


# def DNA_strand(dna):
#     diсt_new = {
#         'A':'T',
#         'T':'A',
#         'C':'G',
#         'G':'C'
#     }
# lst_n = []
# for elem in list(dna):
#     lst_n.append(diсt_new[elem])
# return lst_n
#     return ''.join([diсt_new[elem] for elem in dna])
#
#
# print(DNA_strand("AAAA"))


# def fake_bin(x):
#     return ''.join(['1' if int(elem) >=5 else '0' for elem in list(x)])
#
#
# print(fake_bin('1234567890'))


# def is_pangram(sentence):
#     lookup = [0] * 26
#     sentence = sentence.lower()
#     for char in sentence:
#         if 'a' <= char <= 'z':
#             index = ord(char) - ord('a')
#             lookup[index] += 1
#     return all(lookup)


# import string
#
# def is_pangram(s):
#     return set(string.ascii_lowercase) <= set(s.lower())
#
# print(is_pangram("The quick brown fox jumps over the lazy dog"))


# def is_square(n):
#     # if n == 0:
#     #     return True
#     # elif n == 3:
#     #     return False
#     # elif n >= 0 and int(n) % int(n ** 0.5) == 0:
#     #     return True
#     # return False
#     return n >= 0 and (n**0.5) % 1 == 0
#
# print(is_square(25))
# print(is_square(5))
# print(is_square(0))
# print(is_square(4))
# print(is_square(3))


# def square_digits(num):
#     return int(''.join([str(int(elem) ** 2) for elem in list(str(num))]))
#
# print(square_digits(9119))


# def ghostbusters(building):
#     return ''.join(building.split(' '))
#
# print(ghostbusters('Factor y'))


# def better_than_average(class_points, your_points):
#     return True if sum([elem for elem in class_points]) // len(class_points) <= your_points else False
#     # ИЛИ
#     return your_points > sum(class_points) / len(class_points)
#
#
# print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))
# print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))
# print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))


# def count_positives_sum_negatives(arr):
#     if arr != []:
#         count_1 = 0
#         count_2 = 0
#         lst_ = []
#         for elem in arr:
#             if elem > 0:
#                 count_1 += 1
#             else:
#                 count_2 += elem
#         lst_.append(count_1), lst_.append(count_2)
#         return lst_
#     return arr
#
#
#
# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
# print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# print(count_positives_sum_negatives([]))


# def binary_array_to_number(arr):
#   return int(''.join([str(elem) for elem in arr]), 2)
#
#
# print(binary_array_to_number([0,0,1,0]))


# def duplicate_count(text):
#     return len(sorted({a: list(text.lower()).count(a) for a in set(list(text.lower())) if list(text.lower()).count(a) > 1}))
#
# print(duplicate_count("abcde"))
# print(duplicate_count("Indivisibilities"))
# print(duplicate_count('PJnQe4Z0PEByeI9exqJL3yp2uxGlTSLxWsiUgkMnc8N74gavdynVUYdgBymLsZplfxsSwppv79Qap1k0VMd96muw'))
# print(duplicate_count('ue56V72FZcEwlGY'))


# def add_binary(a,b):
#     return bin(a + b)[2:]
#
# print(add_binary(1, 2))


# def remove_smallest(numbers):
#     numbers.remove(min(numbers))
#     return numbers
#
#
# print(remove_smallest([1, 2, 3, 4, 5]))


# import math
#
# def find_next_square(sq):
#     return (math.sqrt(sq) + 1) ** 2 if math.sqrt(sq) % 1 == 0 else -1
#
#
# print(find_next_square(155))
# print(find_next_square(121))


# def number(bus_stops):
#     peoples = 0
#     # for people in bus_stops:
#     #     peoples += people[0] - people[1]
#     # return peoples
#     return sum([people[0] - people[1] for people in bus_stops])
#
#
# print(number([[10,0],[3,5],[5,8]]))


# def reverse_words(str):
#     return ' '.join(s[::-1] for s in str.split(' '))


# def comp(array1, array2):
#     return sorted([abs(float(elem)) for elem in array1]), sorted([abs(float(elem ** 0.5)) for elem in array2])
#
#
# # a1 = [-121, -144, 19, -161, 19, -144, 19, -11]
# # a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# a1 = [57, 20, 40, 40, 78, 62, 90, 59, 59, 91, 51, 25, 17, 79, 83, 56, 75, 50, 94, 64, 89, 98, 68, 58, 45]
# a2 = [8100, 8281, 7921, 4096, 9604, 3249, 3481, 6241, 625, 5625, 400, 3844, 1600, 290, 6889, 3481, 3136, 2601, 1600, 2025, 6084, 2500, 8836, 4624, 3364]
# print(comp(a1, a2))


# def lovefunc( flower1, flower2 ):
#     # if flower1 % 2 != 0 and flower2 % 2 != 0:
#     #     return False
#     # return True
#     # return False if flower1 % 2 != 0 and flower2 % 2 != 0 else True
#     return True if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0) else False
#
# print(lovefunc(639, 417))
# print(lovefunc(872, 562))


# def get_participants(handshakes):
#     answer = 0
#     sum_ = 0
#     while handshakes > sum_:
#         sum_ = answer * (answer + 1) / 2
#         answer += 1
#     return answer
#
#
# print(get_participants(7))
# print(get_participants(0))


# def high(x):
#     dict_ = {chr(ord('a') + i): int(i + 1) for i in range(26)}
#     lst_x = x.split(' ')
#     lst_new = []
#     for elem in lst_x:
#         list_elem = list(elem)
#         word_sum = 0
#         for sum_ in list_elem:
#             word_sum += dict_[sum_]
#         lst_new.append(word_sum)
#     index_ = lst_new.index(max(lst_new))
#     return lst_x[index_]

# print(high('man i need a taxi up to ubud'))


# def basic_op(operator, value1, value2):
#     return eval(f'{value1} {operator} {value2}')
#
#
# print(basic_op('+', 4, 7))


# def remove_every_other(my_list):
#     return my_list[::2]
#
#
# print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))


# def stray(arr):
#     line = {}
#     for elem in arr:
#         if elem in line:
#             line[elem] += 1
#         else:
#             line[elem] = 1
#     n = min(line, key=line.get)
#     return n


# def move_zeros(arr: list):
#     new_arr = []
#     for elem in range(arr.count(0)):
#         b = arr.pop(arr.index(0))
#         new_arr.append(b)
#     arr.extend(new_arr)
#     return arr
#
# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))


# def duplicate_encode(word: str):
#     lst_ = []
#     word = word.lower()
#     for elem in word:
#         if word.count(elem) > 1:
#             lst_.append(')')
#         else:
#             lst_.append('(')
#     return ''.join(lst_)
#
#
#
# print(duplicate_encode("din"))
# print(duplicate_encode("recede"))
# print(duplicate_encode("Success"))
# print(duplicate_encode('Supralapsarian'))


# def unique_in_order(iterable):
#     str_ = ''
#     lst_ = []
#     for elem in iterable:
#         if elem != str_:
#             lst_.append(elem)
#         str_ = elem
#     return lst_
#
# print(unique_in_order('AAAABBBCCDAABBB'))
# print(unique_in_order('ABBCcAD'))
# print(unique_in_order([1,2,2,3,3]))


# def validate_pin(pin):
#     if len(pin) == 4 or len(pin) == 6:
#         try:
#             if int(pin) > 0:
#                 return True
#         except:
#             return False
#     return False


# def validate_pin(pin):
#     nums = [str(i) for i in range(10)]
#     pin = list(pin)
#     if (len(pin) != 4) and (len(pin) != 6):
#         return False
#     else:
#         for elem in pin:
#             if elem not in nums:
#                 return False
#     return True
#
#
# print(validate_pin('09876'))
# print(validate_pin('123'))
# print(validate_pin('1234'))
# print(validate_pin('12345'))
# print(validate_pin('a123'))
# print(validate_pin('+12123'))


# from itertools import combinations
#
# def choose_best_sum(t, k, ls):
#     result = 0
#     for combination in combinations(ls, k):
#         sum_ = sum(combination)
#         if sum_ <= t and sum_ > result:
#             result = sum_
#
#     if result == 0:
#         return
#     return result
#
#
# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# print(choose_best_sum(230, 4, xs))


# def zeros(n):
#     count = 0
#     while (n >= 5):
#         n //= 5
#         count += n
#     return count
#
#
# print(zeros(6))
# print(zeros(30))
# print(zeros(10))
# print(zeros(1000))
# print(zeros(10000))


# def domain_name(url):
#     print(url)
#     if url[0] == 'w':
#         b = url.split('.')
#         return b[1]
#     elif url[:5] == 'http:':
#         url = url[7:]
#         b = url.split('.')
#         return b[0] if b[0] != 'www' else b[1]
#     elif url[:6] == 'https:':
#         url = url[8:]
#         b = url.split('.')
#         return b[0]
#     else:
#         b = url.split('.')
#         return b[0]
#
#
# print(domain_name("www.xakep.ru"))
# print(domain_name("https://123.net"))
# print(domain_name("http://www.codewars.com/kata/"))
# print(domain_name("https://en.wikipedia.org"))


# def wave(people: str):
#     lst_ = []
#     for index_, elem in enumerate(people):
#         if elem.isalpha():
#             lst_.append(people[:index_] + people[index_].upper() + people[index_ + 1:])
#     return lst_


# def min_sum(arr: list) -> int:
#     arr.sort()
#     count = 0
#     for elem in range(len(arr) // 2):
#         count += arr.pop(0) * arr.pop(-1)
#     return count
#
#
# print(min_sum([3, 4, 5, 2]))


# def solution(s: str) -> str:
#     result = ''
#     for elem in s:
#         if elem == elem.upper():
#             result += ' '
#         result += elem
#     return result


# def count(string):
#     dict_ac = {}
#     for i in list(string):
#         dict_ac[i] = dict_ac.get(i, 0) + 1
#     return dict_ac
# from collections import Counter
#
# def count(string):
#     return Counter(string) Подсчет символов во всей строке


# def human_years_cat_years_dog_years(human_years):
#     cats_1, dogs_1 = 15, 15
#     cats_2, dogs_2 = 9, 9
#     cats_other, dogs_other = 4, 5
#     if human_years == 1:
#         return [human_years, cats_1, dogs_1]
#     elif human_years == 2:
#         return [human_years, cats_1 + cats_2, dogs_1 + dogs_2]
#     else:
#         cats_all, dogs_all = 24, 24
#         for i in range(human_years - 2):
#             cats_all += cats_other
#             dogs_all += dogs_other
#     return [human_years, cats_all, dogs_all]
#
# print(human_years_cat_years_dog_years(10)) # Ну кот и собака, ну года, ну да


# def parse(data):
#     data = list(data)
#     count = 0
#     lst_ = []
#     for elem in data:
#         if elem == 'o':
#             lst_.append(count)
#         elif elem == 'i':
#             count += 1
#         elif elem == 'd':
#             count -= 1
#         elif elem == 's':
#             count **= 2
#     return lst_
#
#
# print(parse("ooo"))
# print(parse("iiisdoso"))


# def count_sheep(n):
#     return ''.join([str(elem) + ' sheep...' for elem in range(1, n + 1)])


# def enough(cap, on, wait):
#     if on + wait <= cap:
#         return 0
#     return abs(cap - (on + wait))


# print(enough(10, 5, 5))
# print(enough(100, 60, 50))
# print(enough(20, 5, 5))


# def solution(string, ending):
#     ending_len = len(ending)
#     string_len = len(string)
#     string = string[string_len - ending_len:]
#     return string == ending
#
# def solution(string, ending):
#     return string.endswith(ending)
#
# print(solution('abc', 'bc')) # returns true
# print(solution('abc', 'd')) # returns false


# def remove_exclamation_marks(s):
#     lst_ = []
#     for elem in s:
#         if elem != '!':
#             lst_.append(elem)
#     return ''.join(lst_)
#
# print(remove_exclamation_marks("Hello World!"))


# def powers_of_two(n):
#     return [2 ** i for i in range(n + 1)]
#
# print(powers_of_two(0))


# def two_sum(numbers, target):
#     dict_ = {}
#     for i in range(len(numbers)):
#         if numbers[i] in dict_:
#             return [dict_[numbers[i]], i]
#         dict_[target - numbers[i]] = i
#
#
#
#
# print(sorted(two_sum([1,2,3], 4)))


# def accum(string: str) -> str:
#     string = list(string.lower())
#     lst_ = []
#     count = 1
#     for elem in string:
#         end = ''
#         for _ in range(count):
#             end += elem
#         count += 1
#         end = end.capitalize()
#         lst_.append(end)
#     return '-'.join(lst_)

# print(accum("ZpglnRxqenU") == "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")


# def beeramid(bonus, price):
#     canCount = bonus // price
#     level = 0
#     while ((level + 1) ** 2 <= canCount):
#         level += 1
#         canCount -= level ** 2
#     return level


# def solution(s):
#     string = ''
#     for elem in s:
#         if elem.isupper():
#             string += ' '
#         string += elem
#     return string
#
#
# print(solution('helloWord!'))


# def gimme(inputArray):
#     # Implement this function
#     return inputArray.index(sorted(inputArray)[1])


# def sort_array(source_array):
#     sorted_array = sorted([i for i in source_array if i % 2 != 0])
#     for index, item in enumerate(source_array):
#         if item % 2 == 0:
#             sorted_array.insert(index, item)
#     return sorted_array
#
# print(sort_array([5, 3, 2, 8, 1, 4]))


# def remove_url_anchor(url):
#     string_all = ''
#     for elem in url:
#         if elem == '#':
#             break
#         string_all += elem
#     return string_all


# print(remove_url_anchor('www.codewars.com#about'))


# def title_case(string: str, minor_words='') -> str:
#     string, minor_words = string.lower(), minor_words.lower()
#     string = string.split(' ')
#     lst_ = []
#     bad_word = minor_words.split(' ')
#     for index, elem in enumerate(string):
#         if elem not in bad_word or index == 0:
#             lst_.append(elem.capitalize())
#         else:
#             lst_.append(elem)
#     return ' '.join(lst_)
#     # return ' '.join([elem.capitalize() if elem not in bad_word or index == 0 else elem for index, elem in enumerate(string)])
#
# print(title_case(''))
# print(title_case('a clash of KINGS', 'a an the of'))
# print(title_case('THE WIND IN THE WILLOWS', 'The In'))


# def capitals(string: str) -> list:
#     # lst_ = []
#     # for index, elem in enumerate(string):
#     #     if elem.isupper():
#     #         lst_.append(index)
#     # return lst_
#     return [index for index, elem in enumerate(string) if elem.isupper()]
#
# print(capitals('CodEWaRs'))


# def findSum(n):
#     result = 0
#     for i in range(n + 1):
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
#     return result
#
# print(findSum(5))
# print(findSum(10))


# def find_difference(a, b):
#     count_a, count_b = a[0] * a[1] * a[2], b[0] * b[1] * b[2]
#     return abs(count_a - count_b)
#
# print(find_difference([9, 7, 2], [5, 2, 2]))


# import numpy as np
# from pandas import DataFrame

# def create_matrix(length, width):
#     a = np.random.randint(10, size=(length, width))
#     b = np.random.randint(10, size=(length, width))
#     return a, b
#
# def matrix_addition(length, width):
#     a, b = create_matrix(length, width)
#     lst_result = []
#     for i in range(len(a)):
#         lst_1 = []
#         for j in range(len(a[i])):
#             lst_1.append(a[i][j] + b[i][j])
#         lst_result.append(lst_1)
#     return DataFrame(lst_result)
#
#
#
# for x in range(20 + 1):
#     print(matrix_addition(x, x), '\n')


# def decode_morse(morse_code):
#     MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
#                   '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
#                   '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
#                   '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
#                   '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
#                   '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'",
#                   '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
#                   '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
#                   '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}
#     morse_code = morse_code.strip()
#     morse_code = morse_code.replace('  ', ' ')
#     morse_code = morse_code.split(' ')
#     lst_ = []
#     for elem in morse_code:
#         if elem == '':
#             lst_.append(' ')
#             continue
#         lst_.append(MORSE_CODE[elem])
#     return ''.join(lst_)
#
#
# print(decode_morse('.... . -.--   .--- ..- -.. .'))
# print(decode_morse('...---...'))
# print(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-'))
# print(decode_morse('...   ---   ...'))


# def digital_root(n):
#     print(n)
#     if n >= 10:
#         while n >= 10:
#             count = 0
#             for elem in str(n):
#                 count += int(elem)
#             n = count
#         return count
#     return n
#     # return n % 9 or n and 9
#
# print(digital_root(16))
# print(digital_root(942))
# print(digital_root(132189))
# print(digital_root(493193))


# def get_grade(s1, s2, s3):
#     average_s = (s1 + s2 + s3) / 3
#     if 90 <= average_s <= 100:
#         return 'A'
#     elif 80 <= average_s < 90:
#         return 'B'
#     elif 70 <= average_s < 80:
#         return 'C'
#     elif 60 <= average_s < 70:
#         return 'D'
#     return 'F'


# def remove_smallest(numbers):
#     arr = numbers[:]
#     return numbers and arr.pop(arr.index(min(arr))) and arr

# def nbMonths(oldCarPrice, newCarPrice, saving, loss):
#     months = 0
#     budget = oldCarPrice
#
#     while budget < newCarPrice:
#         months += 1
#         if months % 2 == 0:
#             loss += 0.5
#
#         oldCarPrice *= (100 - loss) / 100
#         newCarPrice *= (100 - loss) / 100
#         budget = saving * months + oldCarPrice
#
#     return [months, round(budget - newCarPrice)]
#
#
# print(nbMonths(2000, 8000, 1000, 1.5))

# def transpose(matrix):
#     # № 1
#     result = []
#     for i in range(len(matrix[0])):
#         lst_ = []
#         for j in range(len(matrix)):
#             lst_.append(matrix[j][i])
#         result.append(lst_)
#     return result
#     # № 2
#     return list(map(list, zip(*matrix)))
#
#
# print(transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]))
# print(transpose([[1,2,3]]))
# print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(transpose([[1]]))
# print(transpose([[1, 2, 3], [4, 5, 6]]))


# a = ['hoqq', 'bbllkw', 'oox', 'ejjuyyy', 'plmiis', 'xxxzgpsssa', 'xxwwkktt', 'znnnnfqknaz', 'qqquuhii', 'dvvvwz']
# b = ['cccooommaaqqoxii', 'gggqaffhhh', 'tttoowwwmmww']
# lst_ = []
# for elem_1 in a:
#     for elem_2 in b:
#         lst_.append(abs(len(elem_1) - len(elem_2)))
# print(max(lst_))


# import math


# def factorial(n):
#     if n < 0 or n > 12:
#         raise ValueError()
#     return math.factorial(n)


# def solution(string, markers):
#     parts = string.split('\n')
#
#     for s in markers:
#         parts = [v.split(s)[0].rstrip() for v in parts]
#     return '\n'.join(parts)
#
# print(solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))



