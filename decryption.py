def caser_decryption(read_text, up_shift, low_shift):
    resulttext = ""
    for moji in read_text:
        # isupper/islower 大文字かどうかを区別し、Boolで返す
        if moji.isupper(): 
            # ord() 文字を数字に変換する
            # %26 はアルファベットの数　マイナスになることを防ぐ
            decrypted_char = chr((ord(moji) - ord("A") - up_shift) % 26 + ord('A'))
            resulttext += decrypted_char
        elif moji.islower():
            decrypted_char = chr((ord(moji) - ord("a") - low_shift) % 26 + ord('a'))
            resulttext += decrypted_char
        else:
            resulttext += moji
    return resulttext


file_name = "解読text/" + input("読み込むファイルの名前を入力してください。")
# upper_shift = int(input("大文字のシフト数値を入れてください。"))
# lower_shift = int(input("小文字文字のシフト数値を入れてください。"))
keyword = input("元文に入っていそうな単語を入力してください。")

try:
    with open(file_name, "r", encoding="utf-8") as f:
        read_text = f.read()

    print(f"[{file_name}]から暗号文を読み込みました。")

    print("---復号処理結果---")
    print_result = ""
    for up in range(26):
        for low in range(26):
            candidate = result = caser_decryption(read_text, up, low)

            # 復号結果を小文字にしてキーワードが含まれるか調べる
            if keyword.lower() in candidate.lower():
                print_result = result
                print(print_result)
                print(f"大文字のシフト数: {up}")
                print(f"小文字のシフト数: {low}")

    if print_result == "":
        print("キーワードが含まれる文章は見つかりませんでした。")

except FileExistsError:
    print(f"{file_name}ファイルが見つかりません。")
    print("スペルミスがないか確認してください。")
    print("また、「解読text」のフォルダの中ににファイルがあるかも確認してください。")

    