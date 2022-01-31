
letters_dict = {
    "a" : "·-",
    "b" : "-···",
    "c" : "-·-·",
    "d" : "-··",
    "e" : "·",
    "f" : "··-·",
    "g" : "--·",
    "h" : "····",
    "i" : "··",
    "j" : "·---",
    "k" : "-·-",
    "l" : "·-··",
    "m" : "--",
    "n" : "-·",
    "o" : "---",
    "p" : "·--·",
    "q" : "--·-",
    "r" : "·-·",
    "s" : "···",
    "t" : "-",
    "u" : "··-",
    "v" : "...-",
    "w" : "·--",
    "x" : "-··-",
    "y" : "-·--",
    "z" : "--··",
    "0" : "-----",
    "1" : "·----",
    "2" : "··---",
    "3" : "···--",
    "4" : "····-",
    "5" : "·····",
    "6" : "-····",
    "7" : "--···",
    "8" : "---··",
    "9" : "----·",
    "." : "·-·-·-",
    "," : "--··--",
    "?" : "··--··",
    "'" : "·----·",
    "!" : "-·-·--",
    "/" : "-··-·",
    "(" : "-·--·",
    ")" : "-·--·-",
    "&" : "·-···",
    ":" : "---···",
    ";" : "-·-·-·",
    "=" : "-···-",
    "+" : "·-·-·",
    "-" : "-····-",
    "_" : "··--·-",
    '"' : "·-··-·",
    " " : " " 
}

class String_To_Morse:
    def __init__(self,string):
        self.string = string
    
    def translate(self):
        self.string = list(self.string.lower())
        self.string = [letters_dict[letter] for letter in self.string]
        return "".join(self.string)

string = input("Type a string to translate:")        
translation = String_To_Morse(string)
print(translation.translate())
