# s={"Name":"HKOU","age":25,"sex":"male"}
# print(s)
# s["adress"]="KKKKs"
# s["Name"]="PPPP"
# if "sex" in s:
#     del s["sex"]
	    
# print(s)
# '''
# {'Name': 'HKOU', 'age': 25, 'sex': 'male'}
# {'Name': 'PPPP', 'age': 25, 'adress': 'KKKKs'}
# '''

# sentance=input("Give me a sentence")
# words=sentance.split()
# word_count={}
# for word in words:
#     word=word.lower()
#     if word in word_count:
#         word_count[word]+=1
#     else:
#         word_count[word]=1
# print(word_count)
# '''
# Give me a sentence ppp hhhh jib hhhh ppp jknj ppp
# {'ppp': 3, 'hhhh': 2, 'jib': 1, 'jknj': 1}
# PS D:\Project\Python> 
# '''

# stud={}
# h=0
# ss=0
# while True:
#     print("\nIf you want to store marks press 1")
#     print("If want to exit press 2")
#     k=float(input("Press here :"))
#     if k == 2:
#         break
#     if k == 1:
#         n=(input("Give the name : "))
#         m=float(input("give the marks : "))
#         stud[n]=m
#         h+=1
#         ss=ss+m
#     else :
#         print("invalid choice")
    
#     print(stud)
#     print(f"Average student marks {ss/h}")
# '''
# If you want to store marks press 1
# If want to exit press 2
# Press here :1
# Give the name : knjn
# give the marks : 34
# {'knjn': 34.0}
# Average student marks 34.0

# If you want to store marks press 1
# If want to exit press 2
# Press here :2
# '''

# import re
# text = "contact me at 123-456-6789"
# digits = re.findall(r"\d+",text)
# print(digits)
# '''
# ['123', '456', '6789']
# '''

# import re
# text = "contact me at 123-456-6789"
# digits = re.findall(r"\d+",text)
# # print(digits)
# updated_text=re.sub(r"\d","X",text)
# print(updated_text)
# '''
# contact me at XXX-XXX-XXXX
# '''


# import re
# def clean_text(text):
#     # Remove punctuation
#     text = re.sub(r"[^\w\s]", "", text)
#     # Remove extra spaces
#     text = " ".join(text.split())
#     # Convert to lowercase
#     return text.lower()
# input_text = "   Hello, World.!!! Welcome to Python, Programming....   "
# cleaned_text = clean_text(input_text)
# print(input_text)
# print(cleaned_text)
# '''
#    Hello, World.!!! Welcome to Python, Programming....
# hello world welcome to python programming
# '''

# def is_palindrome(text):
#     text = "".join(char.lower() for char in text if char.isalnum())
#     return text == text[::-1]
# k=input("Enter a string : ")
# if is_palindrome(k):
#     print(f"'{k}' is a palindrome")
# else:
#     print(f"'{k}' is not a palindrome")

# '''
# Enter a string : mkmk jdk
# 'mkmk jdk' is not a palindrome

# Enter a string : kkk dgf fgd kkk
# 'kkk dgf fgd kkk' is a palindrome
# '''

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
print(count_vowels("Hello World"))  
'''
3
'''
import re
def mask_emails(text):
    return re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[EMAIL]", text)
text = "Contact me at test123@gmail.com or admin@company.org"
print(mask_emails(text))
'''
Contact me at [EMAIL] or [EMAIL]
'''
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])
print(reverse_words("Hello world this is Python"))
'''
Python is this world Hello
'''