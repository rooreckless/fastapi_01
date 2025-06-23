from typing import Optional

# Userクラス
# ユーザーIDと名前を属性として持つ
class User:
    def __init__(self, id: int, name: str):
        # 引数の型の指定は↑、クラス変数に代入が↓
        self.id = id
        self.name = name
# ダミーデータとして機能するユーザーリスト
user_list = [
    User(1, "内藤"),
    User(2, "辻"),
    User(3, "鷹木"),
]

# 指定されたユーザーIDに対応するユーザーを、user_listから検索する関数
# 引数 = ユーザーID(整数)
# 戻り値 = UserオブジェクトまたはNonde(みつからない場合)
def get_user(user_id: int) -> Optional[User]:
    for user in user_list:
        if user.id == user_id:
            # 指定されたIDを持つユーザーがいた場合、そのユーザーをretuurn
            return user
        # 指定されたIDを持つユーザーがいない場合Noneを返す
        return None
    
#----
# 書籍情報を表すクラス
class Book:
    def __init__(self, id: str, title:str, category:str):
        # 書籍ID, タイトル,カテゴリを引数からクラス変数に代入
        self.id = id
        self.title = title
        self.category = category

# ダミーの書籍データリスト
# category "techinal: 技術書, comics: コミック, magazine: 雑誌"
books = [
    Book(id="1",title="Python入門",category="technical"),
    Book(id="2",title="はじめてのプログラミング",category="technical"),
    Book(id="3",title="すすむ巨人",category="comics"),
    Book(id="4",title="DBおやじ",category="comics"),
    Book(id="5",title="週間ダイヤモンド",category="magazine"),
    Book(id="6",title="ザ・社長",category="magazine"),
]
# カテゴリに基づいて書籍を検索する関数
# もしcateogoryがNoneなら、すべての書籍を返す
def get_books_by_category(category: Optional[str] = None)-> list[Book]:
    if category is None:
        # カテゴリが指定されていない場合はすべての書籍を返す
        return books
    else:
        # 指定されたカテゴリに一致する書籍だけを返す
        # ↓リスト内包表記を使っている
        # booksのリスト内の個々の要素をbookとして回しながら、book.categoryが引数と一致したら、そのbookをリストに詰めて返す
        return [book for book in books if book.category == category]
    