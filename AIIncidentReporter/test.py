import openai

openAI_key = # Feed api key fetched from a new openai account for best reult

def generateTxt(prompt):
    openai.api_key = openAI_key
    response = openai.Completion.create(engine = "text-davinci-003", prompt=prompt, max_tokens = 1000)
    return response.choices[0].text

suspiciousReq = input("[+] Paste your suspected request here: ")
print(generateTxt(suspiciousReq+' Verify the possible attacks for the following requests and register it in following json format {isSusspicious: boolean, Attack name:"", ipAddress: "", UserAgent:"",AttackingTool:"" }, here ipAddress reffers to the ip of attacker from log and userAgent reffers to Browser. Also generate an incident report for the same that includes Title and Heading, Date of incident,Introduction to the event, Description of Incident,Impact on the company, Analysis of Cause, Immidiate Actions taken, Evidence Doccumentation, Mitigation methods and Conclusion.'))
### Heres a test request: 192.168.157.1 - - [26/Sep/2023:10:15:17 -0400] "GET /?id=../../etc/pass HTTP/1.1" 200 3380 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"