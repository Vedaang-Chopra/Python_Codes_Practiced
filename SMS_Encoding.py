# def consonant_check(char_arr):
#     consonants = "b c d f g h j k l m n p q r s t v w x y z".split()
#     print(consonants)
#     flag=1
#     for i in char_arr:
#         if i in consonants:
#
#
#
# def vowel_check(char_arr):
#     vowels='a e i o u'.split()
#     print(vowels)
#     flag=1
#     for i in char_arr:
#         if i in vowels:
#             flag=1
#         else:
#             flag=0
#             break;
#     return flag
#
#
#
# def sms_encoding(data):
#     char_by_char=[[]]
#     word_by_word=data.split()
#     for i in word_by_word:
#         word=i
#         for j in range(0,len(word)):
#             char_by_char[i].append(j)
#
#
#
# def main():
#     input_string=input()
#     encoded_string=sms_encoding(input_string)
#     print("Encoded String is:"+encoded_string)
