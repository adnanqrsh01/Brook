from telethon import events
import telethon
from telethon.tl.custom import Button
from .. import bot
from .. import openai_key
import asyncio
import openai

openai.api_key = "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"
openai.api_key = openai_key
model_engine = "get-3.5-turbo"

k_board = [[Button.inline("stop and reset", b"stopgpt")]]


@bot.on(events.NewMessage(incoming=True, pattern=r"(?i)/ask"))
async def _gpt(event):
    sender_id = event.sender_id
    gpt_message = "hello i am your problem solver"
    try:
        await bot.send_message(sender_id, gpt_message)
        async with bot.conversation(await event.get_chat(), exclusive=True, timeout=600) as conv:
            history = []

            while True:
                gpt_message = "send your query"
                u_input = await send_receive(gpt_message, conv, k_board)
                if u_input is None:
                    gpt_message = "conversation reset. Type /ask to start a new one"
                    await bot.send_message(sender_id, gpt_message)
                    break
                else:
                    gpt_message = "I got your question. Wait for the response"
                    ab = await bot.send_message(sender_id, gpt_message)
                    history.append({"role": "user", "content": u_input})
                    c_comp = await openai.ChatCompletion.create(  # Use `await` for asynchronous call
                        model=model_engine,
                        messages=history,
                        max_tokens=100,
                        n=1,
                        temperature=0.1
                    )
                    response = c_comp.choices[0].message.content
                    history.append({"role": "assistant", "content": response})
                    await ab.delete()
                    await bot.send_message(sender_id, response, parse_mode="Markdown")
    except asyncio.TimeoutError:
        await bot.send_message(sender_id, "Conversation ended due to no response")
        return
    except telethon.errors.AlreadyInConversationError:
        pass
    except Exception as e:
        print(e)
        await bot.send_message(sender_id, "Conversation ended. Something went wrong.")
        return


async def send_receive(gpt_message, conv, keyboard):
    message = await conv.send_message(gpt_message, buttons=keyboard)
    done, _ = await asyncio.wait(
        {
            await conv.wait_event(events.CallbackQuery),
            await conv.get_response(),
        },
        return_when=asyncio.FIRST_COMPLETED,
    )
    result = done.pop().result()
    await message.delete()

    if isinstance(result, events.CallbackQuery):
        return None
    else:
        return result.message.strip()