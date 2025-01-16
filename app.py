from pyrogram import Client, filters ,types
from pyrogram.types import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup 
from apify_client import ApifyClient
from pyromod import listen

dow = ApifyClient("apify_api_4yaUtNE7cjcfsKOh13hZU2Lg2HW8hB2bLIkb")

api_id = 5527711
api_hash = "bfe9610f27c9298bbae60d066d11c5e7"
bot_token = "1670124420:AAHdw3dsLvTK5PBh_-tZ5OfzZLkWe5VeNeU"
app = Client("55", api_id=api_id, api_hash=api_hash,bot_token=bot_token)

async def is_join(chat_id, user_id):
    channel_id = -1001794799134
    user = await app.get_chat_member(chat_id,user_id)
    if user.status == 'left':
        return False
    return True

@app.on_message(filters.command("start"))
async def my_handler(client, message):
    id = message.chat.id
    user_id = message.from_user.id
    try:
        await is_join(chat_id=-1001794799134,user_id=user_id)
    except :
        await app.send_message(
            id,
            text="**شما در کانال عضو نیستید** \n \n --برای دانلود حتما باید عضو کانال باشید--",
            reply_markup = InlineKeyboardMarkup(
                [
                        [InlineKeyboardButton("کانال ما" , url="https://t.me/kosesherpro")],
                        [InlineKeyboardButton("تایید عضویت", url="https://t.me/two1two_bot?start=1234")],
                ]
            )
        )
        return False

    await app.send_message(
    id,text="خدمات بات 👇👇👇",
    reply_markup=ReplyKeyboardMarkup(
        [
            # ["بمبر 😈"],
			# ["ساخت اکانت اسپاتیفای"],
            # ["دانلود ویدیو یوتیوب"],
            ["دانلود پروفایل اینستاگرام"],
        ],
        resize_keyboard=True  # Make the keyboard smaller
        )
    )


@app.on_message(filters.regex('دانلود پروفایل اینستاگرام'))
async def id(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    try:
        await is_join(chat_id=-1001794799134,user_id=user_id)
    except:
        await app.send_message(
            chat_id,
            text="**شما در کانال عضو نیستید** \n \n --برای برای دانلود حتما باید عضو کانال باشید--",
            reply_markup = InlineKeyboardMarkup(
                [
                        [InlineKeyboardButton("کانال ما" , url="https://t.me/kosesherpro")],
                        [InlineKeyboardButton("تایید عضویت", url="https://t.me/two1two_bot?start=1234")],
                ]
            )
        )
        return False
    id = await app.ask(chat_id, "آیدی مورد نظر را وارد کنید ", timeout=30)
    
    try:
        run_input = { "usernames": [f"{id.text}"] }
        run = dow.actor("dSCLg0C3YEZ83HzYX").call(run_input=run_input)
        for item in dow.dataset(run["defaultDatasetId"]).iterate_items():
            # print(item)
            profile = item['profilePicUrlHD']
            fullname = item['fullName']
            biography= item['biography']
            followersCount = item['followersCount']
            await app.send_message(chat_id,
                                   f"""
                                    نام : {fullname}
بیو : {biography}
تعداد فالور : {followersCount}

                                    {profile}
                                    """
                                   
                                
                                   )
    except:
        await app.send_message(chat_id,text="مشکلی وجود دارد")

app.run()
