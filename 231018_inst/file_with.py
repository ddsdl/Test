with open("with.txt", "w", encoding='utf-8') as f:
    f.write("with 블록을 벗어나면, 자동으로 파일객체 f는 close 됩니다.")