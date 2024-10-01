import os
import re
import sys

from typing import List, Dict

from save_to_file import save_to_file as savefile



documentation = """
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
"""

LinkReadme: str = '[Application Control](Product%20List/Application%20Control/README.md)'

title: str = '# **Awarness Training** [x]'
body: str = '> LongText()'
prefix1: str = "Berikut Penjelasan Detail Mengenai Produk *"
prefix2: str = '> [!NOTE] \n > OR > LongText()'

Produk: List[Dict] = [{"title":title, "body":body, "prefix1":prefix1, "prefix2":prefix2}]


def split_text(text):
    # Use regex to capture all repeating sections
    pattern = re.compile(r"""
        ^\#\s\*\*(?P<title>.+?)\*\*\s\[x\]                       # Capture the title
        \n\n> \*\*(?P<body>.+?)\.\n                              # Capture the body
        \n<!--\s(?P<comment>.+?)\s-->\n                          # Capture the optional comment
        \nBerikut\sPenjelasan\sDetail\sMengenai\sProduk\s\*\*(?P<prefix1>.+?)\*\*\n # Capture Prefix1
        \n(?P<prefix2>Akasata\sCybertech.+?)\.\n                 # Capture Prefix2
        \n> \[\!NOTE\]\n> (?P<note>.+?)\n                        # Capture the note section
        \nBerikut\sBeberapa\sRancangan.+?                        # Capture additional info (ignored here for now)
    """, re.VERBOSE | re.DOTALL | re.MULTILINE)

    matches = pattern.finditer(text)
    
    # Store results in a list
    result = []

    for match in matches:
        result.append({
            'title': match.group('title'),
            'body': match.group('body'),
            'comment': match.group('comment'),
            'prefix1': match.group('prefix1'),
            'prefix2': match.group('prefix2'),
            'note': match.group('note')
        })

    print(result)

# Call the function and store the result
# split_data = split_text(documentation)


split_text(documentation)
# print(documentation)
# for idx, data in enumerate(split_data):
#     print(f"Paragraph {idx + 1}:")
#     print(f"Title: {data['title']}")
#     print(f"Body: {data['body']}")
#     print(f"Comment: {data['comment']}")
#     print(f"Prefix1: {data['prefix1']}")
#     print(f"Prefix2: {data['prefix2']}")
#     print(f"Note: {data['note']}")
#     print("-" * 40)