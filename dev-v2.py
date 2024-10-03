import re
import os
import sys


text = """
# **My Task Title** [x]

> **Awareness Training** Merupakan program pelatihan yang dirancang oleh Akasata Cybertech untuk meningkatkan kesadaran dan pemahaman pengguna mengenai keamanan siber. Program ini bertujuan untuk membekali individu dengan pengetahuan yang diperlukan untuk mengenali ancaman potensial, melindungi data pribadi, dan berperan aktif dalam menjaga keamanan sistem di lingkungan digital mereka. Dengan pendekatan yang interaktif dan relevan, pelatihan ini memastikan bahwa setiap pengguna lebih peka terhadap risiko keamanan dan mampu mengambil langkah proaktif untuk melindungi informasi penting

Berikut Penjelasan Detail Mengenain Produk **[Logpoint XDR](Product%20List/Logpoint%20XDR/README.md)**

"""
class iContent1:
        def __init__(self, match):
            self.prefix = match.group('prefix')
            self.body = match.group('body')
            self.postfix = match.group('postfix')
class iContent2:
        def __init__(self, match):
            self.content = match.group('content')
            # if not self.prefix:
                # self.add_content(match)
                # self.content = match.group('content')

        # def add_content(self, match):
            # setattr(self, 'content', match.group('content'))

            # self.content = match.group('content')
            # if Exception :
                # self.content = match.group('content')
            # try:
            #     self.prefix = match.group('prefix')
            #     self.body = match.group('body')
            #     self.postfix = match.group('postfix')
            # except Exception as err:
            #     print(err)
            #     print("kondisi matching group versi 1 tidak ditemukan")
            #     print("Melakukan Percobaan Menggunakan Matching Group Versi 2....")
            #     try:
            #         # if self.prefix is None or self.body is None or self.postfix is None:
            #         self.content = match.group('content')
            #     except Exception as err:
            #         print(err)
            #         print("ada kesalahan dengan matching group versi 2...")


def get_regex_matches(matches):
    
        for match in matches:
            # try:
                # content: str = iContent1(match=match).content
                # return content
            # except Exception as err:
                # sys.exit(err)
            
            try:
                content: str = iContent1(match=match).prefix + iContent1(match=match).body + iContent1(match=match).postfix
                return content
            except Exception as err:
                # print(err, "gaada grup content")
                try:
                    content: str = iContent2(match=match).content
                    return content
                except Exception as err:
                    sys.exit(err)
                

        # if content is None:
        #     sys.exit("if logic run")
        #     content: str = item.content
        #     if content is None:
        #         return "No Content / Regex Salah"
        #     else:
        #         return "No Content / Regex Salah"
        # else:
        #     return "sucess"
    
    # for match in matches:
    #     content: iContent1 = match.group('prefix') + match.group('body') + match.group('postfix')
    #     if (content == None):
    #         content: str = match.group('content')
    #     else:    
    #         return content

def get_title():
    # gex group name: 
    # ?P<prefix>
    # ?P<body>
    # ?P<postfix>
    # OR use ?P<content> instead for all in one line groups
    regex_pattern = re.compile(r'^(?P<prefix>\#\s\*\*)(?P<body>.+?)(?P<postfix>\*\*\s\[x\]\n)', re.MULTILINE)
    pattern = regex_pattern
    
    # do regex pattern matcher

    matchCheck = pattern.search(text)
    if matchCheck:
        # do looping for fetching the contents 
        matches = pattern.finditer(text)
        # for match in matches:
        #     print(match)
        # print(matches)
        result = get_regex_matches(matches=matches)
        return result
    else:
        sys.exit("No Pattern Matches / No Content Available")

def get_desc():
    # Required regex group name: 
    # ?P<prefix>
    # ?P<body>
    # ?P<postfix>
    regex_pattern = re.compile(r'^(?P<prefix>>\s?\S)(?P<body>.*)(?P<postfix>\n)', re.MULTILINE)
    pattern = regex_pattern
    
    # do regex pattern matcher

    matchCheck = pattern.search(text)
    if matchCheck:
        # do looping for fetching the contents 
        matches = pattern.finditer(text)
        # for match in matches:
        #     print(match)
        # print(matches)
        result = get_regex_matches(matches=matches)
        return result
    else:
        sys.exit("No Pattern Matches / No Content Available")

def get_prefix1():
    # Required regex group name: 
    # ?P<prefix>
    # ?P<body>
    # ?P<postfix>
    regex_pattern = re.compile(r'^(?P<content>(\w*).(\w*).(\w*).(\w*).(\w*).((\*\*).*(\*\*)))', re.MULTILINE)
    pattern = regex_pattern
    
    # do regex pattern matcher

    matchCheck = pattern.search(text)
    if matchCheck:
        # do looping for fetching the contents 
        matches = pattern.finditer(text)
        # for match in matches:
        #     print(match)
        # print(matches)
        result = get_regex_matches(matches=matches)
        return result
    else:
        sys.exit("No Pattern Matches / No Content Available")

def get_prefix2():
    # Required regex group name: 
    # ?P<prefix>
    # ?P<body>
    # ?P<postfix>
    regex_pattern = re.compile(r'{regex pattern}', re.MULTILINE)
    pattern = regex_pattern

    matches = pattern.finditer(text)
    return get_regex_matches(matches=matches)

try:
    print("get title")
    print(get_title())
except Exception as err:
    print(err)
try:
    print(get_desc())
except Exception as err:
    print(err)
try:
    print(get_prefix1())
except Exception as err:
    print(err)