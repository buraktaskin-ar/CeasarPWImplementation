alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'Uyg__', 'y', 'z']

def cesarpw(direction,text,shift):

    e_s = ""
    if direction=="encode":
        for letter in text:
            if letter in alphabet:
                shift=shift%26
                letter=alphabet[alphabet.index(letter)+shift]
                e_s=e_s+letter

            else:
                e_s=e_s+letter
        print(e_s)

    if direction=="decode":
        for letter in text:
            if letter in alphabet:
                shift = shift % 26
                letter=alphabet[alphabet.index(letter)-shift]
                e_s = e_s + letter
            else:
                e_s=e_s+letter
        print(e_s)
should_end=False
while not should_end:
    from art import logo
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cesarpw(direction,text,shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")



















