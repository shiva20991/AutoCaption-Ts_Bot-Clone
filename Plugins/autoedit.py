import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import autocaption
from config import Config


# =
usercaption_position = Config.CAPTION_POSITION
caption_position = usercaption_position.lower()
caption_text = Config.CAPTION_TEXT


@autocaption.on_message(filters.channel & (filters.document | filters.video) & ~filters.edited, group=-1)
async def editing(bot, message):
      try:
          file_name = None
          if message.document:
             file_caption = f"**{message.caption}**"
      except:
          pass
      try:
          if caption_position == "top":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = <b>caption_text<\b> + "\n" + file_caption,
                 parse_mode = "markdown"
             )
          elif caption_position == "bottom":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = <b>file_caption<\b> + "\n" + <b>caption_text<\b>,
                 parse_mode = "markdown"
             )
          elif caption_position == "nil":
             await bot.edit_message_caption(
                 chat_id = message.chat.id,
                 message_id = message.message_id,
                 caption = <b>caption_text<\b>, 
                 parse_mode = "markdown"
             ) 
      except:
          pass
              
                   
      
