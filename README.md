# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah mencetak banyak lulusan yang sukses dan memiliki reputasi sangat baik di dunia kerja. Namun demikian, terdapat tantangan signifikan yang dihadapi: tingginya angka siswa yang dropout sebelum menyelesaikan pendidikan mereka. Tingkat dropout yang tinggi merupakan masalah besar bagi institusi pendidikan karena dapat mencoreng reputasi, menurunkan efisiensi operasional, serta menimbulkan kerugian finansial. Untuk itu, Jaya Jaya Institut berinisiatif memanfaatkan teknologi data science untuk memprediksi potensi dropout siswa sejak dini agar dapat diberikan intervensi dan bimbingan khusus.

### Permasalahan Bisnis
Permasalahan bisnis yang ingin diselesaikan meliputi:
- Mendeteksi siswa dengan potensi tinggi untuk melakukan dropout.
- Memberikan insight dan pemahaman yang lebih baik kepada pihak manajemen melalui dashboard interaktif.
- Mengembangkan sistem machine learning sebagai alat bantu dalam pengambilan keputusan terkait manajemen siswa.

### Cakupan Proyek
Cakupan proyek yang akan dikerjakan:
- Melakukan eksplorasi dan pembersihan data siswa.
- Melakukan analisis data eksploratif (EDA) untuk memahami karakteristik siswa dan faktor-faktor yang mempengaruhi dropout.
- Membangun model machine learning untuk memprediksi kemungkinan dropout siswa. Model yang digunakan Random Forest, Gradient Boosting, dan XGBoost untuk membandingkan model yang terbaik.
- Mendeploy aplikasi machine learning di streamlit cloud comunity
- Mengembangkan dashboard interaktif menggunakan looker studio sebagai alat monitoring dan pengambilan keputusan.
- Membuat dokumentasi proyek dan prototype sistem yang dapat dijalankan oleh pihak non-teknis.

### Persiapan

Sumber data: dataset student's performance dari [dicoding dataset - students performance](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment: Apabila menginstal Python melalui Anaconda ataupun miniconda, Anda dapat menggunakan conda sebagai package manager dan environment management system. Langkah bisa menggunakan anaconda navigator dengan cara sebagai berikut :
1. Buka anacoda navigator
2. Buka Enviroments
3. Pilih Create
4. Masukan nama enviroment
5. Pilih versi Python 3.9.21
6. klik create
7. pilih anaconda prompt untuk instal file reqruiements.txt
8. Jalankan perintah
   ```
   pip install -r requirements.txt
   ```

Cara lain membuat enviroment menggunakan terminal
1. Buka terminal bisa menggunakan anaconda prompt
2. Jalankan Perintah
   ```
   conda create --name edutech python=3.9.21
   ```
3. Jalankan Perintah conda activate
   ```
   conda activate edutech
   ```
4. Jalankan perintah install library
   ```
   pip install -r requirements.txt
   ```

## Business Dashboard
Business dashboard yang telah dikembangkan bertujuan untuk memberikan gambaran menyeluruh mengenai performa siswa di Jaya Jaya Institut, serta mempermudah pengambilan keputusan strategis berbasis data. Dashboard ini dibangun dengan tampilan interaktif dan informatif.

