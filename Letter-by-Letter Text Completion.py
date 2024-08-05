from time import sleep
alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z', ' ']
def spam():
    r = input('Enter Text: ') #Only char.
    a = 0
    m = ''
    while True:
        for i in range(0, len(alphabet)):
            sleep(0.01)
            print(m + alphabet[i])
            if alphabet[i] == r[a]:
                
                m += r[a]
                a += 1
                i = 0
                if r == m:
                    print('başarılı.')
                    return  
spam()
