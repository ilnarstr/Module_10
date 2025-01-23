import time
from time import sleep
import threading
from tkinter.scrolledtext import example
from turtledemo.penrose import start


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f'Какое-то слово № {i}'
            file.write(word + '\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time1 = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time1 = time.time()
execution_time1 = end_time1 - start_time1
print(f'Работа функций {execution_time1:.2f} секунд')

start_time2 = time.time()

thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time2 = time.time()
execution_time2 = end_time2 - start_time2
print(f'Работа потоков {execution_time2:.2f} секунд')