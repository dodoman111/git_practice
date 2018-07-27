import pymysql.cursors

connection = pymysql.connect(
    host = '###########',
    user = '###########',
    password = '##########',
    db = '########',
    port = 3306,
    charset = 'utf8',
    autocommit =True,
    cursorclass = pymysql.cursors.DictCursor)
    
test = 1 #에러발생시 입력 멈추게 하기 위한 변수 설정

##############################함수###############################

def f1():
    with connection.cursor() as cursor:
        sql = "select * from buildings"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("-"*80)
        print("id".ljust(7),end="")
        print("name".ljust(20),end="")
        print("location".ljust(20),end="")
        print("capacity".ljust(15),end="")
        print("assigned".ljust(10))
        print("-"*80)
        for i in result:
            print(str(i["id"]).ljust(7),end="")
            print(i["name"].ljust(20),end="")
            print(i["location"].ljust(20),end="")
            print(str(i["capacity"]).ljust(15),end="")
            print(str(i["assigned"]).ljust(10))
        print("-"*80)
        
def f2():
    with connection.cursor() as cursor:
        sql = "select * from performances"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("-"*80)
        print("id".ljust(7),end="")
        print("name".ljust(20),end="")
        print("type".ljust(20),end="")
        print("price".ljust(15),end="")
        print("booked".ljust(10))
        print("-"*80)
        for i in result:
            print(str(i["id"]).ljust(7),end="")
            print(str(i["name"]).ljust(20),end="")
            print(str(i["type"]).ljust(20),end="")
            print(str(i["price"]).ljust(15),end="")
            print(str(i["booked"]).ljust(10))
        print("-"*80)
            
def f3():
    with connection.cursor() as cursor:
        sql = "select * from audiences"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("-"*80)
        print("id".ljust(11),end="")
        print("name".ljust(34),end="")
        print("gender".ljust(25),end="")
        print("age".ljust(10))
        print("-"*80)
        for i in result:
            print(str(i["id"]).ljust(11),end="")
            print(str(i["name"]).ljust(34),end="")
            print(str(i["gender"]).ljust(25),end="")
            print(str(i["age"]).ljust(10))
        print("-"*80)

def f4():
    global test
    b = str(input('Building name:'))
    c = str(input('Biulding location:'))
    d = eval(input('Building capacity:'))
    if len(b)>200:
        b = b[:200]
    if len(c)>200:
        c = c[:200]
    with connection.cursor() as cursor:
        sql = "insert into buildings(name,location,capacity) values(%s,%s,%s)" 
        cursor.execute(sql,(b,c,d))
        result = cursor.fetchall()
        print('A building is successfully inserted')

def f5():
    global test
    with connection.cursor() as cursor:
        b = str(input('which Buildings do you want to delete? write a Building ID:'))
        sql = "select id from buildings where id = %s "
        cursor.execute(sql,b)
        resulta = cursor.fetchall()
        if resulta == ():
            test = 0
            print('Error 입니다','\n해당 공연장은 없습니다')
        else:
            sql = "delete from buildings where id = %s " #공연장정보 삭제
            cursor.execute(sql,b)
            sql = "delete from assigned where b_id = %s  " #공연장 배정 정보 삭제
            cursor.execute(sql,b)
            result = cursor.fetchall()
        
def f6():        
    b = str(input('Performance name:'))
    c = str(input('Performance type:'))
    d = eval(input('Performance price:'))
    with connection.cursor() as cursor:
        if len(b)<200 and len(c)<200 :
            sql = "insert into performances(name,type,price) values(%s,%s,%s)" 
            cursor.execute(sql,(b,c,d))
            result = cursor.fetchall()
        else :
            if len(b) > 200:
                b = b[0:200]
            if len(c) > 200:
                c = c[0:200]
            sql = "insert into performances(name,type,price) values(%s,%s,%s)" 
            cursor.execute(sql,(b,c,d))
            result = cursor.fetchall()            
        print('A performances is successfully inserted')

def f7():
    global test
    with connection.cursor() as cursor:
        b = eval(input('which Perfomance do you want to delete? write a Performance ID:'))
        sql = "select id from performances where id = %s "
        cursor.execute(sql,b)
        resulta = cursor.fetchall()
        if resulta == (): 
            test = 0
            print('Error 입니다','\n정보가 없습니다')
        else:
            sql = "delete from performances where id = %s " #공연 삭제
            cursor.execute(sql,b)
            sql = "update booked set a_id = null where p_id = %s " #예매정보 삭제
            cursor.execute(sql,b)
            result = cursor.fetchall()

