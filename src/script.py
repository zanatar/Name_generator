import random
##import string


## алфавит с учетом частотности букв
abc = "а"*200+"б"*40+"в"*113+"г"*43+"д"*75+"е"*211+"ё"+"ж"*24+"з"*41+"и"*184+"й"*30+"к"*87+"л"*110+"м"*80+"н"*168+"о"*274+"п"*70+"р"*118+"с"*137+"т"*157+"у"*66+"ф"*7+"х"*24+"ц"*12+"ч"*36+"ш"*18+"щ"*9+"ь"*43+"ы"*47+"ъ"+"э"*8+"ю"*16+"я"*50
##abc_no_double = "а"*200+"б"*40+"в"*113+"г"*43+"д"*75+"е"*211+"з"*41+"и"*184+"й"*30+"к"*87+"л"*110+"м"*80+"н"*168+"о"*274+"п"*70+"р"*118+"с"*137+"т"*157+"у"*66+"ф"*7

## гласные и согласные
consonant = "б"*40+"в"*113+"г"*43+"д"*75+"ж"*24+"з"*41+"й"*30+"к"*87+"л"*110+"м"*80+"н"*168+"п"*70+"р"*118+"с"*137+"т"*157+"ф"*7+"х"*24+"ц"*12+"ч"*36+"ш"*18+"щ"*9+"ь"*43+"ъ"
consonant_filter_1 = "б"*40+"в"*113+"г"*43+"д"*75+"ж"*24+"з"*41+"й"*30+"к"*87+"л"*110+"м"*80+"н"*168+"п"*70+"р"*118+"с"*137+"т"*157+"ф"*7+"х"*24+"ц"*12+"ч"*36+"ш"*18+"щ"*9+"ь"*43+"ъ"


vowel = "а"*200+"е"*211+"ё"+"и"*184+"о"*274+"у"*66+"ы"*47+"э"*8+"ю"*16+"я"*50
No_more_1_list = ["ё", "й", "ц", "щ", "ъ", "ы", "я", "ь", "ю", "э"]
name = ""
surname = ""
hard_list = []
random_list = []
no_double_list = ["ы", "ъ", "ь", "щ", "ш", "ц", "ч", "й", "ё", "ж", "я", "ю", "х"]
filter_2_list = ["ы", "ъ", "ь", "щ", "ш", "ц", "й", "ё", "ж", "я", "ю", "х"]
filter_3_list = ["ы", "ъ", "ь", "щ", "ш", "ц", "ч", "й", "ё", "ж", "ю", "х", "я"]
no_bad_start_list = ["ы", "ь","ъ"]
cursed_syllabs = ["бля", "хуй", "жоп", "мля"]
fail_counter = 0
countdown = 0




## Фильтры:

## 1) Ь ъ после гласной или согласной из шаблона ## 4) Ь, Ъ между двумя гласными
def Filter_1(word):
    global countdown## иногда попадаются ошибки
    if word[len(word)-1] == "ь" or word[len(word)-1] == "ъ":
        if word[len(word)-2] in vowel or word[len(word)-2] in no_double_list:
            for x in reversed(range(len(word)-2,len(word))):
                if x not in hard_list:
                    word = Letter_change(word, word[x], x)
                    break
    return word
## 2) Ь после Й, Ц, Ш, Щ, Ъ, Ж, Ё

def Filter_2(word):
    global countdown
    if word[len(word)-1] == "ь" and word[len(word)-2] in filter_2_list:
        for x in reversed(range(len(word)-2,len(word))):
                if x not in hard_list:
                    word = Letter_change(word, word[x], x)
                    break
    
    return word
        
        

## 3) Начинается на Ы, Ъ, Ь

def No_bad_start(word): ## работает
    global countdown
    if word[0] in no_bad_start_list:
        if  word[0] in vowel:
            vowel_no_more = vowel.replace(word[0], "о")
            word = random.choice(vowel_no_more)
        else:
            consonant_no_more = consonant.replace(word[0], "н")
            word = random.choice(consonant_no_more)
    
    return word
        

