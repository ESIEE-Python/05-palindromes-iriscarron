'''
blabla
'''
import string
def ispalindrome(p):
    '''
    blabl
    '''
    accents = str.maketrans("áàâäéèêëíìîïóòôöúùûüç", "aaaaeeeeiiiioooouuuuc")
    table = str.maketrans('', '', string.punctuation + ' ')
    p = p.lower()
    p = p.translate(accents)
    p = p.translate(table)
    if p==p[::-1]:
        return True
    return False

def main():
    '''
    blabla
    '''
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
