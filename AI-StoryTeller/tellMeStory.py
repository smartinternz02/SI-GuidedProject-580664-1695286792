import openai
api_key = #Feed the openai API key reciever from a new accout to avoid any errors 

def storyGenerator(prompt):
    openai.api_key=api_key
    response = openai.Completion.create(engine = "text-davinci-003", prompt=prompt, max_tokens = 500)
    return response.choices[0].text

genere = input(">> Select your genere: ")
promptBuild = "Pretend to be a writer and generate a story of 500 words on "+ genere
print(storyGenerator(promptBuild)+"\n\n")

while(True):
    print("[+] To Generate a new story woth same genere, press 1\n[+] To change genere, press 2\n[+] To Quit, press 0")
    choice = input(">> ")
    if(choice == '1'):
        promptBuild = "Pretend to be a writer and generate a story of 500 words on "+ genere
        print(storyGenerator(promptBuild)+"\n\n")
    elif(choice == '2'):
        genere = input(">> Change genere to: ")
        promptBuild = "Pretend to be a writer and generate a story of 500 words on "+ genere
        print(storyGenerator(promptBuild)+"\n\n")
    elif(choice == '0'):
        print(">> Thank You!!\n")
        print("--------------------Quitting--------------------")
        break
    else:
        print(">> Wrong Input!!\n")

