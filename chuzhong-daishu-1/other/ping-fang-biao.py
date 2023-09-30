import numpy as np
from decimal import *

# 生成《初中代数第一册》 “1.16 平方表和立方表” 中的 “四位平方表”
# 生成的结果和书上的表相比，已知的不同有：
#   1.  “2.2” 的修正值表“1”，生成结果为“5”，原书为“4”
# 其它可能不同的地方：（因为原书影印件不清楚，不能肯定）
#   1. “2.0” 修正值 “6”
#   2. “2.2” 修正值 “7”

def get_table(type):
    table = []
    for num in np.arange(2.0, 2.5, 0.1):
        base = str(round(num, 2))
        lst = [base]

        # 添加第 3 位数的计算结果
        for third in range(10):
            num = Decimal(base + str(third))
            result = (num * num).quantize(Decimal('.000'), type)
            lst.append(str(result))

        # 添加第 4 位数的修正值
        for fourth in range (1, 10):
            values = {}
            for third in range(10):
                num1 = Decimal(base + str(third))
                num2 = Decimal(base + str(third) + str(fourth))
                result1 = (num1 * num1).quantize(Decimal('.0000'), type)    # 中间值多保留一位
                result2 = (num2 * num2).quantize(Decimal('.0000'), type)
                diff = (result2 - result1).quantize(Decimal('.000'), type)  # 差值才按要求保留 3 位
                if diff in values:
                    values[diff] += 1
                else:
                    values[diff] = 1
            max_key, max_value = '', 0
            for key, value in values.items():
               if max_value < value:
                    max_key, max_value = key, value
            max_key *= 1000
            max_key = max_key.quantize(Decimal('0'), type)
            lst.append(str(max_key))

        table.append(lst)

    return table


table = get_table(ROUND_HALF_UP)

for row in table:
    print(row)

print()

print("""\\begin{tblr}{vlines,
    hline{1, 7} = {1pt, solid},
    hline{2} = {solid},
    vline{1, 21} = {1pt, solid},
    vline{12} = {1}{-}{},
    vline{12} = {2}{-}{},
    columns={colsep=2.5pt, c, $$},
}
    N   & 0     & 1     & 2     & 3     & 4     & 5     & 6     & 7     & 8     & 9     & 1 & 2  & 3  & 4  & 5  & 6  & 7  & 8  & 9 \\\\"""
)
for row in table:
    line = " & ".join(row)
    print("    " + line + " \\\\")
print("\\end{tblr}")

