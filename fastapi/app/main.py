from fastapi import FastAPI, HTTPException
from typing import Optional
from .data import get_user,User # data.pyから関数とUserクラスをインポート
from .data import get_books_by_category, Book # data.pyから関数とBookクラスをインポート
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI + PostgreSQL + Docker Compose!"}

@app.get("/abc")
async def abc():
    return {"message": "ABC"}


#--パスパラメータによるget--
@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    # 例えば、DBからuser_idに対応するユーザ情報を取得する処理をここに記述する
    # ここではダミーデータを使っている
    user: Optional[User] = get_user(user_id)
    # ↑get_user関数は、user_idに対応するUserオブジェクトを返すか、見つからない場合はNoneを返すので、
    # 変数userも型ヒントをする場合Optional[User]としている
    if user is None:
        # ユーザーが見つからない場合404エラーを返す
        raise HTTPException(status_code=404, detail="User not found")
    # ユーザーが見つかった場合はユーザーの内容を辞書にして返す
    return {"user_id": user.id, "username": user.name}


#--クエリパラメータによるget--
@app.get("/books/")
async def read_books(category: Optional[str]= None) -> list[dict[str, str]]:
    #↑返り値はリスト型であり、個々の要素は辞書型で、キーが文字列(str)、値も文字列(str)であることを示す
    # ↓例えばここで、DBからcategoryに対応する書籍情報を取得する処理をする
    # ここではダミーデータを使っている
    result = get_books_by_category(category)

    return [{"id" :book.id, "title": book.title, "category": book.category}
            for book in result]



# #-----
# # レスポンス処理についての前置き4章
# from datetime import datetime
# from pydantic import BaseModel, ValidationError
# # イベントを表すクラス
# class Event(BaseModel):
#     # イベント名、デフォルトは未定
#     name: str = "未定"
#     # 開催日時
#     start_datetime: datetime
#     # 参加者リスト、デフォルトはリスト
#     participants: list[str] = []
# # ダミーデータ辞書(外部からのイベントデータのつもり)
# external_data = {
#     "name": "FastAPI勉強会",
#     # "start_datetime": "2023-07-07 07:00",
#     # バリデーションエラーを意図的に起こしたいなら、以下のstart_datetimeの値を使う(strを渡してしまう)
#     "start_datetime": "abc",
#     "participants": ["山田", "鈴木","田中"]
# }


# #-----Eventクラス部分の実行が以下-----
# print("-----Eventクラス部分の実行-----")
# # 辞書をEventにつめてアンパックしてみる
# try:
#     event = Event(**external_data)
#     print("イベント名;", event.name, type(event.name)) # <- イベント名; FastAPI勉強会 <class 'str'>
#     print("開催日時;", event.start_datetime, type(event.start_datetime)) # <- 開催日時; 2023-07-07 07:00:00 <class 'datetime.datetime'>
#     print("参加者リスト;", event.participants, type(event.participants)) # <- 参加者リスト; ['山田', '鈴木', '田中'] <class 'list'>
# except ValidationError as e:
#     print("データのバリデーションエラーが発生しました。",e.errors()) # <- start_datetie = "abc"の時 : データのバリデーションエラーが発生しました。 [{'type': 'datetime_from_date_parsing', 'loc': ('start_datetime',), 'msg': 'Input should be a valid datetime or date, input is too short', 'input': 'abc', 'ctx': {'error': 'input is too short'}, 'url': 'https://errors.pydantic.dev/2.11/v/datetime_from_date_parsing'}]