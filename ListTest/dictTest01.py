# 딕셔너리 = 오브젝트
# 딕셔너리 => key : value가 쌍으로 존재
# 딕셔너리 출력하는 방법 -> dict['key'] (절대 dict.key로는 출력 X)
# phone_book = {'name':'홍길동', 'age':7, 'class':'고급'}

phone_book = {}
phone_book['홍길동'] = '010-1234-5678'
phone_book['강감찬'] = '010-1234-5679'
phone_book['이순신'] = '010-1234-5680'

print(phone_book)

# 모든 key만 출력
print(phone_book.keys()) # dict_keys(['홍길동', '강감찬', '이순신'])
# 모든 value만 출력
print(phone_book.values()) # dict_values(['010-1234-5678', '010-1234-5679', '010-1234-5680'])


# 문제) phone_book을 강감찬 010-1234-5679 이런 방향으로 출력시키시오.
#       (단, for문 사용)

for key in phone_book.keys():
    print(key,phone_book[key]) # 홍길동 010-1234-5678 ...
