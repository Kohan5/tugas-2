# **Tugas 2 PBP (Aplikasi Katalog)**

## Link: [Heroku](https://tugas2kohan.herokuapp.com/katalog/) dan [Gambar Bagan](https://drive.google.com/file/d/1adJu-4myJMLuoeC-L7Sp9YN8r55Tis9R/view?usp=sharing)

## Kenapa menggunakan virtual environment?
Virtual environment digunakan untuk memisahkan antara lingkungan python yang kita kerjakan dengan lingungan python yang lainnya. Dengan begitu, jika kita ingin membuat aplikasi django dengan versi python tertentu, maka versi python yang ada dalam environment dapat menyesuaikan dengan kebutuhan tanpa mengubah versi python secara keseluruhan. Pembuatan aplikasi di django sebenarnya bisa dilakukan tanpa menggunakan virtual environment, tetapi dapat mempersulit pengguna, terutama jika proyek django yang dikerjakan tidak hanya satu. Hal ini terjadi karena versi-versi libraries python di komputer kita harus disesuaikan setiap kali kita mengganti proyek yang kita kerjakan.

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