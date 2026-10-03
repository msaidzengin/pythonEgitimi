# BTK Akademi Python Eğitim İçeriği

Türkçe Python ders notları, örnek kodlar ve alıştırmalar.

## Nasıl başlanır

1. Python'u kurun. [Python Kurulumu](python101/10-Slides/01-Python%20Kurulumu.pdf) slaydı Anaconda ile Python 3.7 kullanır. İndirme adresi slaytta yazılıdır: https://www.anaconda.com/distribution/
2. Depoyu indirin. Git varsa:

```bash
git clone https://github.com/msaidzengin/pythonEgitimi.git
cd pythonEgitimi
```

Git yoksa bu sayfadaki Code menüsünden ZIP indirip açın ve o klasöre geçin.

3. İlk örneği çalıştırın. Anaconda Prompt veya terminalde:

```bash
python python101/01-Basics/01-Hello.py
```

Komut bulunamazsa `python` yerine `python3` yazın. Ekranda `Merhaba Dünya!` görünür.

4. Türkçe derse `python101/01-Basics/07-Ders Notları.txt` ile devam edin. Aynı klasördeki `.py` dosyalarını numara sırasıyla çalıştırın. Adında boşluk olan dosyada yolu tırnak içine alın:

```bash
python "python101/01-Basics/03-Math operators.py"
```

Sonraki klasörler `02-Loops`, `03-IfElse`, `04-Functions`, `05-Algorithms`, `06-OOP`, `07-Sockets` ve `08-Random` şeklindedir. Ödevler `python101/09-Homeworks`, slaytlar `python101/10-Slides` içindedir.

5. Notebook dersleri kökteki numaralı klasörlerdedir. Anaconda Jupyter'i de kurar. Depo klasöründe şunu çalıştırın:

```bash
jupyter notebook
```

`jupyter` bulunamazsa:

```bash
python -m pip install notebook
python -m notebook
```

Açılan sayfada `01-Objects and Data Structures/01-Numbers.ipynb` dosyasını açın. Klasörler `16-Recommender Systems` klasörüne kadar numara sırasıyla ilerler. İleri bir notebook eksik paket hatası verirse o paketi kurun. Bu dersteki paket adları: Pillow, PyPDF2, beautifulsoup4, requests, send2trash, numpy, matplotlib, pandas, scikit-learn ve nltk.

## 1. Seviye
#### 1. Hafta
- Programlama nedir?
- Algoritma nedir?
- Algoritma neden önemlidir?
- Programlamanın temel mantığı ve temel yapısı
- Makine kodu nedir?
- Programlama dilleri nelerdir?
- Programlar ile neler yapılabilir?
- Compiler, interpreter nedir?
- Syntax, semantics nedir?
- Nesne tabanlı programlama nedir?
- Python kurulumu
- Python'ı tanıyoruz
- Python ile Merhaba Dünya kodu
- Indentation
- Variables - Değişkenler
- Python ile matematiksel işlemler
- String nedir?
- Integer nedir?
- Input ve output
- If-else yapısı
#### 2. Hafta
- Nesne türleri - String, Integer, Boolean...
- Özel karakterler
- Karşılaştırma Operatörleri
- If-Elif-Else örnek alıştırmalar
- For ve while döngüsü
- String manipülasyonları
#### 3. Hafta
- Diziler
- Fonksiyonlar
- Veri türleri - Tuples, Dictionary, Lists...
- Hazır metodlar - math, random, numpy, time, os, sys
- Kütüphane kullanımı
- Modül Oluşturma ve Kulanma
- Random password generation application
- Number guessing game with random library
#### 4. Hafta
- Messaging application with sockets
- Recursive Functions - Özyinemeli Fonksiyonlar
- Linear Search - Lineer Arama Algoritması
- Binary Search - İkili Arama Algoritması
- Time Complexity - Algoritmaların Zaman Karşılaştırmaları
#### 5. Hafta
- Tkinter ve PAGE ile gui tasarlama
- Dosya okuma ve yazma 
- Excel okuma ve yazma
- Pandas, numpy, nltk kütüphaneleri kullanımı
- Executable oluşturma


## 2. Seviye
- Running Time
- Time Complexity
- Space Complexity
- Recursion
##### Veri Yapıları
- Arrays
- Stacks
- Queues
- Linked Lists
- Hash Tables
- Trees
- Graphs

##### Algorithms
- Linear Search
- Binary Search
- Selection Sort
- Insertion Sort
- Bubble Sort
- Merge Sort
- Heap Sort
- Other sorting algorithms
- Binary Search Tree
- BFS and DFS
- AVL
##### Applications
- Crawling
- Data Mining
- Data Processing
- Mongo DB
- Django
- GitHub

## 3. Seviye
- Natural Language Process (NLP)
- Recommender Systems (RS)
- Image Processing
- Machine Learning
- AI - ML - DL Applications



## Contact

msaidzengin@gmail.com


## Links

- https://bit.ly/btk-python
- https://bit.ly/python-uni
- https://bit.ly/python-sinav
- https://bit.ly/sinav-python
- https://bit.ly/btk-uni-python
- https://bit.ly/btk-python-uni
- https://bit.ly/btk-python-sinav
