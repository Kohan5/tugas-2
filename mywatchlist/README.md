# **Tugas 2 PBP (Aplikasi Katalog)**

## Link
### [Heroku](https://tugas2kohan.herokuapp.com/katalog/)
<br />

## Perbedaan antara JSON, XML, dan HTML
Untuk membedakan ketiganya, pertama kita dapat memisahkan antara HTML dan JSON & XML. HTML dibuat untuk menjadi bahasa dengan aturan yang tidak terlalu ketat sehingga pembuatan web dengan html dapat menjadi lebih mudah. Berbeda dengan HTML, XML dan JSON dibuat untuk memudahkan pengguna dalam membaca *code* dengan cara menjaga struktur informasi dengan mengorbankan aturan yang lebih ketat (seperti pendahulu HTML yaitu SGML).

Untuk perbedaan JSON dan XML sendiri dapat dilihat dari dua hal. Pertama, XML menggunakan *mark up languange* sedangkan JSON didasarkan pada bahasa Javascript. Kedua,  XML merupakan *mark up languange* yang hanya digunakan untuk menampilkan hal yang statik, sedangkan JSON dapat digunakan untuk membuat tampilan web menjadi interaktif (contoh: hover, clickable link, dll.).

<br />

## Cara pengimplementasian poin 1-4 (step kerjain tugas)
### 1. Membuat sebuah fungsi pada views.py.
#### a.) Import file models.py (agar database di models.py dapat diakses oleh views.py)
#### b.) data disimpan pada suatu variabel list dan dimasukkan dalam scope context, beserta dengan informasi nama dan NPM
<br />

### 2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py
#### a.) tambahkan ```path('katalog/', include('katalog.urls'))]``` pada pada variabel urlpatterns di urls.py pada project_django
#### b.) import untuk file views.py yang berada pada folder katalog di urls.py pada folder katalog
<br />
    
### 3. Memetakan data yang didapatkan ke dalam HTML.
#### a.) cantumkan nama dan NPM dengan menggunakan syntax {{nama_variabel}} untuk kedua variabel tersebut yang sudah ditulis pada views.py.
#### b.) menggunakan syntax {{nama_variabel}} untuk kedua variabel tersebut yang sudah ditulis pada views.py.
<br />

### 4. Melakukan deployment ke Heroku
#### a.) buat aplikasi di web heroku
#### b.) hubungkan aplikasi dengan repository tugas2 pada GitHub
#### c.) tambahkan repository secret HEROKU_API_KEY dengan key yang diambil dari heroku
#### d.) tambahkan repository secret HEROKU_API_NAME dengan nama aplikasi yang telah dibuat
#### e.) run ulang proses deployment di tab action
#### f.) Jika sudah ada centang hijau, situs aplikasi Heroku sudah bisa kita buka