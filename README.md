# Penerapan Konsep Matematika Dalam Data Science
## Konsep Aljabar dalam Data Science
Aljabar adalah proses perhitungan yang mencakup entitas (wujud) non-numerik yang biasa disimbolkan dengan huruf “x” atau bisa dengan huruf apapun
![image](https://github.com/christadel27/Matrix/assets/133072315/42f9a917-8e2f-4df2-b4d7-a805b38bb07a)
Aljabar linear memakai persamaan linear (linear equation), yaitu persamaan yang pangkat tertinggi dari variabel/entitas x-nya selalu 1. 
![image](https://github.com/christadel27/Matrix/assets/133072315/6f399498-6cf0-463a-9e46-4a8a7dd78ab2)
Dalam persamaan linear  ada 2 jenis yaitu persamaan yang bereksponen bukan aljabar linear dan persamaan linear. Contohnya dapat dilihat pada gambar dibawah ini :
![image](https://github.com/christadel27/Matrix/assets/133072315/a75b8d8c-0ea4-4f83-9aca-0fd334768381)
Ada 4 istilah aljabar linear dalam Data Science yaitu : 
![image](https://github.com/christadel27/Matrix/assets/133072315/dd87c355-13a1-41e1-9d5e-77469837f36f)
1. Tensor adalah sebuah objek data atau generalisasi machine learning dari vector dan matrix ke sejumlah dimensi atau bisa juga di katakan objek data yang dibedakan berdasarkan dimensinya.
   ![image](https://github.com/christadel27/Matrix/assets/133072315/b5506f2b-7594-4020-ac73-109d4f3be657)
2. Scalar adalah angka yang berdiri sendiri, tidak memiliki dimesi, nilai numeriknya tunggal(sendiri), disimbolkan dengan huruf kecil dan miring(italic) dan punya tipe data seperti integer atau float. contohnya :
   ## X = 25 atau Y = 3.5
3. Vector bisa juga disebut dengan **array**, biasanya dikondisikan dalam bentuk urutan (baris), elemen/valuenya bisa diakses berdasarkan "_index_".
   ![image](https://github.com/christadel27/Matrix/assets/133072315/0dde8261-3cf4-4a7b-8225-e196b4462e58)
**CATATAN : kita harus mengubah bentuk list menjadi array dengan kode .array()**
4. Matrix : terdiri dari array/vector 2 dimensi, disimbolkan dengan huruf besar, miring dan bold. Contohnya sebagai berikut ini :
   ![image](https://github.com/christadel27/Matrix/assets/133072315/3de052a6-5ef5-4fd8-8258-6675bbdc40dc)
## Matrix dalam Data Science
Dalam python dan Numpy ada 6 jenis perubahan bentuk yaitu :
1. Symmetric Matrix : Kondisi dimana matrix yang berukuran persegi  dan saat dilakukan transposisi bentuk matrix ini **tidak** berubah.
   **Untuk melakukan Tranposisi kita bisa menggunakan kode .T**
2. Matrix Multiplication : perubahan matrix untuk operasi perkalian, bisa matrix dengan matrix atau matrix dengan vectors.
   ![image](https://github.com/christadel27/Matrix/assets/133072315/6a8260af-4bfb-4ece-ac81-927fd88092b5)
3. Matrix Inversion (kebalikan) : perubahan matrix untuk operasi membagi
   ![image](https://github.com/christadel27/Matrix/assets/133072315/f1035fe0-b424-47ff-a59c-f7e0ecd8516f)
## Implementasi aljabar Linear
Dalam implementasi aljabar seperti dalam teknologi untuk mengenal wajah user menggunakan fitur face ID. Dalam kasus kenapa wajah miring tetap bisa dikenali oleh fitur face ID itu karena ada **kontribusi eigenvectors dan eigenvalues** saat di-flip maupun di-sheared.
_Flip_ artinya wajah kita dibalikkan, sedangkan _sheared_ artinya dimiringkan.
![image](https://github.com/christadel27/Matrix/assets/133072315/c563c280-6392-4b3a-b290-38fd32c98875).
vectors yang sudah dilakukan flipping matrix sehingga disebut dengan **eigenvectors**.
eigenvalues berperan di mana dia adalah nilai scalar yang menunjukkan seberapa besar panjang eigenvectors berubah ketika wajahnya miring (diterapkan sheared matrix).
Ketika suatu wajah dilakukan perubahan matrix maka eigenvectors (vector) nya masih sama, seperti garis biru di flipping matrix tadi.Sedangkan** eigenvalues adalah scalar yang menunjukkan seberapa besar eigenvectors yang berubah (ukuran/panjang eigenvectors). **
**Eigenvectors** adalah special vector yang berbentuk v dari hasil transformasi (perubahan) matrix yang mana special vectors Av punya arah yang sama dengan v. 
Sedangkan **eigenvalues** adalah nilai scalar yang disimbolkan seperti gambar dari eigenvectors v.
Kalau eigenvalues adalah perubahan scalar dari eigenvectors, maka determinants dari sebuah matrix adalah perubahan eigenvectors dari matrix itu.
Operasi yang terakhir ini adalah cara untuk mengubah matrix menjadi eigenvectors dan eigenvalues dengan menjabarkan(breakdown) matrix yang kompleks/rumit.
Eigendecomposition punya karakteristik yaitu matrix adalah singular jika dan hanya jika salah satu dari eigenvalues-nya adalah nol.
Eigendecomposition tidak bisa diterapkan di semua operasi matrix Di kasus tertentu eigendecomposition bahkan melibatkan angka lebih kompleks. 
Dalam kasus machine learning, bakal sering menemui matrix berbentuk real symmetric matrix, di mana dengan mudah dan efisien untuk melakukan decomposed ke real-only eigenvectors dan real-only eigenvalues. 
Kalau A adalah real symmetric matrix maka equation-nya.
_**Referensi : Modul Binar Academy, untuk lebih lanjut silahkan buka Calculu.py**_