## 5) Ы после Щ, Ш, Ж, Ц, Й, Е, Ъ, Ы, Э, Я, Ч, Ё, ь

def Filter_4(word):
    global countdown
    if word[len(word)-1] == "ы" and word[len(word)-2] in no_double_list:
        for x in reversed(range(len(word)-2,len(word))):
            if x not in hard_list:
                word = Letter_change(word, word[x], x)
                break
    
    return word

## 6) Удвоенные ы, ъ, ь, щ, ш, ц, ч, й, ё, ж, я, э, ю, х
def No_double(word):  
    global countdown
    if word[len(word)-1] in no_double_list and word[len(word)-2] in no_double_list  :
        if len(word) in hard_list and len(word)-1 not in hard_list:
            abc_no_double = abc.replace(word[len(word)-1], "н")
            word = word[:len(word)-2] + random.choice(abc_no_double)+ word[len(word)-1]
            return word
        elif len(word) not in hard_list:
            abc_no_double = abc.replace(word[len(word)-1], "н")
            word = word[:len(word)-1] + random.choice(abc_no_double)
            return word
        else:
            return word
    
    return word



## 7) Заканчивается на Ъ, Ё

def No_bad_end(word): ##Проверка встроенна в генератор, не в чек
    global countdown
    if word[len(word)-1] == "ъ" or word[len(word)-1] == "Ё":
        if len(word)-1 not in hard_list:
            word =  Letter_change(word, word[len(word)-1], len(word)-1)
    
    return word
    
## 8) Я после Ц, Ш, Щ, Ъ, Ы, Ж, Ч, Ь, Ю

def Filter_3(word):
    global countdown
    if word[len(word)-1] == "я" and word[len(word)-2] in filter_3_list:
        for x in reversed(range(len(word)-2,len(word))):
                if x not in hard_list:
                    word = Letter_change(word, word[x], x)
                    break
    
    return word

## 9) Больше одной гласной после Я, Ы, Ю
## 10) Матные сочетания БЛЯ, ХУЙ, ЖОП, МЛЯ,

def No_cursed_syllabs(word):
    global countdown
    if len(word) >= 3:
        check = word[len(word)-3]+word[len(word)-2]+word[len(word)-1]
        if check in cursed_syllabs:
            for x in reversed(range(len(word)-3,len(word))):
                    if x not in hard_list:
                        word = Letter_change(word, word[x], x)
                        break
    
    return word

## 11) Любая утроенная буква 

def No_triple(word):
    global countdown
    if len(word) >= 3:
        if word[len(word)-1] ==  word[len(word)-2]  and word[len(word)-2] == word[len(word)-3]:
            for x in reversed(range(len(word)-3,len(word))):
                if x not in hard_list:
                    word = Letter_change(word, word[x], x)
                    break
    
    return word
                    
                              



##def No_triple(word): ##вариант 3 букв в слове. не то.
##    counter = 1
##    for x in reversed(range(len(word)-2)):
##        if  word[x] == word[len(word)-1]:
##            counter +=1
##        if counter == 3:
##            if len(word) not in hard_list:
##                word = Letter_change(word, word[len(word)-1],len(word)-1)
##            else:
##                for y in reversed(range(len(word)-2)):
##                    if  word[y] == word[len(word)-1]:
##                        if y not in hard_list:
##                            word = Letter_change(word, word[y],y)
##                            break
##    return word ## срань возвращает пришедшее значение. если убрать, не возвращает ничегоS
##            
    
## 12) Больше двух гласных подряд

def Vowel_double(word):
    global countdown
    if len(word) >= 2:
        if word[len(word)-1] in vowel and word[len(word)-2] in vowel and word[len(word)-3] in vowel:
            for x in reversed(range(len(word)+1)):
                if x in random_list :
                    word = word[:x-1]+random.choice(consonant)+word[x:]
                    return word
                    break
        else:
            return word
    
    return word
    
