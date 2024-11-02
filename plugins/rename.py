from asyncio import sleep
from pyrogram import Client

# Define the rename handler function
async def rename_handler(message, client):
    global St_Session

    # Check if the user's session is available
    if message.from_user.id in St_Session:
        try:
            String_Session = St_Session[message.from_user.id]
            ubot = Client("Urenamer", session_string=String_Session, api_id=API_ID, api_hash=API_HASH)
            print("Ubot Connected")
        except Exception as e:
            print(e)
            return await message.reply("String Session Not Connected! Use /connect")
    else:
        return await message.reply("String Session Not Connected! Use /connect")

    await ubot.start()

    # Get the source channel ID from the user
    chat_id_response = await client.ask(
        text="Send Channel ID from where you want to forward in `-100XXXX` format",
        chat_id=message.chat.id
    )
    chat_id = int(chat_id_response.text)

    # Get the target channel ID for renamed files
    forward_response = await client.ask(
        text="Send Channel ID in which you want renamed files to be sent in `-100XXXX` format",
        chat_id=message.chat.id
    )
    forward_channel = int(forward_response.text)

    await savforward(message, forward_channel)

    # Get the start message link to begin renaming and forwarding
    msg_id_response = await client.ask(text="Send Start Message Link", chat_id=message.chat.id)
    msg_id = int(msg_id_response.text.split("/")[-1])

    # Loop through messages and rename/forward as needed
    for i in range(msg_id, msg_id + 5):
        try:
            messages = await ubot.get_messages(chat_id=chat_id, message_ids=i)
            await sleep(3)

            # Inner loop to wait for signal to proceed
            while True:
                await sleep(5)
                try:
                    handler = get_manager()
                    value = handler[message.from_user.id]
                except Exception:
                    value = False

                if i == msg_id or value:
                    break

            # Copy the message to the target username
            await messages.copy(Bot_Username)

        except Exception as e:
            print(f"Error copying message {i}: {e}")
            continue

        # Delete the original message after copying
        try:
            await client.delete_messages(chat_id=chat_id, message_ids=i)
        except Exception as e:
            print(f"Error deleting message {i}: {e}")

        # Update the manager status
        manager(message.from_user.id, False)

    await ubot.stop()
