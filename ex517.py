#딕셔너리: key:value...순서로 반복복
person = {'이름': '나귀욤', '나이':7, '키':120, '몸무게':23}
#print(person['이름'])
#print(person['나이'])

#print(person['별명']) 없는 키를 언급하면 에러발생
#print(person.get('이름')) #인덱스로 조회하나 []으로 조회하나 결과는 나온다

print(person)
person['최종학력'] = '유치원'
print(person)

person['키'] = 130
print(person)

person.update({'키':140, '몸무게':26})
print(person)

person.pop('몸무게')
print(person)

#person.clear()
#print(person)

print(person.keys())
print(person.values())
print(person.items())