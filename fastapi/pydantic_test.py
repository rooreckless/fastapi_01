#--型ヒント--
def add(num1: int, num2: int) -> str:
    # 「num1はint型、num2はint型、このadd関数はstr型を返す」という意味
    """Add two numbers."""
    result:str = "足し算結果=>"
    # 変数定義時も形ヒント(str)を指定してから、値を代入

    return result+str(num1 + num2)

def hello(name: str) -> str:
    return f"こんにちは,{name}さん"

def divide(dividend:float, divisor:float) -> float:
    # divide関数の2つはfloatで戻りもfloat
    return dividend / divisor

#--Optional--

from typing import Optional

def divideOp(dividend: float, divisor: Optional[float] = None) -> Optional[float]:
    # Optionalは引数がNoneもしくはfloat型であることを示す
    # 戻り値もfloatもしくはNoneであることを示している。
    if divisor is None:
        # 引数divisorが渡されなかったらNone -> その場合10.0にされる
        divisor = 10.0
    # divide関数の2つはfloatで戻りもfloat
    return dividend / divisor

# --Annotated--
from typing import Annotated
# 引数でわたされた整数値が指定の範囲ないにあるかをチェックする関数
# 引数 : 数値型(Annotated)
# 戻り値 : None
def process_value(value: Annotated[int, "範囲: 0 <= value <= 100"])-> None:
    # 値が指定の範囲内にあるかをチェックする
    if 0 <= value <= 100:
        # 値が範囲内にだった場合
        print(f"値は範囲内です: {value}")
    else:
        # 値が範囲外にだった場合
        raise ValueError(f"値は範囲外です: {value}")

if __name__ == "__main__":
    print(add(1,2))

    print(hello("田中"))

    print(divide(10.0,2.0))

    print(divideOp(10.0))

    process_value(50)
    # process_value(110) <=ちゃんとエラー