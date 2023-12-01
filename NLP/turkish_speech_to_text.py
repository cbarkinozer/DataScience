import speech_recognition as sr
import time


def split_audio(file_path, chunk_size):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_duration = source.DURATION
        num_chunks = int(audio_duration / chunk_size) + 1

        for i in range(num_chunks):
            start_time = i * chunk_size
            end_time = min((i + 1) * chunk_size, audio_duration)

            with sr.AudioFile(file_path) as chunk_source:
                chunk_audio_data = recognizer.record(chunk_source, duration=end_time - start_time, offset=start_time)

                try:
                    text = recognizer.recognize_google(chunk_audio_data, language='tr-TR')
                    print(text)
                except sr.UnknownValueError:
                    print("<Anlaşılmıyor>")
                except sr.RequestError as e:
                    print("Google Konuşma Tanıma hizmetine yapılan istekte hata oluştu (parça numarsı:) {}): {}".format(i + 1, e))

if __name__ == "__main__":
    
    # Türkçe olmayan kelimeler yanlış anlaşılıyor onun dışında başarılı. 1.5 saatlik bir dosyayı 20-30 dk'da işliyor çünkü Google API'ye istek atıyor ama ücretsiz.
    
    t0 = time.time()
    print("Yazmaya başlıyor...")
    print("---------------------------------------------------------------------------")

    audio_file_path = "./rec.wav"  # rec.wav ismindeki dosyalar ile çalışıyor yalnızca

    try:
        split_audio(audio_file_path, chunk_size=30)
    except FileNotFoundError:
        print(f"Error: File not found at {audio_file_path}")

    print("---------------------------------------------------------------------------")
    print("Yazma bitti...")
    t1 = time.time()
    total = t1-t0
    print("İşlemin aldığı süre: ", total)
