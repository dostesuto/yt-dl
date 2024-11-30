import yt_dlp

def download_video(url):
    # yt-dlpのオプションを設定
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # 最良の動画と音声を選択
        'outtmpl': '%(title)s.%(ext)s',  # 出力ファイル名のフォーマット
    }

    try:
        # yt-dlpを使って動画をダウンロード
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("ダウンロードが完了しました！")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    url = input("YouTubeのURLを入力してください: ")
    download_video(url)
