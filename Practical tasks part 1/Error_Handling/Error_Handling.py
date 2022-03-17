
import datetime
import sys

# Функция с ошибкой
def errorMaker():
    print(1/0)
    print("1")

# Подмена обработчика ошибки и запись в файл логов
def run_with_log(f):
    def Exception(exctype, value, traceback):
        print(f"Исключение {exctype.__name__} : {value}")
        f = open('log.log', 'a', encoding='utf-8')
        f.write(f"{datetime.datetime.now():%H:%M:%S %d-%m-%Y}\n\t{exctype.__name__} : {value} : {traceback}\n\n")
        f.close()
    sys.excepthook = Exception
    f()


if __name__ == '__main__':
    run_with_log(errorMaker)