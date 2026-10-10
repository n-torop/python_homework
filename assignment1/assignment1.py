# Task 1
def hello():
    return "Hello!"



# Task 2
def greet(name):
    return f"Hello, {name}!"




# Task 3
def calc(num1, num2, action="multiply"):
    try: 
        match action:
            case "add":
                return num1+num2
            case "subtract":
                return num1-num2
            case "multiply":
                return num1*num2
            case "power":
                return num1**num2
            case "modulo"| "divide" | "int_divide":
                try:
                    if action=="modulo":
                        return num1%num2
                    elif action=="divide":
                        return num1/num2
                    
                    elif action=="int_divide":
                        return num1//num2
                except ZeroDivisionError:
                    return "You can't divide by 0!"
    except TypeError:
        return f"You can't {action} those values!"
    



# Task 4
def data_type_conversion(value, name):
    match name:
        case "float" | "int":
            try: 
                if name=="float":
                    return float(value)
                elif name=="int":
                    return int(value)
            except ValueError:
                # return f"You can't convert {value} into {'an' if name=='int' else 'a'} {name}."
                return f"You can't convert {value} into a {name}."
        case "str":
            return str(value)
        

#Task 5
def grade(*args):
    try:
        average=sum(args)/len(args)
        match average:
            case n if n>=90:
                return "A"
            case n if 80<=n<=89:
                return "B"
            case n if 70<=n<=79:
                return "C"
            case n if 60<=n<=69:
                return "D"
            case n if n<=60:
                return "F"
    except TypeError:
        return "Invalid data was provided."


#Task 6
def repeat(string, count):
    try:
        # string=string.strip()
        new_list=[]
        for el in range (count):
            new_list.append(string)
        sentence="".join(new_list)
        return sentence
    except TypeError:
        return "Invalid data was provided."


#Task 7
def student_scores(choice, **kwargs):
    maxx=0
    avg=0
    scores=[]
    for key, value in kwargs.items():
        scores.append(value)
    for key, value in kwargs.items():
        match choice:
            case "best":
                maxx=max(scores) #91 
                if maxx==value:
                    return key
            case "mean":
                avg=sum(scores)/len(scores)
                return avg

#Task 8
def titleize(string):
    non_capitalized={
        "a": True,
        "on": True,
        "an": True,
        "the": True,
        "of": True,
        "and": True,
        "is": True,
        "in": True,
    }
    listt=string.split()
    length=len(listt) #3
    cap_list=[]
    for index, word in enumerate(listt):
        if index==0 or index==length-1:
            cap_list.append(word.capitalize())
        if (index!=0 and index!=length-1) and word in non_capitalized:
            cap_list.append(word)
        elif (index!=0 and index!=length-1) and word not in non_capitalized:
            cap_list.append(word.capitalize())

    result=' '.join(cap_list)
    return result

#Task 9
def hangman(secret, guess):
    secret_letters=list(secret)
    guess_letters=list(guess)
    updated_list=[]
    for letter in secret_letters: 
        if letter not in guess_letters:
            updated_list.append("_")
        elif letter in guess_letters:
            updated_list.append(letter)            
    result="".join(updated_list)
    return result


#Task 10
import re

def pig_latin(string):
    vowels="aeiou"
    # vowels=['a', 'e', 'i', 'o', 'u']

    result=[]

    for word in string.split():
        print (word)
        letters=re.findall(r"qu|.", word)
        
        index=0
    
        while index<len(letters) and letters[index] not in vowels:
            index+=1

        reordered=letters[index:]+letters[:index]
        result.append("".join(reordered)+"ay")

    return " ".join(result)











# print(hello())
# print(greet("James"))
# print (calc(6, 2, "power"))

# print (data_type_conversion("aj", "float"))
# print(grade(150, 50, 50))
# print(repeat("new", 6))
# print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50))
# print(titleize("a and peace"))
# print(hangman("difficulty", "ic"))

# print( pig_latin("apple"))
# print( pig_latin("banana"))
# print(pig_latin("cherry"))
# print( pig_latin("quiet"))
# print(pig_latin("square"))
# print(pig_latin("the quick brown fox"))