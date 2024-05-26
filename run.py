import json

from bs4 import BeautifulSoup

# Thay bằng đường dẫn thực tế của bạn
file_path = r"D:\Lấy lại truyện đã đọc ở NetTruyen mà không cần thông qua NetTruyenLoli\text.json"

# Đọc chuỗi JSON từ tệp tin
try:
    with open(file_path, "r", encoding="utf-8") as f:
        json_string = f.read()
except FileNotFoundError:
    print(f"Không tìm thấy tệp tin tại đường dẫn: {file_path}")
    exit(1)  # Thoát khỏi chương trình nếu không tìm thấy file

data = json.loads(json_string)
html_content = data["listHtml"]

soup = BeautifulSoup(html_content, 'html.parser')

# Trích xuất thông tin truyện
comics = []
for item in soup.find_all('div', class_='item'):
    title = item.find('a', title=True)['title']
    chapter = item.find('div', class_='view viewed').a['title']
    comics.append({'title': title, 'chapter': chapter})

for comic in comics:
    print(f"{comic['title']} - {comic['chapter']}")
    
 # By @makoto_sama from [WBW] - Wibu Wonderland - discord.gg/wbw with love
