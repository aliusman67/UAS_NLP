import language_tool_python

def grammar_check(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    return matches

def correct_grammar(input_text, matches):
    if len(matches) == 0:
        print("Tidak ada kesalahan tata bahasa.")
        return input_text

    # Mengganti kesalahan dengan saran yang diberikan oleh LanguageTool
    corrected_text = language_tool_python.utils.correct(input_text, matches)
    
    print("Kesalahan tata bahasa telah diperbaiki.")
    return corrected_text

def process_text_from_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
            matches = grammar_check(text)
            corrected_text = correct_grammar(text, matches)

        with open(output_file, 'w') as file:
            file.write(corrected_text)

        print(f"Hasil diperbaiki telah disimpan di '{output_file}'.")
    except FileNotFoundError:
        print(f"File '{input_file}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    print("Pilih mode:")
    print("1. Masukkan teks melalui input standar.")
    print("2. Baca teks dari file dan simpan hasil perbaikan di file baru.")
    
    choice = input("Masukkan pilihan (1/2): ")

    if choice == '1':
        input_text = input("Masukkan teks bahasa Inggris untuk diperiksa: ")
        matches = grammar_check(input_text)
        corrected_text = correct_grammar(input_text, matches)
        print("\nTeks setelah perbaikan:")
        print(corrected_text)
    elif choice == '2':
        input_file = input("Masukkan nama file teks yang akan diperiksa: ")
        output_file = input("Masukkan nama file untuk menyimpan hasil perbaikan: ")
        process_text_from_file(input_file, output_file)
    else:
        print
