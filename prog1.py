#Write a program to count the numberof vowels and consonants present in an input string.

def  checkvowel(s):
    vcount=0#count for vowel
    ccount=0#count for consonant
    ncount=0#count for number(single digit)
    scount=0#count for symbol
    vowel=['a','e','i','o','u']

    for a in s:
        c=str(a)
        if(c.isalpha()):  
            if(c.isdigit()):#check if character is digit
                ncount+=1
            elif a in vowel:#check if the character is a vowel
                vcount+=1
            else:#check if character is consonant
                ccount+=1
        else:#character is symbol
            scount+=1

    return vcount, ccount, ncount, scount


if __name__=="__main__":
    s= input("enter string\n")
    v,c,n,sy= checkvowel(s.lower())
    print("\n\n\nThe Sentence is ",s)
    print("Number of vowels: ",v)
    print("Number of consonants: ",c)
    print("Number of digits: ",n)
    print("Number of symbols: ",sy)

