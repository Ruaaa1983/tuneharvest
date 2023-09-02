import requests
from bs4 import BeautifulSoup

def scrape_hot_songs():
    url = 'https://music.163.com/discover/toplist?id=3778678'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try:
        # 发送请求
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"报错了捏: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    hot_songs = []

    # 获取歌曲列表
    song_elements = soup.select('#song-list-pre-cache ul li a')
    
    for i, song_element in enumerate(song_elements, start=1):
        title = song_element.get_text()
        hot_songs.append(f"{i}. {title}")
    
    return hot_songs

if __name__ == '__main__':
    hot_songs = scrape_hot_songs()
    for song in hot_songs:
        print(song)