def Consonant_triple(word):
    global countdown
    if len(word) >= 3:
        if word[len(word)-1] in consonant and word[len(word)-2] in consonant and word[len(word)-3] in consonant and word[len(word)-4] in consonant:
            for x in reversed(range(len(word)+1)):
                if x in random_list :
                    word = word[:x-1]+random.choice(vowel)+word[x:]
                    return word
                    break
        else:
            return word
   
    return word



## 13) Больше одной Ё, Й, Ц, Щ, Ъ, Ы, Я, Ь, Ю, э в слове

def No_more_1(word):
    global countdown
    if word[len(word)-1] in No_more_1_list:
        for x in reversed(range(len(word)-1)):
            if word[x] == word[len(word)-1]:
                if  len(word) not in hard_list:
                    word = Letter_change(word, word[len(word)-1],len(word)-1) 
                elif x not in hard_list:
                    word = Letter_change(word, word[x],x)
                    
    
    return word

def Letter_change(word, letter, number):
    if  letter in vowel:
        vowel_no_more = vowel.replace(letter, "о")
        word = word[:number]+random.choice(vowel_no_more)+word[number+1:]
    else:
        consonant_no_more = consonant.replace(letter, "н")
        word = word[:number]+random.choice(consonant_no_more)+word[number+1:]
    return word
##  
##


## Фильтруем результат
## цикл while true с check +=1 на прохождении теста без условий. потом проверка и break
def Check(word):
    global countdown
    while True:
        word = Consonant_triple(word)
        word = Vowel_double(word)
        word = No_double(word)
        word = Filter_1(word)
        word = No_more_1(word)
        word = No_triple(word)
        word = Filter_2(word)
        word = No_bad_start(word)
        word = Filter_3(word)
        word = Filter_4(word)
        word = No_cursed_syllabs(word)
        countdown +=1
##        print(countdown)
##        return word
        if countdown >= 10:
            return word
            break
                    
    
##крутим рандом, отправляем на проверку. 
##введенные буквы оставляем.
def Generator(form, sourse):
    x = 0
    global hard_list
    global random_list
    for letter in form:
        if letter == '*': ##любые буквы
            random_list.append(x)
            sourse += random.choice(abc)
            sourse = Check(sourse)
            x+=1
        elif letter == '1': ##только гласные
            sourse += random.choice(vowel)
            sourse = Check(sourse)
            x+=1
        elif letter == '2': ##только согласные
            sourse += random.choice(consonant)
            sourse = Check(sourse)
            x+=1
        else: ## жестко заданные буквы
            hard_list.append(x)
            sourse += letter
            sourse = Check(sourse)
            x+=1
    hard_list = []
    random_list = []
    sourse = No_bad_end(sourse)
    return sourse


##f = open('text_gen.txt', 'a')

##запрос шаблона имени/фамилии

def main():
    name_form = input('Введите требуемый шаблон для имени. количество необходимых случайных букв укажите звездочками. пропишите нужные буквы в нужных местах. ')

    surname_form = input('Введите требуемый шаблон для имени. количество необходимых случайных букв укажите звездочками. пропишите нужные буквы в нужных местах. если фамилия не требуется - не вводите ничего. ')

    global name
    global surname
    
    while True:
        try:
            attempt = int(input('введите число попыток '))
        except ValueError:
            print('нужно ввести число')
            continue
        else:
            break
    Parser_test(name_form, surname_form, attempt)

def Parser_test(name_form, surname_form, attempt):
    global name
    global surname
    for x in range(attempt):
        name = Generator(name_form, name)
        name = name[0].upper()+name[1:]
        if surname_form != '':
            surname = Generator(surname_form, surname)
            surname = surname[0].upper()+surname[1:]
    ##    t = 'сгенерировано имя: '+name+' '+surname+'\n'
    ##    f.write(t)
        print('сгенерировано имя: ',name , surname)
        name = ""
        surname = ""
        random_list = []
        hard_list = []

def Parser(name_form, surname_form):
    name = ""
    surname = ""
    hard_list = []
    name = Generator(name_form, name)
    name = name[0].upper()+name[1:]
    if surname_form != '':
        surname = Generator(surname_form, surname)
        surname = surname[0].upper()+surname[1:]
    return name, surname


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()


##выводим результат
