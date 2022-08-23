import webbrowser

#sample message
messageEnc ='kwwsv=22dpdqxhodzrnh1frp2edkedkedk2'

#ascii caeser cipher scroll
def decrypt(input, scroll):
    
    arr = list(input)
    result = ""

    for i in range(len(arr)):
        result +=chr(ord(arr[i]) - scroll)
    return result

#cipher scroll
messageDec = decrypt(messageEnc, 3)
webbrowser.open(messageDec) 
print("Got dam!")