📊 Dashboard tersedia di: [[Student's Performance Dashboard]](https://lookerstudio.google.com/reporting/0c0aeae4-7f7c-4040-87e2-1156bc1fe646)

Fitur-fitur pada Dashboard:
- Kontrol
  - Aplication Mode : Fitur ini sangat membantu dalam mengevaluasi efektivitas masing-masing jalur penerimaan terhadap risiko dropout maupun tingkat kelulusan siswa
- Statistik Utama:
  - Jumlah siswa yang masih aktif (Enrolled): 794
  - Jumlah lulusan (Graduate): 2.209
  - Jumlah siswa yang dropout: 1.421
- Visualisasi Berdasarkan Kategori:
  - Gender: Perbandingan jumlah dropout, enrolled, dan graduate berdasarkan jenis kelamin.
  - Debtor: Status hutang mahasiswa dan kaitannya dengan risiko dropout.
  - Marital Status: Status pernikahan mahasiswa saat mendaftar dan kaitannya dengan kelulusan/dropout.
  - Tuition Fees Up to Date: Keterlambatan pembayaran uang kuliah sebagai indikator dropout.
  - Scholarship Holder: Dampak kepemilikan beasiswa terhadap tingkat dropout.
  - Age at Enrollment: Distribusi umur saat mendaftar dan hubungannya dengan kelulusan/dropout.

Dashboard ini membantu pihak manajemen untuk:
- Mengidentifikasi kelompok siswa yang berisiko tinggi melakukan dropout.
- Mengevaluasi kebijakan beasiswa, sistem pembayaran, dan strategi rekrutmen.
- Memberikan intervensi atau bimbingan berdasarkan kategori yang relevan seperti usia, status sosial, dan status keuangan siswa.

## Menjalankan Sistem Machine Learning
Prototype sistem machine learning untuk prediksi potensi dropout siswa telah dikembangkan dan di-deploy menggunakan Streamlit. Sistem ini memungkinkan pengguna untuk melakukan prediksi berdasarkan input karakteristik siswa secara langsung melalui antarmuka web yang interaktif.

**Akses Aplikasi ML** = [Student Performance](https://dsw3zxt7dkvt7ekvtjweon.streamlit.app/)

**Antarmuka dan Cara Menggunakan:**

Pengguna akan diminta untuk memasukkan sejumlah fitur penting mahasiswa, antara lain:
- Curricular_units_2nd_sem_approved: Jumlah mata kuliah semester 2 yang disetujui/lulus
- Curricular_units_2nd_sem_grade: Nilai rata-rata semester 2
- Curricular_units_1st_sem_approved: Jumlah mata kuliah semester 1 yang disetujui/lulus
- Curricular_units_1st_sem_grade: Nilai rata-rata semester 1
- Tuition_fees_up_to_date: Status pembayaran uang kuliah (0 = tidak, 1 = ya)
- Scholarship_holder: Status beasiswa (0 = tidak menerima, 1 = menerima)
- Age_at_enrollment: Usia saat masuk institusi
- Debtor: Status hutang (0 = tidak, 1 = ya)
- Gender: Jenis kelamin (0 = perempuan, 1 = laki-laki)
- Application_mode: Jalur masuk (dalam bentuk kode numerik sesuai data)

Setelah data diisi, pengguna dapat mengklik tombol "🔍 Prediksi Status" dan sistem akan memberikan hasil prediksi apakah mahasiswa tersebut berpotensi:
- Lulus (Graduate),
- Dropout, atau
- Masih Aktif (Enrolled).

## Conclusion
Berdasarkan hasil dari proses penyelesaian masalah perusahaan edutech jaya jaya institut dapat disimpulkan 
- Proyek ini berhasil mengembangkan sistem prediksi risiko dropout mahasiswa di Jaya Jaya Institut menggunakan pendekatan machine learning berbasis data historis siswa.
- Berdasarkan hasil analisis korelasi dan uji model, fitur-fitur yang paling berpengaruh terhadap status mahasiswa yaitu
- ```
  ['Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 'Tuition_fees_up_to_date', 'Scholarship_holder', 'Age_at_enrollment', 'Debtor', 'Gender', 'Application_mode']
  ```
- Berdasarkan perbandingan model machine learning yang digunakan didapatkan acurasi model yang paling baik yaitu model gradient bosting dengan akurasi 0.751412429378531
- Deploy aplikasi prediksi dilakukan di streamlit cloud comunity yang berguna untuk membantu manajemen dalam mengetahui dan mencegah lebih awal potensi mahasiswa dropout
- Dashboard looker studio menyajikan insight visual yang bermanfaat untuk pengambilan keputusan oleh tim Manajaemen

### Rekomendasi Action Items
Berikut beberapa langkah yang direkomendasikan untuk Jaya Jaya Institut:
- Menerapkan sistem prediksi secara rutin di awal dan pertengahan semester untuk mendeteksi potensi dropout secara dini.
- Memberikan bimbingan atau konseling khusus bagi mahasiswa yang terindikasi berisiko tinggi dropout.
- Melakukan evaluasi pada faktor-faktor utama seperti status pembayaran kuliah, status beasiswa, dan performa akademik di semester awal.
- Mengoptimalkan jalur pendaftaran (Application Mode) yang menunjukkan rasio dropout rendah melalui kebijakan penerimaan yang selektif.