def f8():
    global test
    b = str(input('Audience name:'))
    c = str(input('Audience gender:'))
    d = eval(input('Audience age:'))
    if len(b)>200:
        b = b[:200]
    if len(c)>200:
        c = c[:200]
    if d > 150:
        test = 1
    with connection.cursor() as cursor:
        sql = "insert into audiences(name,gender,age) values(%s,%s,%s)" 
        cursor.execute(sql,(b,c,d))
        result = cursor.fetchall()
        print('A audiences is successfully inserted')
        
def f9():
    global test
    with connection.cursor() as cursor:
        b = eval(input('which Audiences do you want to delete? write an Aduience ID:'))
        sql = "select id from audiences where id = %s "
        cursor.execute(sql,b)
        resulta = cursor.fetchall()
        if resulta == (): 
            test = 0
            print('Error 입니다','\n해당관객이 없습니다.')
        else:
            sql = "delete from audiences where id = %s " #고객정보 삭제
            cursor.execute(sql,b)
            sql = "update booked set a_id = null where a_id = %s " #예매정보 삭제
            cursor.execute(sql,b)
            result = cursor.fetchall()
            
def f10():    
    global test
    b = eval(input('Building ID:'))
    c = eval(input('Performance ID:'))
    with connection.cursor() as cursor:
        sql = "select assigned from assigned where p_id = %s"
        cursor.execute(sql,c)
        result_a = cursor.fetchall()
        if result_a !=():
            if result_a[0]['assigned'] == 1 :           #해당공연이 이미 다른 공연장에 배정되었다면
                test = 0
                print('Error입니다','\n해당 공연은 이미 다른 곳에 배정되었습니다.')
        else:
            sql = "insert into assigned(b_id,p_id,assigned) values(%s,%s,1)" 
            cursor.execute(sql,(b,c))
            cursor.fetchall()
            sql = "update buildings set assigned = 1 where id = %s" 
            cursor.execute(sql,b)
            result = cursor.fetchall()
            #공연이 공연장에 배정되는 순간 -> booked table에 공연과 좌석정보 insert -> 공연장 용량만큼
            sql = "select capacity from buildings where id =%s"
            cursor.execute(sql,b)
            capacity_val = cursor.fetchall()
            for i in range(1,int(capacity_val[0]['capacity'])+1):
                sql = "insert into booked(p_id,seat_number) values(%s,%s)"
                cursor.execute(sql,(c,i))
            cursor.fetchall()
            print('Succesfully assigned a performances')

def f11():        
    global test
    b = eval(input('Performance ID:'))
    c = eval(input('Audience ID:'))
    d = str(input('Seat number:'))
    seatnumbers = d.split(',')
    count = 0
    valid = 0
    a =[]
    c22=[]
    with connection.cursor() as cursor:
        sql = "select distinct id from performances"
        cursor.execute(sql)
        result_f13 = cursor.fetchall()
        for i in result_f13:
            a.append(i['id'])
        sql = "select distinct p_id from assigned where assigned = 1"
        cursor.execute(sql)
        result_f12 = cursor.fetchall()
        for i in result_f12:
            c22.append(i['p_id'])
        if b not in a or b not in c22:
            test = 0
            print('Error입니다','\n해당 공연이 없거나 공연이 공연장에 배정되지 않았습니다.')
        else:
            sql = "select distinct seat_number from booked where p_id =%s and a_id is not null"
            cursor.execute(sql,(b))
            isemptyseat = cursor.fetchall()
            a =[]
            for i in isemptyseat:
                a.append(i['seat_number'])
            isemptyseat_t = a                                           # 이미 예약되어있는 좌석 번호 리스트
            seatnumbers_s = list(map(lambda x : eval(x),seatnumbers))   #예매하려는 좌석 번호 리스트
            sql = "select capacity from buildings where id in (select b_id from assigned where p_id = %s and assigned = 1)"
            cursor.execute(sql,(b))
            condition = cursor.fetchall()
            if isemptyseat_t !=[]:
                for i in isemptyseat_t:#매진된 좌석 번호 
                    if i not in seatnumbers_s and  max(seatnumbers_s) <= condition[0]['capacity']:  #예약할 좌석번호, 예약번호가 용량보다 크진않은지 비교 
                        valid = 1
                    else : 
                        valid = 0
                        break
            else: 
                valid =1
            if valid == 1:
                for i in seatnumbers_s:
                    sql = "update booked set a_id = %s where p_id =%s and seat_number = %s "
                    cursor.execute(sql,(c,b,i))
                    cursor.fetchall()
                    sql = "update performances set booked = booked + 1 where id = %s;"
                    cursor.execute(sql,(b))
                    cursor.fetchall()
                    count += 1
            else : 
                print('The seat is already taken')
            if count >0:
                sql = "select price from performances where id=%s" 
                cursor.execute(sql,(b))
                result = cursor.fetchall()
                resul = count * result[0]['price']
                print('Succesfully booekd a performances')
                print('Total ticket price is %d' %resul)

