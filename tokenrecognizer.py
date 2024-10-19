def subject(words):
    ret = False
    state = "q1"

    for char in words:
        if char in ['D', 'd']:
            if state == "q1":
                state = "q2"
                ret = False
            else:
                ret = False
        elif char in ['S', 's']:
            if state == "q1":
                state = "q3"
                ret = False
            else:
                ret = False
        elif char in ['A', 'a']:
            if state == "q1":
                state = "q4"
                ret = False
            elif state == "q5":
                state = "q9"
                ret = False
            elif state == "q3":
                state = "q7"
                ret = False
            elif state == "q6":
                state = "q10"
                ret = True
            elif state == "q11":
                state = "q14"
                ret = True
            else:
                ret = False
        elif char in ['K', 'k']:
            if state == "q1":
                state = "q5"
                ret = False
            elif state == "q4":
                state = "q8"
                ret = False
            else:
                ret = False
        elif char in ['U', 'u']:
            if state == "q8":
                state = "q12"
                ret = True
            elif state == "q13":
                state = "q15"
                ret = True
            else:
                ret = False
        elif char in ['I', 'i']:
            if state == "q2":
                state = "q6"
                ret = False
            elif state == "q13":
                state = "q16"
                ret = True
            else:
                ret = False
        elif char in ['Y', 'y']:
            if state == "q7":
                state = "q11"
                ret = False
            else:
                ret = False
        elif char in ['M', 'm']:
            if state == "q9":
                state = "q13"
                ret = False
            else:
                ret = False
        else:
            ret = False
    return ret


def predikat(wordp):
    retp = False
    state = "q1"

    for char in wordp:
        if char in ['M', 'm']:
            if state == "q1":
                state = "q2"
                retp = False
            elif state == "q13":
                state = "q17"
                retp = True
            elif state == "q5":
                state = "q9"
                retp = False
            else:
                retp = False
        elif char in ['A','a']:
          if state == 'q2':
                state = 'q3'
                retp = False
          elif state == 'q6':
                state = 'q11'
                retp = False
          elif state == 'q9':
                state = 'q14'
                retp = False
          elif state == 'q15':
                state = 'q19'
                retp = False
          elif state == 'q21':
                state = 'q23'
                retp = True
          elif state == 'q18':
                state = 'q20'
                retp = False
          else:
              retp = False
        elif char in ['I', 'i']:
            if state == "q3":
                state = "q7"
                retp = False
            elif state == "q2":
                state = "q4"
                retp = False
            elif state == "q20":
                state = "q22"
                retp = True            
            else:
                retp = False
        elif char in ['B', 'b']:
            if state == "q9":
                state = "q15"
                retp = False
            else:
                retp = False
        elif char in ['C', 'c']:
            if state == "q19":
                state = "q21"
                retp = False
            else:
                retp = False
        elif char in ['K', 'k']:
            if state == "q3":
                state = "q6"
                retp = False
            elif state == "q14":
                state = "q18"
                retp = False
            else:
                retp = False
        elif char in ['N', 'n']:
            if state == "q11":
                state = "q16"
                retp = True
            elif state == "q7":
                state = "q12"
                retp = True
            elif state == "q4":
                state = "q8"
                retp = False
            else:
                retp = False
        elif char in ['U', 'u']:
            if state == "q8":
                state = "q13"
                retp = False
            else:
                retp = False
        elif char in ['E','e']:
            if state == 'q2':
                state = 'q5'
                retp = False
            else:
                retp = False
    return retp


def objek(wordo):
    reto = False
    state = "q1"

    for char in wordo:
        if char in ['A', 'a']:
            if state == "q1":
                state = "q3"
                reto = False
            elif state == "q2":
                state = "q6"
                reto = False
            elif state == "q13":
                state = "q17"
                reto = True
            elif state == "q15":
                state = "q19"
                reto = True
            else:
                reto = False
        elif char in ['B', 'b']:
            if state == "q1":
                state = "q5"
                reto = False
            else:
                reto = False
        elif char in ['E', 'e']:
            if state == "q12":
                state = "q17"
                reto = True
            elif state == 'q4':
                state = 'q8'
                reto = False
            elif state == "q3":
                state = "q8"
                reto = False
            elif state == "q11":
                state = "q16"
                reto = True
            else:
                reto = False
        elif char in ['G', 'g']:
            if state == "q1":
                state = "q2"
                reto = False
            elif state == "q23":
                state = "q25"
                reto = True
            else:
                reto = False
        elif char in ['I','i']:
            if state == 'q11':
                state = 'q16'
                reto = True
            elif state == 'q3':
                state = 'q7'
                reto = False
            else:
              reto = False
        elif char in ['K', 'k']:
            if state == "q9":
                state = "q14"
                reto = False
            else:
                reto = False
        elif char in ['L', 'l']:
            if state == "q10":
                state = "q15"
                reto = False
            else:
                reto = False
        elif char in ['M', 'm']:
            if state == "q7":
                state = "q12"
                reto = False
            else:
                reto = False
        elif char in ['N', 'n']:
            if state == "q8":
                state = "q13"
                reto = False
            elif state == "q21":
                state = "q23"
                reto = False
            elif state == "q24":
                state = "q26"
                reto = True
            elif state == "q1":
                state = "q2"
                reto = True
            else:
                reto = False
        elif char in ['O','o']:
            if state == 'q5':
                state = 'q10'
                reto = False
            else:
                reto = False
        elif char in ['P','p']:
          if state == 'q1':
                state = 'q4'
                reto = False
          else:
                reto = False
        elif char in ['Q', 'q']:
            if state == "q10":
                state = "q15"
                reto = False
            else:
                reto = False
        elif char in ['R', 'r']:
            if state == "q7":
                state = "q12"
                reto = True
            elif state == "q20":
                state = "q22"
                reto = False
            else:
                reto = False
        elif char in ['S', 's']:
            if state == "q1":
                state = "q4"
                reto = False
            elif state == "q9":
                state = "q14"
                reto = False
            elif state == 'q6':
                state = 'q11'
                reto = False
            else:
                reto = False
        elif char in ['U', 'u']:
            if state == "q5":
                state = "q9"
                reto = False
            elif state == "q14":
                state = "q18"
                reto = True
            elif state == "q6":
                state = "q11"
                reto = False
            elif state == "q15":
                state = "q20"
                reto = False
            else:
                reto = False
    return reto



