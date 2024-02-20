from interpreter import interpreter

interpreter.llm.model = "together_ai/mistralai/Mixtral-8x7B-Instruct-v0.1"
interpreter.auto_run = True
interpreter.chat("using this linux cli tool subfinder which is installed on the system , perform recon on hackerone.com and save the output in a file called subs.txt ")