def f12():        
    global test
    b = eval(input('Building ID:'))
    a = []
    with connection.cursor() as cursor:
        sql = "select id from buildings"
        cursor.execute(sql)
        result_f12 = cursor.fetchall()
        for i in result_f12:
            a.append(i['id'])
        if b not in a :
            test = 0
            print('Error입니다','\n해당 공연장은 없습니다.')
        else:
            sql = "select * from performances where id in (select p_id from assigned where b_id=%s and assigned =1) " 
            cursor.execute(sql,b)
            result = cursor.fetchall()
            print("-"*80)
            print("id".ljust(7),end="")
            print("name".ljust(20),end="")
            print("type".ljust(20),end="")
            print("price".ljust(15),end="")
            print("booked".ljust(10))
            print("-"*80)
            for i in result:
                print(str(i["id"]).ljust(7),end="")
                print(str(i["name"]).ljust(20),end="")
                print(str(i["type"]).ljust(20),end="")
                print(str(i["price"]).ljust(15),end="")
                print(str(i["booked"]).ljust(10))
            print("-"*80)

def f13():     
    global test
    b = eval(input('Performance ID:'))
    a = []
    with connection.cursor() as cursor:
        sql = "select id from performances"
        cursor.execute(sql)
        result_f13 = cursor.fetchall()
        for i in result_f13:
            a.append(i['id'])
        if b not in a:
            test = 0
            print('Error입니다','\n해당 공연은 없습니다.')
        else:   
            sql = "select * from audiences where id in (select distinct a_id from booked where a_id is not null and p_id = %s)" 
            cursor.execute(sql,(b))
            result = cursor.fetchall()
            print("-"*80)
            print("id".ljust(11),end="")
            print("name".ljust(34),end="")
            print("gender".ljust(25),end="")
            print("age".ljust(10))
            print("-"*80)
            for i in result:
                print(str(i["id"]).ljust(11),end="")
                print(str(i["name"]).ljust(34),end="")
                print(str(i["gender"]).ljust(25),end="")
                print(str(i["age"]).ljust(10))
            print("-"*80)

def f14():
    global test
    b = eval(input('Performance ID:'))
    a =[]
    c =[]
    with connection.cursor() as cursor:
        sql = "select id from performances"
        cursor.execute(sql)
        result_f13 = cursor.fetchall()
        for i in result_f13:
            a.append(i['id'])
        sql = "select id from performances where id in (select p_id from assigned where assigned = 1)"
        cursor.execute(sql)
        result_f12 = cursor.fetchall()
        for i in result_f12:
            c.append(i['id'])
        if b not in a or b not in c:
            test = 0
            print('Error입니다','\n해당 공연이 없거나 공연이 공연장에 배정되지 않았습니다.')
        else:
            sql = "select seat_number, a_id from booked where p_id = %s order by seat_number"
            cursor.execute(sql,b)
            result = cursor.fetchall()
            print("-"*80)
            print("seat_number".ljust(40),end="")
            print("audience_id".ljust(10))
            print("-"*80)
            for i in result:
                print(str(i["seat_number"]).ljust(40),end="")
                if i["a_id"] == None:
                       print("".ljust(10))
                else: print(str(i["a_id"]).ljust(10))
            print("-"*80)
            
def f15(): 
    connection.close()
    print('Bye!')
    
 ##########################출력단#########################
print("="*80)
print('1. print all buildings')
print('2. print all performances')
print('3. print all audiences')
print('4. insert a new building')
print('5. remove a building')
print('6. insert a new performance')
print('7. remove a performance')
print('8. insert a new audience')
print('9. remove an audience')
print('10. assign a performance to a building')
print('11. book a performance')
print('12. print all performances assigned to a building')
print('13. print all audiences who booked for a performance')
print('14. print ticket booking status of a performance')
print('15. exit')
print("="*80)
while True:
    a = eval(input('Select your action?:'))
    for i in range(16):
        if a == i:
            eval('f'+str(a)+'()')
    if a >15 or test == 0:
        print('다시 확인바랍니다')
        break
    if a ==15:
        break