def keterangan(wordk):
    retk = False
    state = "q1"

    for char in wordk:
        if char in ['D', 'd']:
            if state == "q1":
                state = "q2"
                retk = False
            else:
                retk = False
        elif char in ['I', 'i']:
            if state == "q2":
                state = "q3"
                retk = True
            else:
                retk = False
        else:
            retk = False
    return retk


def keteranganfix(wordkf):
    retkf = False
    state = "q1"

    for char in wordkf:
        if char in ['A', 'a']:
            if state == "q11":
                state = "q16"
                retkf = False
            elif state == "q3":
                state = "q7"
                retkf = False
            elif state == "q12":
                state = "q17"
                retkf = False
            elif state == "q4":
                state = "q8"
                retkf = False
            elif state == "q5":
                state = "q9"
                retkf = False
            elif state == "q14":
                state = "q19"
                retkf = False
            elif state == "q15":
                state = "q20"
                retkf = False
            else:
                retkf = False
        elif char in ['D', 'd']:
            if state == "q1":
                state = "q4"
                retkf = False
            else:
                retkf = False
        elif char in ['E', 'e']:
            if state == "q5":
                state = "q10"
                retkf = False
            else:
                retkf = False
        elif char in ['H', 'h']:
            if state == "q16":
                state = "q21"
                retkf = True
            else:
                retkf = False
        elif char in ['K', 'k']:
            if state == "q1":
                state = "q5"
                retkf = False
            else:
                retkf = False
        elif char in ['L', 'l']:
            if state == "q10":
                state = "q15"
                retkf = False
            else:
                retkf = False
        elif char in ['M', 'm']:
            if state == "q6":
                state = "q11"
                retkf = False
            elif state == "q7":
                state = "q12"
                retkf = False
            elif state == "q9":
                state = "q14"
                retkf = False
            else:
                retkf = False
        elif char in ['N', 'n']:
            if state == "q17":
                state = "q22"
                retkf = True
            else:
                retkf = False
        elif char in ['P', 'p']:
            if state == "q8":
                state = "q13"
                retkf = False
            else:
                retkf = False
        elif char in ['R', 'r']:
            if state == "q1":
                state = "q2"
                retkf = False
            elif state == "q19":
                state = "q23"
                retkf = True
            elif state == "q18":
                state = "q22"
                retkf = True
            elif state == "q17":
                state = "q22"
                retkf = True
            else:
                retkf = False
        elif char in ['S', 's']:
            if state == "q20":
                state = "q24"
                retkf = True
            else:
                retkf = False
        elif char in ['T', 't']:
            if state == "q1":
                state = "q3"
                retkf = False
            else:
                retkf = False
        elif char in ['U', 'u']:
            if state == "q2":
                state = "q6"
                retkf = False
            elif state == "q13":
                state = "q18"
                retkf = False
            else:
                retkf = False
        else:
            retkf = False
    return retkf


def main():
    sentence = input("Masukkan kata: ")
    words = sentence.split()

    mystack = []
    output = ""

    mystack.append("#")
    states = "q1"

    # parser
    for word in words:
        if subject(word):
            output += "S"
            if word != words[-1]:
                output += " - "
            if states == "q1":
                mystack.append("s")
                states = "q2"
        elif predikat(word):
            output += "P"
            if word != words[-1]:
                output += " - "
            if states == "q2":
                if mystack[-1] == "s":
                    mystack.pop()
                mystack.append("p")
                states = "q3"
                if word == words[-1]:
                    if mystack[-1] == "p":
                        mystack.pop()
                        states = "q6"
        elif objek(word):
            output += "O"
            if word != words[-1]:
                output += " - "
            if states == "q3":
                if mystack[-1] == "p":
                    mystack.pop()
                mystack.append("o")
                states = "q5"
                if word == words[-1]:
                    if mystack[-1] == "o":
                        mystack.pop()
                        states = "q8"
        elif keterangan(word):
            if states == "q3":
                if mystack[-1] == "p":
                    mystack.pop()
            elif states == "q5":
                if mystack[-1] == "o":
                    mystack.pop()
            mystack.append("b")
        elif keteranganfix(word):
            output += "K"
            if word != words[-1]:
                output += " - "
            if states == "q3" or states == "q5":
                if mystack[-1] == "b":
                    mystack.pop()
                mystack.append("k")
                states = "q7"
                if word == words[-1]:
                    if mystack[-1] == "k":
                        mystack.pop()
                        states = "q10"
        else:
            output += "Unknown"
            if word != words[-1]:
                output += " - "
            mystack.append("e")

    if states in ["q10", "q8", "q6"]:
        if mystack[-1] == "#":
            mystack.pop()

    if not mystack:
        print("VALID")
    else:
        print("NOT VALID")

    print(output)


if __name__ == "__main__":
    main()