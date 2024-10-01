import re
import os
import sys


text = """
# **My Task Title** [x]

> **Awareness Training** Merupakan program pelatihan yang dirancang oleh Akasata Cybertech untuk meningkatkan kesadaran dan pemahaman pengguna mengenai keamanan siber. Program ini bertujuan untuk membekali individu dengan pengetahuan yang diperlukan untuk mengenali ancaman potensial, melindungi data pribadi, dan berperan aktif dalam menjaga keamanan sistem di lingkungan digital mereka. Dengan pendekatan yang interaktif dan relevan, pelatihan ini memastikan bahwa setiap pengguna lebih peka terhadap risiko keamanan dan mampu mengambil langkah proaktif untuk melindungi informasi penting


"""

def get_regex_matches(matches):
    class iContent:
        def __init__(self, match):
            self.prefix = match.group('prefix')
            self.body = match.group('body')
            self.postfix = match.group('postfix')
            self.content = match.group('content')
            # if self.prefix is None or self.body is None or self.postfix is None:
                
    for match in matches:
        item = iContent(match=match)
        # content: str = item.prefix + item.body + item.postfix
        content2: str = item.content
        return "Oke"
        if content2 == None:
            return "No Content Available"
        else:
            return "oke"
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
    #     content: iContent = match.group('prefix') + match.group('body') + match.group('postfix')
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
    regex_pattern = re.compile(r'^(?P<prefix>\#\s\*\*)(?P<body>.+?)(?P<postfix>\*\*\s\[x\])', re.MULTILINE)
    pattern = regex_pattern
    matches = pattern.finditer(text)
    return get_regex_matches(matches=matches)

def get_desc():
    # Required regex group name: 
    # ?P<prefix>
    # ?P<body>
    # ?P<postfix>
    regex_pattern = re.compile(r'^(?P<prefix>>\s?\S)(?P<body>.*)(?P<postfix>\n)', re.MULTILINE)
    pattern = regex_pattern
    matches = pattern.finditer(text)
    return get_regex_matches(matches=matches)

def get_prefix1():
    # Required regex group name: 
    # ?P<prefix>
    # ?P<body>
    # ?P<postfix>
    regex_pattern = re.compile(r'^(?P<content>(Berikut).(Penjelasan).(Detail).(Mengenai).(Produk).*)', re.MULTILINE)
    pattern = regex_pattern
    
    # do regex pattern matcher
    match = pattern.match(text)

    if match:
        # do looping for fetching the contents 
        matches = pattern.finditer(text)
        for match in matches:
            print(match)
        print(matches)
        result = get_regex_matches(matches=matches)
        sys.exit(result)
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

# print(get_desc())
print(get_prefix1())