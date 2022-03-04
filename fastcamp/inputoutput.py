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
        # print(c) # 한줄씩 읽어와서 \n 이 자동작동
        print(c.strip()) # 라인끝의 공백 및 줄바꿈 제거

print("\n")


with open('/Volumes/128No1/study/fastcamp/resource/review.txt', 'r') as f:
    contents = f.read()
    print('>', contents)
    contents = f.read()
    print('>', contents)  # 내용 없음
    f.seek(0, 0)
    contents = f.read()
    print('>', contents) # 리드로 한번 읽어온 다음 커서가 끝에 위치해있기때문에 리드문을 두번써도 한번만 출력됨

# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기

print()

# 한줄한줄 읽어오게하기
with open('/Volumes/128No1/study/fastcamp/resource/review.txt', 'r') as f:
    line = f.readline() #한줄씩 호출
    while line: # 전체 다 읽어 오는 방법 / 한줄씩 라인별 호출해서 반복
        print(line, end='****')
        line = f.readline()

# readlines : 전체 읽은 후 라인 단위 리스트 저장

print()
print()

with open('/Volumes/128No1/study/fastcamp/resource/review.txt', 'r') as f:
    contents = f.readlines() # 마지막 이스케이프 문자를 포함해서 리스트형태로 저장
    print(contents)
    print()
    for c in contents:
        print(c, end='****')

print()
print()

# 예제7
with open('/Volumes/128No1/study/fastcamp/resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line)) # 텍스트 파일에 저장된건 무조건 srt로 인식됨으로 필요에 따라 int 등의 형변환이 필요함
    print(score)
    print('Average : {:6.3f}'.format(sum(score) / len(score)))

# 파일 쓰기

with open('/Volumes/128No1/study/fastcamp/resource/test.txt', 'w') as f:
    f.write('niceman!\n')

with open('/Volumes/128No1/study/fastcamp/resource/test2.txt', 'a') as f:
    f.write('niceman!!\n')

from random import randint

with open('/Volumes/128No1/study/fastcamp/resource/score2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 46)))
        f.write('\n') #랜덤 구문 확인하여 로또 번호 뽑아서 텍스트 파일에 기재하기


# writelines : 리스트 -> 파일로 저장
with open('/Volumes/128No1/study/fastcamp/resource/test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5
with open('/Volumes/128No1/study/fastcamp/resource/test3.txt', 'w') as f:
    print('Test Contents!', file=f) # 프린트문을 활용한 파일 기재
    print('Test Contents!!', file=f)
