# ちゃんとした実行
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)


# 誰かが配列名をミスしてしまう(選ばせる配列が崩れるが、タプルだと未然に防げる)
chose_from_two2 = ['A', 'B', 'C']
chose_from_two2.append('A')
chose_from_two2.append('C')

print("意図しない配列構造", chose_from_two2)

