import datetime

def save_hot_songs_to_file(songs):
    if not songs:
        print("空的。")
        return
    
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')  # 修正时间戳格式
    filename = f'hotmusic_{timestamp}.txt'
    
    try:
        # 保存歌曲列表到文件
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'Timestamp: {timestamp}\n')
            file.writelines([f"{song}\n" for song in songs])
    except IOError as e:
        print(f"写入文件时发生错误: {e}")

if __name__ == '__main__':
    # 假设 hot_songs 是从爬虫脚本返回的歌曲列表
    hot_songs = []  
    save_hot_songs_to_file(hot_songs)
    print('已保存到文件。')

