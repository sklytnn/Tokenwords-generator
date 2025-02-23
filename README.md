# Tokenwords Generator

Tokenwords Generator adalah skrip Python yang menghasilkan daftar kata acak yang terdiri dari noun (kata benda) dan verb (kata kerja) dengan panjang 3-6 huruf. Hasil akhirnya disimpan dalam file **words.js** dalam format array JavaScript.

## Instalasi

1. **Clone repositori ini**

   ```bash
   git clone https://github.com/sklytnn/Tokenwords-generator.git
   cd Tokenwords-generator
   ```

2. **Buat virtual environment (opsional, tetapi disarankan)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate  # Untuk Windows
   ```

3. **Instal dependensi Python**

   ```bash
   pip install nltk
   ```

4. **Instal dependensi Node.js**

   ```bash
   npm install
   ```

5. **Jalankan skrip untuk menghasilkan words.js**

   ```bash
   python3 generate_words.py
   ```

## Output

Setelah dijalankan, skrip akan membuat file **words.js** yang berisi daftar kata dalam format JavaScript array:

```javascript
export const words = [
  'apple', 'table', 'drink', ...
];
```

## Lisensi

Proyek ini menggunakan lisensi MIT.

