import time
from get_hot_songs import scrape_hot_songs
from process_hot_songs import save_hot_songs_to_file

def main():
    hot_songs = scrape_hot_songs()
    
    if hot_songs:
        print("今日热歌：")
        for song in hot_songs:
            print(song)
    
        user_input = input('要不要保存呢？(是/否): ')
        
        if user_input.lower() == '是':
            save_hot_songs_to_file(hot_songs)
            print('OJBK,已保存到文件。')
    else:
        print("坏了捏，不能获取。")
    
    time.sleep(3)

if __name__ == '__main__':
    main()

