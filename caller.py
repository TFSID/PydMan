import json
import re

from dev import iDocStructure, get_all_link, get_prefix1, get_desc, get_title

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



# **Patch Management** [X]

> Produk **Patch Management** adalah layanan yang ditawarkan oleh Akasata Cybertech untuk memastikan keamanan, stabilitas, dan kinerja optimal perangkat lunak.Layanan ini mencakup pengelolaan pembaruan perangkat lunak secara berkala melalui penambalan (patching) yang dirancang untuk mengatasi kerentanan keamanan, bug, serta peningkatan fungsionalitas.

Berikut Penjelasan Detail Mengenai Produk **[Patch Management](Product%20List/Patch%20Management/README.md)**

<!-- Ide Software/Tools -->
> [!NOTE]
Akasata Cybertech juga menawarkan beberapa solusi software dan tools untuk Application Control.
Berikut Beberapa Rancangan Ide Lainnya Jika Produk Tersebut Ingin Disediakan Dalam Bentuk Software/Tools atau dapat disebut juga sebagai [Patch Management Suite](Product%20List/Patch%20Management/Patch%20Management.md)

Berikut Beberapa Rancangan Untuk Menuliskan [Panduan Terkait Produk Patch Management](Product%20List/Patch%20Management/PointPenting.md)



# **Tunable Machine Learning** [x]

> **Produk Tunable Machine Learning** merupakan layanan yang disediakan oleh Akasata Cybertech sebagai solusi untuk mengoptimalkan proses analisis data dan deteksi ancaman siber melalui penerapan teknik pembelajaran mesin yang dapat disesuaikan. Dengan memanfaatkan algoritma yang dapat diatur, layanan ini memungkinkan organisasi untuk menyesuaikan model pembelajaran mesin sesuai dengan kebutuhan dan karakteristik spesifik lingkungan operasional mereka. Hal ini tidak hanya meningkatkan akurasi dalam mendeteksi anomali dan serangan, tetapi juga memungkinkan respons yang lebih cepat dan tepat terhadap ancaman yang muncul. Produk ini dirancang untuk memberikan fleksibilitas dan efisiensi dalam mengelola data keamanan, sehingga organisasi dapat mengambil keputusan yang lebih baik dan meningkatkan postur keamanan siber mereka secara keseluruhan.

Berikut Penjelasan Detail Mengenai Produk **[Tunable Machine Learning](Product%20List/Tunable%20Machine%20Learning/README.md)**

> [!NOTE]
Akasata Cybertech juga menawarkan beberapa solusi software dan tools untuk Tunable Machine Learning.
Berikut Beberapa Rancangan Ide Lainnya Jika Produk Tersebut Ingin Disediakan Dalam Bentuk Software/Tools atau dapat disebut juga sebagai [Tunable Machine Learning](Product%20List/Tunable%20Machine%20Learning/Tunable%20Machine%20Learning.md)

Berikut Beberapa Rancangan Untuk Menuliskan [Panduan Terkait Produk Patch Management](Product%20List/Tunable%20Machine%20Learning/PointPenting.md)


# **Security For Mobile** [x]

<!-- **Produk Security For Mobile** Merupakan ... -->

> Produk **Security for Mobile** merupakan layanan yang disediakan oleh Akasata Cybertech untuk memantau dan mengamankan mobile endpoint seperti handphone, tablet, dan laptop. Dengan solusi ini, organisasi dapat melindungi perangkat seluler mereka dari ancaman siber, mencegah akses tidak sah, serta memastikan perlindungan data yang lebih baik dalam lingkungan bisnis mobile. Layanan ini juga mencakup pengelolaan perangkat dan aplikasi secara efektif, baik untuk penggunaan internal maupun cloud-based services.

<!-- Layanan Yang disediakan oleh Akasata Cybertech untuk memantau dan mengamankan Mobile Endpoint Seperti Handphone, Tablet, Laptop -->


Berikut Penjelasan Detail Mengenai Produk **[Security For Mobile](Product%20List/Security%20For%20Mobile/README.md)**

> [!NOTE]
Akasata Cybertech juga menawarkan beberapa solusi software dan tools untuk Security For Mobile.
Berikut Beberapa Rancangan Ide Lainnya Jika Produk Tersebut Ingin Disediakan Dalam Bentuk Software/Tools atau dapat disebut juga sebagai [Security For Mobile](Product%20List/Security%20For%20Mobile/Security%20For%20Mobile.md)

Berikut Beberapa Rancangan Untuk Menuliskan [Panduan Terkait Produk Security For Mobile](Product%20List/Security%20For%20Mobile/PointPenting.md)

