Skip to content
jordngill
/
rename-bot-new

Type / to search

Code
Issues
Pull requests
Actions
Projects
Security
Insights
Files
Go to file
helpo
plugins
F_Sub.py
broadcast.py
caption.py
cb_data.py
filedetect.py
rename.py
start.py
thumbfuc.py
Dockerfile
LICENSE
Procfile
README.md
app.json
bot.py
config.py
koyeb.yml
render.yaml
requirements.txt
route.py
Creating a new file in rename-bot-new
Breadcrumbsrename-bot-new/plugins
/
rename.py
in
main

Edit

Preview
Indent mode

Spaces
Indent size

2
Line wrap mode

No wrap
Editing rename.py file contents
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
from asyncio import sleep
    global St_Session
    if message.from_user.id in St_Session:
        try:
            String_Session = St_Session[message.from_user.id]
            ubot = Client("Urenamer", session_string=String_Session, api_id=API_ID, api_hash=API_HASH)
            print("Ubot Connected")
        except Exception as e:
            print(e)
            return await message.reply("String Session Not Connected!! ,Use /connect")
    else:
        return await message.reply("String Session Not Connected!! ,Use /connect")
    await ubot.start()
    chat_id = await client.ask(text ="Send Channel Id From Where You Want To Forward in `-100XXXX` Format ",chat_id = message.chat.id)
    chat_id = chat_id.text
    chat_id = int(chat_id)
    Forward  = await client.ask(text ="Send Channel Id In Which You Want Renamed Files To Be Sent in `-100XXXX` Format ",chat_id = message.chat.id)
    Forward = Forward.text
    Forward = int(Forward)
    await savforward(message,Forward)
    
    msg_id = await client.ask(text ="Send Start Message Link ",chat_id = message.chat.id)
    msg_id = msg_id.text
    msg_id = msg_id.split("/")[-1]
    msg_id = int(msg_id)

    for i in range(msg_id,msg_id+5):
        messages = await ubot.get_messages(chat_id=chat_id,message_ids=i)
        try:
            await asyncio.sleep(3)
            x = msg_id + 5
            y = msg_id +6
            while True:  
                # print("Stuck In Loop")
                await asyncio.sleep(5)
                try:
                    handler = get_manager()
                    value = handler[message.from_user.id]
                except Exception as e:
                    # print(e)
                    pass
                if i == msg_id:
                    value = True
                if value == True:
                    break 
                
            await messages.copy(Bot_Username)
        except Exception as e:
            print(e)
            pass
        try:
            await client.delete_messages(chat_id = chat_id, message_ids=i)
        except Exception as e:
            print(e)
            pass
        manager(message.from_user.id,False)
    await ubot.stop()

#Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
#New File at plugins · jordngill/rename-bot-new 
