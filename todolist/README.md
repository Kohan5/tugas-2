# **Tugas 4 PBP - (Aplikasi To Do List)**

## Link
[Klik disini untuk membuka aplikasi yang sudah di-deploy](https://tugas2kohan.herokuapp.com/todolist/)
<br />

## Kegunaan {% csrf_token %} pada elemen `<form>` 
Secara general, token digunakan sebagai keamanan aplikasi. Secara spesifik, token digunakan untuk menambah argumen pada sebuah request dengan token yang berupa angka besar yang ditentukan secara random. Jika user yang menjalankan berbeda, maka tokennya juga akan berbeda. Token inilah yang digunakan sebagai perbandingan dengan token yang dimiliki user ketika user ingin melakukan Post atau Get. Jika tokennya sama, maka akan dilanjutkan.

Referensi: https://stackoverflow.com/questions/5207160/what-is-a-csrf-token-what-is-its-importance-and-how-does-it-work

<br />

## Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
Jika tidak ada, semua orang dapat dengan mudah mengakses data orang lain

<br />

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?
Ya, kita bisa membuat elemen form secara manual tanpa generator 

<br />

<br />

## Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Berikut merupakan contoh pembuatan form secara manual
```
<form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Title:</td>
                <td><input type="text" name="title" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Description: </td>
                <td><input type="text" name="description" class="form-control"></td>
            </tr>
        </table>
        <input type="submit" name="submit" value="Create"/>
</form>
```
Form dibuat langsung di html. Ditandai dengan pembatas `<form> </form>` dengan method POST, lalu untuk keperluan kerapihan, dibuat tabel karena perlu ada 2 input pada form ini, masing-masing dalam sebuah tr. Textfield yang akan diisi oleh user ditandai dengan awalan input, dilanjutkan dengan beberapa argumen yang dibutuhkan. name merupakan argumen yang penting karena dibutuhkan untuk retrieval data. Dibawah tabel input, diperlukan tombol submit untuk menyimpan hasil input user. 

<br />

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. 
Hasil input dari user bisa diakses melalui `request.POST.get({nama_input})` pada `todolist/views.py`. Data kemudian digunakan untuk membuat instansi objek class pada `todolist/models.py` dengan menggunakan method `{ClassName}.objects.create(args)` dengan `args` disesuaikan berdasarkan atribut yang ada pada class tersebut.   
Pada tahap ini, data dari input user pada form sudah masuk ke database, sekarang diperlukan untuk dimunculkan pada html. Untuk itu, objek ini perlu di pass dalam `context` yang ada pada fungsi yang bertujuan untuk menampilkan html, pada kasus ini, `show_todolist`. Dalam fungsi itu, instansi objek baru akan diambil pada statement `{ClassName}.objects.filter(user=request.user)` yang masuk ke context dalam bentuk list.  
Setelah di dalam context, kita dapat mengakses data tersebut pada file html. Tiap objek pada list tersebut akan diiterasi pada sebuah `for-loop`. Dalam `for-loop` tersebut, kita dapat mengakses tiap atribut pada objek tersebut untuk ditampilkan sesuai format yang kita inginkan.

<br />

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. 
- Melakukan perintah `python manage.py startapp todolist` untuk menginisiasi file-file yang dibutuhkan untuk membuat aplikasi baru
- Membuat fungsi untuk menghandle request html pada views.py lalu melakukan routing dari fungsi tersebut kepada urls yang sesuai pada file `todolist/urls` dengan menambahkan `path('', show_todolist, name='show_todolist'),` dan `path('todolist/', include('todolist.urls')),` pada file `project_django/urls`
- Membuat class baru pada file `todolist/models.py` dengan atribut yang sesuai dengan ketentuan tugas, lalu menjalankan `python manage.py makemigrations` dan `python manage.py migrate`.
- Membuat fungsi login, logout, dan register pada `todolist/views.py` untuk menghandle registrasi, login, logout, serta implementasi COOKIES
- Melakukan routing untuk fungsi-fungsi tersebut pada file `todolist/urls.py` dengan menambahkan masing-masing fungsi pada urlpatterns
- Membuat fungsi `create_task` pada `todolist/views.py` dengan implementasi retrieval data pada form manual seperti yang dijelaskan pada poin sebelumnya. Hal ini mencakup membuat file html yang berisi form serta tombol submit.
- Membuaat fungsi untuk menghapus task dan mengubah status task, `deletetask` dan `finishtask`, dengan logika yang cukup simpel memanfaatkan method dari objects.
- Melakukan routing untuk masing-masing fungsi tersebut pada file `todolist/urls.py`
- Menambahkan button untuk `finishtask` dan `deletetask` pada `todolist.html`
- Setelah semua sudah berjalan semestinya pada local, dilakukan add, commit, dan push, lalu deployment melalui Github Actions.

<br />

# **Tugas 5 PBP - (Desain pada Aplikasi To Do List)**

## Link
[Klik disini untuk membuka aplikasi yang sudah di-deploy](https://tugas2kohan.herokuapp.com/todolist/)
<br />

## perbedaan dari Inline, Internal, dan External CSS
- **Inline CSS** <br />
merupakan penulisan kode CSS langsung pada atribut elemen HTML. Kelebihan dari
inline CSS adalah proses request HTTP lebih singkat sehingga proses load website akan lebih cepat, dapat memperbaiki kode dengan cepat, dan membantu ketika developer ingin menguji perubahan pada satu elemen. Namun kekurangan inline CSS adalah kurang efisien dikarenakan inline CSS hanya dapat diterapkan pada satu elemen HTML.
- **Internal CSS** <br />
merupakan penulisan kode CSS dalam tag style dan penulisan kode HTML di header file HTML. Untuk membuat memiliki tampilan yang berbeda-beda sangat cocok menggunakan Internal CSS dikarenakan Internal CSS dapat membuat tampilan unik pada setiap page (halaman) website. Kelebihan dari Internal CSS adalah HTML dan CSS berada di dalam satu file sehingga tidak memerlukan untuk upload beberapa file. Selain itu, perubahan pada Internal CSS berlaku pada satu halaman saja. Namun, kekurangan dari Internal CSS adalah membuat performa website lebih lambat karena terdapat file CSS yang berbeda-beda pada setiap halaman akan membuat loading ulang setiap user mengganti halaman website.
- **External CSS**<br />
merupakan penulisan kode CSS yang terpisah dengan kode HTML. External CSS ditulis pada file khusus `(.css)` dan diletakkan setelah bagian head halaman. Kelebihan dari External CSS adalah membuat ukuran dan struktur kode file HTML menjadi lebih kecil dan rapih, loading website lebih cepat dan file CSS dapat digunakan di beberapa halaman sekaligus. Namun, kekurangan dari External CSS adalah gagalnya pemanggilan file CSS oleh file HTML yang menyebabkan halaman web bisa saja menjadi berantakan. Hal tersebut dapat terjadi apabila koneksi internet tidak stabil.

<br />

## tag pada HTML5
- `<div>`  = Merepresentasikan container/section.
- `<head>` = Mendefinisikan head dari dokumen HTML, biasanya berisi title.
- `<body>` = Mendefinisikan body dari dokumen HTML.
- `<h1>` to `<h6>` = Mendefinisikan ukuran heading HTML.
- `<title>` = Mendefinsikan title dari dokumen HTML.
- `<link>` = Mendefinisikan hubungan antara dokumen HTML dengan dokumen external.
- `<meta>` = Menyediakan metadata terstruktur mengenai konten dokumen.
- `<a>` = Mendefinisikan hyperlink.

<br />

## tipe-tipe CSS selector
- ID Selector adalah tipe CSS selector yang berfungsi untuk menambahkan style dengan ID tertentu. Penggunaannya dengan menuliskan hashtag diikuti dengan nama ID. Contohnya `#idSatu {`.
- Class Selector adalah tipe CSS selector yang berfungsi untuk menambahkan style dengan class tertentu. Penggunannya dengan menuliskan titik diikuti dengan nama classnya. Contohnya `.classSatu {`.
- Tag Selector adalah tipe CSS selector yang berfungsi untuk menambahkan style pada sebuah tag. Penggunaannya dengan menuliskan tag yang ingin diberikan style, Contohnya `div {`.

<br />