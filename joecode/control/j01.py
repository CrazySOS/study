money = True
if money:
    print('택시를 타고 가라')
else:
    print('걸어가라')

money = False
if money:
    print('택시를 타고 가라')
else:
    print('걸어가라')
    
x = 3
y = 2

if x > y:
    print('I luv you')
else:
    print('I hate you')

if x < y:
    print('I luv you')
else:
    print('I hate you')

if x == y:
    print('I luv you')
else:
    print('I hate you')

if x != y:
    print('I luv you')
else:
    print('I hate you')

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money = 5000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")



btc = 60000
eth = 2000

if btc >= 70000 or eth >= 3000:
    print("비트코인을 사라")
else:
    print("매수를 멈추고 대기해라")

if btc >= 60000 or eth >= 3000:
    print("비트코인을 사라")
else:
    print("매수를 멈추고 대기해라")


if btc >= 60000 and eth >= 2000:
    print("비트코인을 사라")
else:
    print("매수를 멈추고 대기해라")

if btc >= 60000 and eth >= 3000:
    print("비트코인을 사라")
else:
    print("매수를 멈추고 대기해라")


if not btc <= 30000:
    print("비트코인을 사라")
else:
    print("매수를 멈추고 대기해라")

if not btc >= 30000:
    print("비트코인을 사라")
else:
    print("매수를 멈추고 대기해라")

if btc in [40000, 50000, 60000]:
    print("비트코인을 사라")
else:
    print("매수를 멈추고 대기해라")

if btc not in [40000, 50000, 60000]:
    print("비트코인을 사라")
else:
    print("매수를 멈추고 대기해라")

pocket = ["paper", "money", "cellphone"]
if "money" in pocket:
    pass
else:
    print("카드를 꺼내라")

card = False
if "Tmoney" in pocket:
    print("버스를 타고 가라")
elif "card" in pocket:
    print("카드를 꺼내라")
elif "paper" in pocket:
    print("수표에 서명해라")
else:
    print("걸어가라")
    
    
score = 70

if score >= 60:
    message = "success"
else:
    message = "failure" 
print(message)

message = "success" if score >= 60 else "failure"
print(message)

















