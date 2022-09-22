# **Tugas 2 PBP (Aplikasi Katalog)**

## Link Heroku dan Foto Postman
- [Foto Postman XML](https://drive.google.com/file/d/1tnd_FIw9VqJ46me5zu5Vclhz6hQJ55et/view?usp=sharing)
- [Foto Postman JSON](https://drive.google.com/file/d/1GWeWRDtyLm9dREqnLJvqd1pGKINT-_z7/view?usp=sharing)
- [Foto Postman HTML](https://drive.google.com/file/d/1cC-trcrYfGW4485fsYBzfVw4f-4avfJw/view?usp=sharing)
- [HTML Heroku]()
- [XML Heroku](https://tugas2kohan.herokuapp.com/mywatchlist/xml/)
- [JSON Heroku](https://tugas2kohan.herokuapp.com/mywatchlist/json/)
<br />

## Perbedaan antara JSON, XML, dan HTML
Untuk membedakan ketiganya, pertama kita dapat memisahkan antara HTML dan JSON & XML. HTML dibuat untuk menjadi bahasa dengan aturan yang tidak terlalu ketat sehingga pembuatan web dengan html dapat menjadi lebih mudah. Berbeda dengan HTML, XML dan JSON dibuat untuk memudahkan pengguna dalam membaca *code* dengan cara menjaga struktur informasi dengan mengorbankan aturan yang lebih ketat (seperti pendahulu HTML yaitu SGML).

Untuk perbedaan JSON dan XML sendiri dapat dilihat dari dua hal. Pertama, XML menggunakan *mark up languange* sedangkan JSON didasarkan pada bahasa Javascript. Kedua,  XML merupakan *mark up languange* yang hanya digunakan untuk menampilkan hal yang statik, sedangkan JSON dapat digunakan untuk membuat tampilan web menjadi interaktif (contoh: hover, clickable link, dll.).

<br />

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform
Data delivery sangat sering terjadi dalam pengimplementasi sebuah platform. Hal tersebut menandakan terjadinya pertukaran data user dengan data yang ada di server. Data delivery juga berguna untuk membantu mempermudah melakukan proses pengiriman data. Dalam penggunaannya, data delivery menggunakan format HTML, JSON, dan XML supaya data yang dikirim mudah dipahami berbagai programming language untuk didevelop serta dapat diterima dengan baik dan dipahami oleh user.

<br />

## Cara pengimplementasian poin-poin pengerjaan
1. Buat environment di dalam folder yang sama dengan folder yang digunakan pada repository
2. Buat aplikasi "mywatchlist" dengan cara menjalankan perintah 'python manage.py startapp watchlist'
3. Lakukan route url dengan memasukkan 'path('mywatchlist/', include('mywatchlist.urls'))' supaya urlpatterns pada project_django dapat terhubung dengan mywatchlist
4. Masukkan mywatchlist pada installed_app di setting.py
5. Lakukan path route di dalam mywatchlist/urls.py agar terhubung dengan fungsi yang akan dijalankan pada mywatchlist/views.py
6. Buat model data di mywatchlist/models.py dengan fields yang sudah ditentukan
7. Lakukan migrasi dengan command 'python manage.py makemigrations' dan 'python manage.py migrate'