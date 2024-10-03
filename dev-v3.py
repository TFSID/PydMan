import re
import os
import sys


text = """
# **Awarness Training** [x]

> **Awareness Training** Merupakan program pelatihan yang dirancang oleh Akasata Cybertech untuk meningkatkan kesadaran dan pemahaman pengguna mengenai keamanan siber. Program ini bertujuan untuk membekali individu dengan pengetahuan yang diperlukan untuk mengenali ancaman potensial, melindungi data pribadi, dan berperan aktif dalam menjaga keamanan sistem di lingkungan digital mereka. Dengan pendekatan yang interaktif dan relevan, pelatihan ini memastikan bahwa setiap pengguna lebih peka terhadap risiko keamanan dan mampu mengambil langkah proaktif untuk melindungi informasi penting

<!-- Program Pelatihan yang disediakan oleh akasata cybertech untuk meningkatkan kepekaan dan kepedulian user terhadap keamanan siber -->

Berikut Penjelasan Detail Mengenai Produk **[Awareness Training](Product%20List/Awarness%20Training/README.md)**

Akasata Cybertech juga menawarkan beberapa solusi software dan tools untuk Awareness Training.

> [!NOTE]
> Berikut Beberapa Rancangan Ide Lainnya Jika Produk Tersebut Ingin Disediakan Dalam Bentuk Software/Tools atau dapat disebut juga sebagai [Awareness Training Platform](Product%20List/Awarness%20Training/Awareness%20Training.md)

Berikut Beberapa Rancangan Untuk Menuliskan [Panduan Terkait Produk Awareness Training](Product%20List/Awarness%20Training/PointPenting.md)



# **Implementasi UU PDP** [x]

<!-- **Produk Implementasi UU PDP** Merupakan suatu Packaging dari beberapa produk yang dimiliki oleh akasata untuk mengimplementasikan Peraturan peraturan yang tercantum dalam RUU PDP Yang membahas terkait Pengelolaan Data Pribadi -->

> Produk Implementasi UU PDP merupakan solusi terintegrasi dari Akasata Cybertech yang dirancang untuk membantu organisasi memenuhi persyaratan yang diatur dalam Undang-Undang Perlindungan Data Pribadi (UU PDP).Tujuannya adalah memastikan kepatuhan terhadap regulasi terkait keamanan dan privasi data, serta membantu organisasi mengelola risiko keamanan siber terkait perlindungan informasi pribadi.


Berikut Penjelasan Detail Mengenai Produk **[Implementasi UU PDP](Product%20List/Implementasi%20UU%20PDP/README.md)**

> [!NOTE]
> Akasata Cybertech juga menawarkan beberapa solusi software dan tools untuk Implementasi UU PDP.
> Berikut Beberapa Rancangan Ide Lainnya Jika Produk Tersebut Ingin Disediakan Dalam Bentuk Software/Tools atau dapat disebut juga sebagai [PDP Suite](Product%20List/Implementasi%20UU%20PDP/Implementasi%20UU%20PDP.md)

Berikut Beberapa Rancangan Untuk Menuliskan [Panduan Terkait Produk Implementasi UU PDP](Product%20List/Implementasi%20UU%20PDP/PointPenting.md)


# **Application Control** [x]   

<!-- Jasa/Service yang disediakan oleh akasata cybertech untuk memantau dan mengamankan aktifitas yang berhubungan dengan aplikasi/software lokal yang terdapat pada endpoint,Web-Based Application, dan Cloud-Based Application.
Dengan Application Control,dapat dilakukan beberapa metode  seperti Whitelisting, Blacklisting, dan Mengontrol sub-fungsi aplikasi dan mempertimbangkan konteks tambahan sebelum memungkinkan eksekusi (Granular Least Privilege) -->

> Produk **Application Control** adalah layanan yang disediakan oleh Akasata Cybertech untuk memantau dan mengamankan aktivitas aplikasi yang digunakan pada endpoint, aplikasi berbasis web, dan cloud. Layanan ini memungkinkan penerapan metode seperti Whitelisting, Blacklisting, serta pengontrolan sub-fungsi aplikasi melalui pendekatan Granular Least Privilege. Hal ini membantu memastikan bahwa hanya aplikasi dan fungsi yang sah dapat dieksekusi, dengan mempertimbangkan konteks tambahan untuk meningkatkan keamanan siber di lingkungan organisasi.



Berikut Penjelasan Detail Mengenai Produk **[Application Control](Product%20List/Application%20Control/README.md)**

<!-- Ide Software/Tools -->
> [!NOTE]
Akasata Cybertech juga menawarkan beberapa solusi software dan tools untuk Application Control.
Berikut Beberapa Rancangan Ide Lainnya Jika Produk Tersebut Ingin Disediakan Dalam Bentuk Software/Tools atau dapat disebut juga sebagai [Application Control Suite](Product%20List/Application%20Control/Application%20Control.md)

Berikut Beberapa Rancangan Untuk Menuliskan [Panduan Terkait Produk Application Control](Product%20List/Application%20Control/PointPenting.md)

"""
class iContent1:
        def __init__(self, match):
            self.prefix = match.group('prefix')
            self.body = match.group('body')
            self.postfix = match.group('postfix')
class iContent2:
        def __init__(self, match):
            self.content = match.group('content')

def get_regex_matches(matches):
        content_list = []
        for match in matches:
            try:
                content: str = iContent1(match=match).prefix + iContent1(match=match).body + iContent1(match=match).postfix
                content_list.append(content) 
            except Exception as err:
                try:
                    content: str = iContent2(match=match).content
                    content_list.append(content)
                except Exception as err:
                    sys.exit(err)
        for result in content_list:
             print(result)

def get_title():
    # gex group name: 
    # ?P<prefix>
    # ?P<body>
    # ?P<postfix>
    # OR use ?P<content> instead for all in one line groups
    regex_pattern = re.compile(r'^(?P<prefix>\#\s\*\*)(?P<body>.+?)(?P<postfix>\*\*\s\[x\]?.*?\n)', re.MULTILINE)
    pattern = regex_pattern
    
    # do regex pattern matcher

    matchCheck = pattern.search(text)
    if matchCheck:
        # do looping for fetching the contents 

        matches = pattern.finditer(text)
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
    print("\nGetting Data From Source...\n")
    print(get_title())
    print(get_desc())
    print(get_prefix1())
except Exception as err:
    print(err)