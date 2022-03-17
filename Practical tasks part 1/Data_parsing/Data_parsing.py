import requests
from collections import Counter
import matplotlib.pyplot as plt


def statistik():
    # Парсеринг
    url = requests.get('https://raw.githubusercontent.com/Newbilius/Old-Games_DOS_Game_Gauntlet/master/GAMES.csv')
    true_data = []
    correct_data_format = ((url.text).replace('"', '')).splitlines()
    for line in correct_data_format:
        data = (line.split(';'))[1::2]
        if data[1] != 'не издана':
            true_data.append(data)
    
    # Обработка данных (разбиение по массивам)
    alldata = locals()
    for year in range(1981, 2009):
        alldata[f'{year}'] = []
    for line in true_data:
        alldata[f'{line[1]}'].append(line[0])
    
    # График кол-во вышедших игр в год
    ONyears = dict()
    for year in range(1981, 2009):
        genre_counter = {year: len(alldata[f'{year}'])}
        ONyears.update(genre_counter)
    plt.bar(ONyears.keys(), ONyears.values())
    plt.savefig("Года.png")

    # Графики жанров по годам
    figure, axis = plt.subplots(14, 2)
    for year in range(1981, 2009):
        yeardata = Counter(alldata[f'{year}'])
        current_year = year - 1981
        axis[current_year // 2, current_year % 2].set_title(year)
        axis[current_year // 2, current_year % 2].bar(yeardata.keys(), yeardata.values())
        for tick in axis[current_year // 2, current_year % 2].get_xticklabels():
            tick.set_rotation(45)
    figure.set_size_inches(20, 80)
    plt.subplots_adjust(hspace=0.8)
    plt.savefig("По годам.png", dpi=100)

    # Поломанный график жанров по годам
    figure, axis = plt.subplots(1, 1)
    for year in range(1981, 2009):
        yeardata = Counter(alldata[f'{year}'])
        plt.bar(year, yeardata.keys(), yeardata.values(),  1, label='Men')
        plt.savefig("Тест.png", dpi=100)
    print("Графики построены")
    plt.show()


if __name__ == '__main__':
    statistik()