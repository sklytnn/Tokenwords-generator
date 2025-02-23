import random
import nltk
from nltk.corpus import wordnet

# Download dataset jika belum ada
nltk.download('wordnet')

# Fungsi untuk membersihkan kata (hapus underscore, strip, dan apostrof)
def clean_word(word):
    return word.replace('_', '').replace('-', '').replace("'", "")

# Fungsi untuk memproses kata (maksimal 6 huruf, minimal 3 huruf)
def process_word(word):
    word = clean_word(word)
    return word if 3 <= len(word) <= 6 else None  # Hanya ambil yang panjangnya 3-6 huruf

# Ambil semua noun dan verb dari WordNet
raw_nouns = {w.name().split('.')[0] for w in wordnet.all_synsets('n')}
raw_verbs = {w.name().split('.')[0] for w in wordnet.all_synsets('v')}

# Proses kata, filter yang memenuhi syarat
nouns = list(filter(None, {process_word(w) for w in raw_nouns}))
verbs = list(filter(None, {process_word(w) for w in raw_verbs}))

# Ambil hanya yang panjangnya maksimal 6 huruf
nouns = [word for word in nouns if len(word) <= 6]
verbs = [word for word in verbs if len(word) <= 6]

# Acak daftar kata
random.shuffle(nouns)
random.shuffle(verbs)

# Ambil 4000 noun + 4000 verb agar total 8000 kata
final_words = nouns[:4000] + verbs[:4000]

# Acak ulang hasil akhir
random.shuffle(final_words)

# Format sebagai JavaScript array dengan 12 kata per baris dan pembatas setiap 180 kata
js_content = "export const words = [\n"
for i in range(0, len(final_words), 12):
    # Menambahkan 12 kata per baris
    js_content += "  " + ', '.join(f"'{w}'" for w in final_words[i:i+12]) + ",\n"
    
    # Menambahkan komentar dan pembatas setiap 180 kata
    if (i + 12) % 180 == 0:
        js_content += "  // ---------- Pembatas 180 kata ----------\n"

# Menghapus koma terakhir dan menambahkan penutupan array
js_content = js_content.rstrip(",\n") + "\n];\n"

# Simpan ke dalam file words.js
with open("words.js", "w") as f:
    f.write(js_content)

print(f"? words.js berhasil dibuat dengan {len(final_words)} kata!")
