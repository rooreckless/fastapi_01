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