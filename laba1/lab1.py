import requests
from bs4 import BeautifulSoup
import os

url = "https://omgtu.ru/general_information/the-structure/the-department-of-university.php"

headers = {
"User-Agent": (
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) "
"Gecko/20100101 Firefox/124.0"
)
}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("Ошибка загрузки:", response.status_code)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

#Находим блок, где точно есть список кафедр
content = soup.find(id="pagecontent")

#Все теги <a> внутри него
kafedry_links = content.find_all("a")

#Извлекаем текст и ссылку
kafedry = [a.get_text(strip=True) for a in kafedry_links if a.get_text(strip=True)]

#Сохраняем на рабочий стол
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, "kafedry_omgtu.txt")

with open(file_path, "w", encoding="utf-8") as file:
    for line in kafedry:
        file.write(line + "\n")

print("Список кафедр с ссылками сохранён на рабочем столе:", file_path)
