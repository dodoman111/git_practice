def digit(num,pos):              #n자리수에 위치한 숫자 값 찾기
    return (num//10**(pos-1))%10

def num_in_french(num):
    ones_list = ['zero','un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix','onze','douze','treize','quatorze','quinze','seize','dix-sept','dix-huit','dix-neuf']
    tens_list = ['','dix','vingt','trente','quarante','cinquante','soixante','soixante','quatre-vingt','quatre-vingt']
    if num < 20:
        return ones_list[num]
    if num == 100:
        return 'cent'
    if num >= 70 and num <80:
        a,b = digit(num,2),digit(num,1)
        if b ==1:
            return tens_list[a]+' et '+ones_list[b+10]
        return tens_list[a]+'-'+ones_list[b+10]
    if num >= 80 and num <=99:
        a,b = digit(num,2),(num-80)
        if b == 0:
            return tens_list[a]+'s'
        elif digit(b,1) ==1:
            return tens_list[a]+'-'+ones_list[b]
        return tens_list[a]+'-'+ones_list[b]
    if num >= 20 and num < 70 :
        if digit(num,1) ==0:
            return tens_list[digit(num,2)]
        elif digit(num,1) ==1:
            return tens_list[digit(num,2)] +' et '+ones_list[digit(num,1)]   
        else :
            return tens_list[digit(num,2)] +'-'+ones_list[digit(num,1)]

def print_French(lo,hi):
    for i in range(lo,hi+1):
        print(i,num_in_french(i))
