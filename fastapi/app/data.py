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