# 입력과 출력
# 파일 읽기 = r , 쓰기(기존파일 삭제) = w, 추가 = a

f = open('/Volumes/128No1/study/fastcamp/resource/review.txt', 'r')
contents = f.read()
print(contents)
# print(dir(f))
# 반드시 close 리소스 반환
f.close() # 파일을 오픈하면 꼭 닫아줘야함

print("\n")

# 위드문은 클로즈 안해줘도 됨
with open('/Volumes/128No1/study/fastcamp/resource/review.txt', 'r') as f:
    c = f.read()
    print(iter(c))
    print(list(c))
    print(c)

print("\n")

# read : 전체 내용 읽기, read(10) : 10글자 읽기


with open('/Volumes/128No1/study/fastcamp/resource/review.txt', 'r') as f:
    for c in f:
        # print(c)
        print(c.strip()) # 공백 및 엔터제거

print()

# 예제4
with open('/Volumes/128No1/study/fastcamp/resource/review.txt', 'r') as f:
    contents = f.read()
    print('>', contents)
    contents = f.read()
    print('>', contents)  # 내용 없음
    f.seek(0, 0)
    contents = f.read()
    print('>', contents)

# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기

print()

# 예제5
with open('/Volumes/128No1/study/fastcamp/resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

# readlines : 전체 읽은 후 라인 단위 리스트 저장

print()
print()

# 예제6
with open('/Volumes/128No1/study/fastcamp/resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    print()
    for c in contents:
        print(c, end='')

print()
print()

# 예제7
with open('/Volumes/128No1/study/fastcamp/resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)
    print('Average : {:6.3f}'.format(sum(score) / len(score)))

# 파일 쓰기

# 예제1
with open('/Volumes/128No1/study/fastcamp/resource/test.txt', 'w') as f:
    f.write('niceman!')

# 예제2
with open('/Volumes/128No1/study/fastcamp/resource/test.txt', 'a') as f:
    f.write('niceman!!')

# 예제3
from random import randint

with open('/Volumes/128No1/study/fastcamp/resource/score2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(50, 100)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('/Volumes/128No1/study/fastcamp/resource/test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5
with open('/Volumes/128No1/study/fastcamp/resource/test3.txt', 'w') as f:
    print('Test Contents!', file=f)
    print('Test Contents!!', file=f)