# **Security For Containers** [x]

> Produk **Security for Containers** adalah layanan yang disediakan oleh Akasata Cybertech untuk memantau dan mengamankan lingkungan container seperti Kubernetes, Docker, dan platform container lainnya. Solusi ini membantu organisasi dalam mengelola keamanan container dari tahap pembangunan hingga deployment, memastikan perlindungan terhadap ancaman siber, serta menjaga integritas dan ketersediaan aplikasi yang berjalan di atas platform container. Layanan ini juga mencakup pemantauan terus-menerus, deteksi ancaman, dan respons terhadap insiden keamanan di lingkungan container.

<!-- **Produk Security For Containers** Merupakan ... -->

<!-- Layanan Yang disediakan oleh Akasata Cybertech untuk memantau dan mengamankan Containers Seperti Kubernetes, Docker, dsb -->


Berikut Penjelasan Detail Mengenai Produk **[Security For Containers](Product%20List/Security%20For%20Containers/README.md)**

> [!NOTE]
Akasata Cybertech juga menawarkan beberapa solusi software dan tools untuk Security For Containers.
Berikut Beberapa Rancangan Ide Lainnya Jika Produk Tersebut Ingin Disediakan Dalam Bentuk Software/Tools atau dapat disebut juga sebagai [Security For Containers](Product%20List/Security%20For%20Containers/Security%20For%20Containers.md)

Berikut Beberapa Rancangan Untuk Menuliskan [Panduan Terkait Produk Security For Containers](Product%20List/Security%20For%20Containers/PointPenting.md)

# **Incident Advisor** [ x ]

> Produk **Incident Advisor** adalah layanan yang disediakan oleh Akasata Cybertech untuk membantu tim keamanan (Security Team) dalam merespons dan menangani insiden yang terjadi di lingkungan IT, khususnya yang terkait dengan keamanan siber. Layanan ini dirancang untuk memberikan panduan cepat dan efisien dalam mengelola insiden keamanan, termasuk investigasi, mitigasi, dan pemulihan dari ancaman siber. Incident Advisor memastikan bahwa setiap insiden ditangani secara tepat untuk meminimalkan dampak terhadap operasi bisnis.

<!-- **Produk Incident Advisor** Merupakan ...
Produk Incident Advisor Merupakan Layanan Yang disediakan oleh Akasata Cybertech untuk Membantu Tim Security pada perusahaan/Organisasi jika terjadinya incident pada suatu lingkungan IT dan berkaitan dengan Cyber Security -->

Berikut Penjelasan Detail Mengenai Produk **[Incident Advisor](Product%20List/Incident%20Advisor/README.md)**

> [!NOTE]
Akasata Cybertech juga menawarkan beberapa solusi software dan tools untuk Incident Advisor.
Berikut Beberapa Rancangan Ide Lainnya Jika Produk Tersebut Ingin Disediakan Dalam Bentuk Software/Tools atau dapat disebut juga sebagai [Incident Advisor](Product%20List/Incident%20Advisor/Incident%20Advisor.md)

Berikut Beberapa Rancangan Untuk Menuliskan [Panduan Terkait Produk Incident Advisor](Product%20List/Incident%20Advisor/PointPenting.md)


"""

regex_readme_links = re.compile(r'(?P<content>(?P<LinkName>\[.*\])(?P<Link>\(.*\)))', re.MULTILINE)


try:
    print("\nGetting Data From Source...\n")
    
    doc_structure = iDocStructure()
    doc_structure.title = get_title()
    doc_structure.description = get_desc()
    doc_structure.prefix1 = get_prefix1()
    doc_structure.links = get_all_link(pattern=regex_readme_links, source=text)
    # doc_structure.link1 = get_link1()
    # doc_structure.link2 = get_link2()

    # title = [i for i in doc_structure.title]
    title = doc_structure.title
    description = doc_structure.description
    prefix1 = doc_structure.prefix1
    links = doc_structure.links
    # link1 = doc_structure.link1
    # link2 = doc_structure.link2

    # slices = []
    result = {
         "title": title,
         "description": description,
         "prefix1": prefix1,
         "links": links
    }
    # slices.append(result)

    f_name = "file.json"
    print('Writting File Into ',f_name)
    with open(f_name,'w') as file:
        try:
            file.write(json.dumps(result,indent=4))
            print('file writted to ',f_name)
        except Exception as err:
            print(err)
    # print(slices)
    # result_json = print([slc for slc in slices])
    # print(result_json)
    # print(title[0])
    # print(title2)
    # print(title[1])
    # print(title[2])
    # print(description)
except Exception as err:
    print(err)