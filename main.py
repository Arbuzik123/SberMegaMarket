import asyncio
from Searchengines.startFind import SBFind
from DefOzon.test import test
drivers = []
async def main():
    price = 'result.xlsx'
    # price = rf'"C:\Users\Dimulka\Desktop\аштфд\YANDEX.xlsx"'
    # print("start")
    # # ФУНКЦИИ ПОИСКА ТОВАРОВ-------------------------------------------------------------------------------------------
    # await OzonFind(price)  # Вставить файл с прайсом
    # await YandexFind(price)
    # await WBFind(price)
    await SBFind(price)
    # ФУНКЦИЯ ДЛЯ УДАЛЕНИЯ ИЗ ЯЧЕЕК СИМВОЛОВ ПОСЛЕ "Rubl"
    # test(p)
    # ФУНКЦИИ ОБНОВЛЕНИЯ ЦЕН-------------------------------------------------------------------------------------------
    # print("Запуск 1 функции")
    # await createFilesOzon("OZON.xlsx") #Вставка пути к файлу Ozon
    # print("Запуск 2 функции")
    # await createFilesYandex("YANDEX.xlsx")#Вставка пути к файлу Yandex
    # print("Запуск 3 функции")
    # await createFilesWildberries(rf"wb1.xlsx")  # Вставка пути к файлу Wildberries
    # print("Запуск 4 функции")
    # await createFilesSberMega(price)  # Вставка пути к файлу SberMega
if __name__ == '__main__':
    asyncio.run(main())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
