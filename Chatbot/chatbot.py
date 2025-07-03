from flask import Flask, render_template, request

app = Flask(__name__)

# Store chat history in a list
chat_history = []
ticket_details= []
i = 0
j=0
current_position=0 # it is a variable which will we use later
total_no_of_tickets=0

def input_checker(user_message,checker): #for checking alphabet or not enter 1 otherwise 2
        if(user_message.isalpha() and checker=='alpha'):
            return user_message
        elif(user_message.isdigit() and checker=='digit'):
            return user_message
        else:
            return None

def ticket_price_for_age(age):
    if(age<10):
        return 20
    elif(age>=10 and age<=20):
        return 35
    else:
        return 50


@app.route('/', methods=['GET', 'POST'])
def home():
    global chat_history,ticket_details,current_position,total_no_of_tickets,i,j

    if request.method == 'POST':
        user_message = request.form.get('user_message')
        if user_message:
            # Add user's message to chat history
            chat_history.append({'sender': 'user', 'message': user_message})
            
            if i==0 :
                bot_response = "number of tickets you want ?"
                chat_history.append({'sender': 'bot', 'message': bot_response})
                i=1
                j=1

            elif (i==1 or j==1):
                if input_checker(user_message,'digit'):
                    if(j==1):
                      total_no_of_tickets=int(user_message)
                      j=2
                    ticket_details.append({'name':None ,'age':int(user_message),'price':ticket_price_for_age(int(user_message))})
                    bot_response=f"enter name for ticket {current_position + 1}"
                    chat_history.append({'sender': 'bot', 'message': bot_response})
                    i=2
                else:
                    chat_history.append({'sender': 'bot', 'message': "invalid input please enter a number"})
                    
            
            elif i==2:
                if input_checker(user_message,'alpha'):
                    ticket_details[current_position-1]['name']=user_message
                    bot_response=f"enter age for ticket {current_position+1}"
                    chat_history.append({'sender': 'bot', 'message': bot_response})
                    current_position+=1
                    if(current_position<total_no_of_tickets):
                        i=1
                    else:
                        i+=1
                else:
                    chat_history.append({'sender': 'bot', 'message': "invalid input please enter a word"})
            else:
                chat_history = []
                ticket_details= []
                i = 0
                j=0
                current_position=0
                total_no_of_tickets=0
                
                
    return render_template('chatbot.html.j2', chat_history=chat_history)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)

