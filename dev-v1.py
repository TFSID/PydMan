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
            if self.prefix is None or self.body is None or self.postfix is None:
                self.content = match.group('content')
    
    for match in matches:
        content: iContent = match.group('prefix') + match.group('body') + match.group('postfix')
        if (content == None):
            content: str = match.group('content')
        else:    
            return content

def get_title():
    # gex group name: 
    # ?P<prefix>
    # ?P<body>
    # ?P<postfix>
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
    regex_pattern = re.compile(r'{regex pattern}', re.MULTILINE)
    pattern = regex_pattern
    matches = pattern.finditer(text)
    return get_regex_matches(matches=matches)

def get_prefix2():
    # Required regex group name: 
    # ?P<prefix>
    # ?P<body>
    # ?P<postfix>
    regex_pattern = re.compile(r'{regex pattern}', re.MULTILINE)
    pattern = regex_pattern
    matches = pattern.finditer(text)
    return get_regex_matches(matches=matches)

print(get_desc())