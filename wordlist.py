import time
import random
import string

class WordlistGenerator():
    def __init__(self):
        print "[*] WORDLIST GENERATOR"
        print "[*]Started on", time.ctime()
        self.genarate()
        print "[*]Finished..."
        print "[*]Completed at", time.ctime()
        
    def genarate(self):
        words=raw_input("Number of words:\t")
        min_len=raw_input("Minimum word length:\t")
        max_len=raw_input("Maximum word length:\t")
        options=raw_input('''
        SELECT YOUR COMBINATION
            1. Letters only
            2. Digits only
            3. Letters and digits
            4. Uppercase letters only
            5. Lowercase letters only
            6. Uppercase letters + digits
            7. Lowercase letters + digits
            8. Uppercase letters + punctuation
            9. Lowercase letters + punctuation
            10. Uppercase letters + digits + punctuation
            11. Lowercase letters + digits + punctuation
        ''')
        default_option=string.letters+string.digits
        if options=="":
            chars=default_option
        elif int(options)==1:
            chars=string.letters
        elif int(options)==2:
            chars=string.digits
        elif int(options)==3:
            chars=string.letters+string.digits
        elif int(options)==4:
            chars=string.ascii_uppercase
        elif int(options)==5:
            chars=string.ascii_lowercase
        elif int(options)==6:
            chars=string.ascii_uppercase+string.digits
        elif int(options)==7:
            chars=string.ascii_lowercase+string.digits
        elif int(options)==8:
            chars=string.ascii_uppercase+string.punctuation
        elif int(options)==9:
            chars=string.ascii_lowercase+string.punctuation
        elif int(options)==10:
            chars=string.ascii_uppercase+string.digits+string.punctuation
        elif int(options)==11:
            chars=string.ascii_lowercase+string.digits+string.punctuation
        else:
            chars=default_option
            
        word=""   
        if words.isdigit() and min_len.isdigit() and max_len.isdigit():
            try:
                wl=open("wordlist.txt","w")
                for i in xrange(int(words)):
                    for j in random.sample(chars, random.randint(int(min_len), int(max_len))):
                        word+=j
                    wl.write(word+"\n")    
                    print word
                    word=""
                wl.close()
            except Exception as err:
                print "Error:" ,str(err)
        else:
            print "[*] Wrong entries/ Empty fields. Please check your entries and try again."
        
def main():
    WordlistGenerator()
    
if __name__=="__main__":
    main()