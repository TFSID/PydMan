import re
import sys

links = [
        "[Awareness Training](Product%20List/Awarness%20Training/README.md)",
        "[Awareness Training Platform](Product%20List/Awarness%20Training/Awareness%20Training.md)",
        "[Panduan Terkait Produk Awareness Training](Product%20List/Awarness%20Training/PointPenting.md)",
        "[Implementasi UU PDP](Product%20List/Implementasi%20UU%20PDP/README.md)",
        "[PDP Suite](Product%20List/Implementasi%20UU%20PDP/Implementasi%20UU%20PDP.md)",
        "[Panduan Terkait Produk Implementasi UU PDP](Product%20List/Implementasi%20UU%20PDP/PointPenting.md)",
        "[Application Control](Product%20List/Application%20Control/README.md)",
        "[Application Control Suite](Product%20List/Application%20Control/Application%20Control.md)",
        "[Panduan Terkait Produk Application Control](Product%20List/Application%20Control/PointPenting.md)",
        "[Patch Management](Product%20List/Patch%20Management/README.md)",
        "[Patch Management Suite](Product%20List/Patch%20Management/Patch%20Management.md)",
        "[Panduan Terkait Produk Patch Management](Product%20List/Patch%20Management/PointPenting.md)",
        "[Tunable Machine Learning](Product%20List/Tunable%20Machine%20Learning/README.md)",
        "[Tunable Machine Learning](Product%20List/Tunable%20Machine%20Learning/Tunable%20Machine%20Learning.md)",
        "[Panduan Terkait Produk Patch Management](Product%20List/Tunable%20Machine%20Learning/PointPenting.md)",
        "[Security For Mobile](Product%20List/Security%20For%20Mobile/README.md)",
        "[Security For Mobile](Product%20List/Security%20For%20Mobile/Security%20For%20Mobile.md)",
        "[Panduan Terkait Produk Security For Mobile](Product%20List/Security%20For%20Mobile/PointPenting.md)",
        "[Security For Containers](Product%20List/Security%20For%20Containers/README.md)",
        "[Security For Containers](Product%20List/Security%20For%20Containers/Security%20For%20Containers.md)",
        "[Panduan Terkait Produk Security For Containers](Product%20List/Security%20For%20Containers/PointPenting.md)",
        "[Incident Advisor](Product%20List/Incident%20Advisor/README.md)",
        "[Incident Advisor](Product%20List/Incident%20Advisor/Incident%20Advisor.md)",
        "[Panduan Terkait Produk Incident Advisor](Product%20List/Incident%20Advisor/PointPenting.md)"
    ]

# print(links)

def extract_substring(input_string, rm_last_char):
    pattern = last_character_remove
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    return None

def links_change(source_list,last_word_change,last_character_remove):
    result_list = []
    for link in source_list:
        parts = re.split('/',link)
        # print(parts)
        extracted_text = extract_substring(parts[-1], rm_last_char=last_character_remove)
        if parts[-2] == extracted_text:
            # print(extracted_text)
            parts[-1] = last_word_change
        else:
            continue
        # print(parts[-1])
        # print(parts)

        # sys.exit(print(len(links)))
        # sys.exit(parts)
        array_val = 0
        if array_val < len(source_list):
            link_result = f'{parts[0]}/{parts[1]}/{parts[2]})'
            result_list.append(link_result)
            array_val += 1
    f_name = "changed_list.txt"
    with open(f_name, 'w') as fp:
        for f in result_list:
            out = f'"{f}",\n'
            fp.write(out)
    return(result_list)

last_word_change = "Referensi%20Produk.md"
last_character_remove = "(.*)\.md\)"

links_change(source_list=links,last_word_change=last_word_change, last_character_remove=last_character_remove)

