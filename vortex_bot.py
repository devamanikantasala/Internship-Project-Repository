from chatterbot import ChatBot;
from chatterbot.trainers import ListTrainer;
from training_data.greetings import msgs;
from training_data.introductions import introduce_yourself as introduce;
from training_data.basic_queries import basic_conversational_queries as basic_queries;
import google.generativeai as ai;

confidence_threshold = 0.5
api = ""    #add your api code here! go to 'aistudio.google.com'

# --- remove the below 10th line to 16th line before executing lines ---
if api == '':
    import colorama
    colorama.init();
    print(f'{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}{'* * * W A R N I N G * * *\n'}{colorama.Style.RESET_ALL}{colorama.Fore.RED}{'Please provide an API Key of Gemini Model, to get your own api key you can headover to-->'}{colorama.Style.RESET_ALL}{colorama.Fore.LIGHTYELLOW_EX}{'\'https://aistudio.google.com\''}{colorama.Style.RESET_ALL}');
    exit();
# --- remove the above lines ---

ai.configure(api_key=api)
model = ai.GenerativeModel('gemini-pro')
gemini = model.start_chat()

myVortex = ChatBot('Vortex-BOT')
trainer = ListTrainer(myVortex)

def train_everything():
    count = 1;
    while count <= 2:
        for training_item in msgs:
            trainer.train(training_item)
        count += 1;
    count = 1;
    while count <= 2:
        for training_item in introduce:
            trainer.train(training_item)
        count += 1;
    count = 1;
    while count <= 2:
        for training_item in basic_queries:
            trainer.train(training_item)
        count += 1;

train_everything();

'''The run_chatbot() function is just an example function to test out the capabilities of our chatbot, here I named my chatbot as \'Vortex\'
The following function further is recommended to only run in terminal mode for learning purposes!'''
# def run_chatbot():
#     exit_conditions = ('exit', ':e', ':q', 'quit', 'EXIT', 'QUIT', '-1')
#     user_input = ''
#     while True:
#         user_input = input('You: ');
#         if user_input in exit_conditions:
#             print('Vortex: Bye! ;)')
#             break;
#         else:
#             response = get_vortex_response(user_input)
#             print(response)

# run_chatbot(); # Function Call

def get_vortex_response(user_input):
    try:
        if user_input.lower() == '':
            response = 'Hi there! Type something so that I can interact with you!'
            return response
        else:
            response = myVortex.get_response(user_input)
            if response.confidence <= confidence_threshold:
                gemini_response = gemini.send_message(user_input)
                print(f"(confi:{response.confidence})Vortex:", gemini_response.text)
                return gemini_response.text
            else:
                print(f"(confi:{response.confidence})Vortex:", response.text)
                return response.text
    except Exception as e:
        return f'**[{e}]**<br>Oops! Some error has been occured due to incorrect input or explicit input given. Could you please try again something different!'