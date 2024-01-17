global temptxt,imagedic,imagepdfdic
imagedic = []
imagepdfdic = []
imagepdfdic1 = []
vidsrt = []
audmergelist = []
temptxt = "res.txt"
from pyrogram import Client, filters 
import os ,re , random ,shutil,asyncio ,pytesseract,requests
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery , ForceReply
import pypdfium2 as pdfium
from yt_dlp import YoutubeDL
from PyPDF2 import PdfWriter, PdfReader
from pypdf import PdfMerger
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet
from pathlib import Path
from urllib.parse import urlparse, unquote
from PIL import Image
ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
bot = Client(
    "audiobot",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6466415254:AAE_m_mYGHFuu3MT4T0qzqVCm0WvR4biYvM"
)
#6032076608:AAGhqffAlibHd7pipzA3HR2-0Ca3sDFlmdI 
#5782497998:AAFdx2dX3yeiyDIcoJwPa_ghY2h_dozEh_E
#6306753444:AAFnoiusUbny-fpy4xxZWYqGNh_c7yOioW8
#6709809460:AAGWWXJBNMF_4ohBNRS22Tg0Q3-vkm376Eo
#6466415254:AAE_m_mYGHFuu3MT4T0qzqVCm0WvR4biYvM
#6812722455:AAEjCb1ZwgBa8DZ4_wVNNjDZbe6EtQZOUxo
def merge_images1(file1, file2):
    
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    (width1, height1) = image1.size
    (width2, height2) = image2.size
    result_width = max(width1 , width2)
    result_height = height1 + height2
    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(0, height1))
    return result
def merge_images2(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    (width1, height1) = image1.size
    (width2, height2) = image2.size
    result_width = width1 + width2
    result_height = max(height1, height2)
    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result


CHOOSE_UR_AUDIO_MODE = "اختر العملية  التي تريد "
CHOOSE_UR_AUDIO_MODE_BUTTONS = [
    
    [InlineKeyboardButton("تضخيم صوتية / فيديو ",callback_data="amplifyaud"),InlineKeyboardButton("قص صوتية / فيديو ",callback_data="trim")],
    [InlineKeyboardButton("تسريع صوتية / فيديو ",callback_data="speedy"),InlineKeyboardButton("تحويل صوتية / فيديو ",callback_data="conv")], 
    [InlineKeyboardButton("تغيير الصوت",callback_data="voicy"), InlineKeyboardButton("ضغط الصوتية ",callback_data="comp")],
    [InlineKeyboardButton("تقسيم الصوتية ",callback_data="splitty"),InlineKeyboardButton("دمج صوتيات ",callback_data="audmerge")],
    [InlineKeyboardButton("تفريغ صوتية",callback_data="transcribe"),InlineKeyboardButton("إزالة الصمت",callback_data="rmvsilence")],
    [InlineKeyboardButton("إبدال صوت الفيديو ",callback_data="subs"),InlineKeyboardButton("كتم صوت الفيديو",callback_data="mute")],
    [InlineKeyboardButton("منتجة فيديو ",callback_data="imagetovid"),InlineKeyboardButton("تغيير أبعاد الفيديو ",callback_data="vidasp")],
    [InlineKeyboardButton("دمج الترجمة مع الفيديو",callback_data="vidsrt")],
    [InlineKeyboardButton("إعادة التسمية ",callback_data="renm"),InlineKeyboardButton("OCR صور",callback_data="OCR")],
    [InlineKeyboardButton("تفريغ pdf",callback_data="pdfOCR"),InlineKeyboardButton("ضغط pdf",callback_data="pdfcompress")],
    [InlineKeyboardButton("دمج pdf",callback_data="pdfmerge"),InlineKeyboardButton("قص pdf ",callback_data="pdftrim")],
    [InlineKeyboardButton("صور إلى pdf",callback_data="imagetopdf"),InlineKeyboardButton("أزلة أسطر txt",callback_data="rmvlines")],
    [InlineKeyboardButton("titled",callback_data="titled"),InlineKeyboardButton("ترقيع الصور",callback_data="imagestitch")],
    [InlineKeyboardButton("صورة إلى gif",callback_data="imagetogif"),InlineKeyboardButton("الرفع لأرشيف",callback_data="upldarch")]
]

PRESS_MERGE_IMAGE = "الآن أرسل الصورة الأخرى و اختر دمج الآن "
PRESS_MERGE_IMAGE_BUTTONS = [
    [InlineKeyboardButton("دمج الآن ",callback_data="imagemergenow")]
     ]
CHOOSE_UR_TRIMMODE = "اختر نمط القص"
CHOOSE_UR_TRIMMODE_BUTTONS = [
    [InlineKeyboardButton("قص عادي",callback_data="normaltrim")],
    [InlineKeyboardButton("قص معكوس",callback_data="reversetrim")]
     ]
CHOOSE_UR_RTRIMFILE_MODE = "اختر نوع ملفك "
CHOOSE_UR_RTRIMFILE_MODE_BUTTONS = [   
    [InlineKeyboardButton("صوتية",callback_data="rtrimaud")]
     ]
PRESS_MERGEMODE_IMAGE = "اختر نمط الدمج "
PRESS_MERGEMODE_IMAGE_BUTTONS = [
    [InlineKeyboardButton("متجاورتين بالجانب",callback_data="sidebyside")],
    [InlineKeyboardButton("الأولى فوق والثانية تحت ",callback_data="updown")]

     ]
CHOOSE_UR_DL_MODE = "اختر نمط التنزيل "
CHOOSE_UR_DL_MODE_BUTTONS = [
    [InlineKeyboardButton("VIDEO 360P",callback_data="vid360")],
    [InlineKeyboardButton("VIDEO 720P ",callback_data="vid720")],
    [InlineKeyboardButton("AUDIO",callback_data="auddl")],
    
]
CHOOSE_UR_AMPLE_MODE = "اختر نمط التضخيم "
CHOOSE_UR_AMPLE_MODE_BUTTONS = [
    [InlineKeyboardButton("5db",callback_data="mod1")],
     [InlineKeyboardButton("10db",callback_data="mod2")],
     [InlineKeyboardButton("15db",callback_data="mod3")],
     [InlineKeyboardButton("20db",callback_data="mod4")],
     [InlineKeyboardButton("25db",callback_data="mod5")]
]
THE_LAST_IMAGE = "عند إرسال آخر صورة , اضغط تحويل الآن"
THE_LAST_IMAGE_BUTTONS = [
   [InlineKeyboardButton("تحويل الآن ",callback_data="convnow")]
]

CHOOSE_UR_VIDRES_MODE = "الآن اختر أبعادالناتج"
CHOOSE_UR_VIDRES_MODE_BUTTONS = [
    [InlineKeyboardButton("9:16",callback_data="vidresnow11")],
    [InlineKeyboardButton("16:9",callback_data="vidresnow169")]
]
CHOOSE_UR_COMP_MODE = " اختر نمط الضغط \n كلما قل الرقم زاد الضغط و قل حجم الصوتية "
CHOOSE_UR_COMP_MODE_BUTTONS = [
    [InlineKeyboardButton("10k",callback_data="compmod1")],
     [InlineKeyboardButton("20k",callback_data="compmod2")],
     [InlineKeyboardButton("30k",callback_data="compmod3")],
     [InlineKeyboardButton("40k",callback_data="compmod4")],
     [InlineKeyboardButton("50k",callback_data="compmod5")]
]

CHOOSE_UR_FILE_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILE_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="aud")],
     [InlineKeyboardButton("فيديو ",callback_data="vid")]
]

CHOOSE_UR_YTPLST_MODE = "اختر نمط التحميل "
CHOOSE_UR_YTPLST_MODE_BUTTONS = [
    [InlineKeyboardButton("VID 360",callback_data="ytplstvid360")],
     [InlineKeyboardButton("VID 720 ",callback_data="ytplstvid720")],
      [InlineKeyboardButton("AUD ",callback_data="ytplstaud")]

]

CHOOSE_UR_FILETRIM_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILETRIM_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="audtrim")],
     [InlineKeyboardButton("فيديو ",callback_data="vidtrim")]
     ]
CHOOSE_UR_FILERENM_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILERENM_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="audrenm")],
     [InlineKeyboardButton("فيديو ",callback_data="vidrenm")],
     [InlineKeyboardButton("وثيقة",callback_data="docrenm")]
]
CHOOSE_UR_FILESPED_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILESPED_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="speedfileaud")],
     [InlineKeyboardButton("فيديو ",callback_data="speedfilevid")]
]

CHOOSE_UR_SPEED_MODE = "اختر نمط التسريع "
CHOOSE_UR_SPEED_MODE_BUTTONS = [
    [InlineKeyboardButton("x1.25",callback_data="spd1")],
     [InlineKeyboardButton("x1.5 ",callback_data="spd2")],
     [InlineKeyboardButton("x1.75",callback_data="spd3")],
      [InlineKeyboardButton("x2",callback_data="spd4")]
]
CHOOSE_UR_PDFMERGE_MODE = " بعد الانتهاء من إرسال الملفات اضغط دمج الآن "
CHOOSE_UR_PDFMERGE_MODE_BUTTONS = [
  [InlineKeyboardButton("دمج الآن ",callback_data="pdfmergenow")]
]
CHOOSE_UR_MERGE = "أرسل الصوتية التالية  \n تنبيه / بعد الانتهاء من إرسال الصوتيات اضغط دمج الآن "
CHOOSE_UR_MERGE_BUTTONS = [
    [InlineKeyboardButton("دمج الآن ",callback_data="mergenow")] ]

CHOOSE_UR_CONV_MODE = "اختر نمط التحويل"
CHOOSE_UR_CONV_MODE_BUTTONS = [
    [InlineKeyboardButton("تحويل صوتية/ فيديو إلى mp3",callback_data="audconv")],
     [InlineKeyboardButton("تحويل صوتية/ فيديو إلى m4a",callback_data="audconvm4a")],
    [InlineKeyboardButton("تحويل فيديو إلى mp4 ",callback_data="vidconv")]
]
CHOOSE_UR_SUBS_MODE = '''اختر ما يناسب'''
CHOOSE_UR_SUBS_MODE_BUTTONS = [
    [InlineKeyboardButton("هذا الفيديو",callback_data="thisisvid")], [InlineKeyboardButton("إبدال الآن",callback_data="subsnow")]]
CHOOSE_UR_MON_MODE = '''اختر ما يناسب'''
CHOOSE_UR_MON_MODE_BUTTONS = [
    [InlineKeyboardButton("هذه الصورة",callback_data="thisisimage")], [InlineKeyboardButton("منتجة الآن",callback_data="montagnow")]]
CHOOSE_UR_RESO_MODE = '''اختر ما يناسب'''
CHOOSE_UR_RESO_MODE_BUTTONS = [
    [InlineKeyboardButton("فيديو اعتيادي",callback_data="normalvideo")], [InlineKeyboardButton("YT Short",callback_data="ytshort")]]

@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت متعدد الاستعمالات , فقط أرسل الفيديو أو الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/sunnay6626/2 ",disable_web_page_preview=True)

@bot.on_message(filters.command('setbucket') & filters.text & filters.private)
def command9(bot,message):
  global bucketname
  bucketname = message.text.split("setbucket", maxsplit=1)[1]
  bucketname = bucketname.replace(" ", "")
  message.reply_text("تم ضبط المعرف ")

@bot.on_message(filters.command('ytdl') & filters.text & filters.private)
def command20(bot,message):
     global yt_id , ytlink
     dlmode = message.text.split(" ")[-1] 
     ytlink = message.text.split("ytdl", maxsplit=1)[1].replace(" ", "")
     yt_id = message.from_user.id
     with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{ytlink}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "")
        video = f"{video_title}.mp4" 
        audio = f"{video_title}.mp3"      
     if dlmode == "vid" :  
       cmd(f'''yt-dlp -f 18 -ciw  -o "{video}" "{ytlink}"''')
       bot.send_video(yt_id, video,caption=video_title)
       os.remove(video)
     elif dlmode == "vid720" :
       cmd(f'''yt-dlp -f 18 -ciw  -o "{video}" "{ytlink}"''')
       bot.send_video(yt_id, video,caption=video_title)
       os.remove(video)
     else : 
       cmd(f'''yt-dlp -ciw  --extract-audio --audio-format mp3  -o "{audio}"  "{ytlink}"''')
       bot.send_audio(yt_id, audio,caption=video_title)
       os.remove(audio)
@bot.on_message(filters.command('yttransy') & filters.text & filters.private)
def command4(bot,message):
     url = message.text.split("yttransy ", maxsplit=1)[1]
     yttransyid = message.from_user.id
     cmd(f'''yt-dlp --flat-playlist -i --print-to-file url yttransy.txt {url}''')
     cmd(f'''wc -l < yttransy.txt > "{temptxt}"''')
     with open(temptxt, 'r') as file:
      temp = file.read().rstrip('\n') 
     numbofvid = int(temp) + 1
     os.remove(temptxt)
     for i in range(1,numbofvid):
         cmd(f'sed -n {i}p yttransy.txt > "{temptxt}"')
         with open(temptxt, 'r') as file:
           link = file.read().rstrip('\n')  
         with YoutubeDL() as ydl: 
          info_dict = ydl.extract_info(f'{link}', download=False)
          video_url = info_dict.get("url", None)
          video_id = info_dict.get("id", None)
          video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "") 
          mp32file =   f"{video_title}.mp3"
          txtresfile = f"{video_title}.txt"
          mp42file =   f"{video_title}.mp4"
         cmd(f'''yt-dlp -ciw  --extract-audio --audio-format mp3  -o "{video_title}" "{link}"''')
         cmd(f'''python3 speech.py RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH "{mp32file}" "{txtresfile}"''')
         bot.send_document(yttransyid, txtresfile,caption=video_title)
         os.remove(mp32file)
         os.remove(temptxt)
         os.remove(txtresfile)
     os.remove("yttransy.txt")
@bot.on_message(filters.command('ytplst') & filters.text & filters.private)
def command4(bot,message):
     x = message.text.split(" ")[1]
     url = x.split(" ")[0]
     dlmode = message.text.split(" ")[-1] 
     global ytplstid
     ytplstid = message.from_user.id
     cmd(f'''yt-dlp --flat-playlist -i --print-to-file url ytplst.txt {url}''')
     cmd(f'''wc -l < ytplst.txt > "{temptxt}"''')
     with open(temptxt, 'r') as file:
      temp = file.read().rstrip('\n') 
     global plstnumbofvid
     plstnumbofvid = int(temp) + 1
     os.remove(temptxt)
     if dlmode == "vid" : 
       for i in range(1,plstnumbofvid):
         cmd(f'sed -n {i}p ytplst.txt > "{temptxt}"')
         with open(temptxt, 'r') as file:
           link = file.read().rstrip('\n')  
         with YoutubeDL() as ydl: 
          info_dict = ydl.extract_info(f'{link}', download=False)
          video_url = info_dict.get("url", None)
          video_id = info_dict.get("id", None)
          video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "") 
          mp32file =   f"{video_title}.mp3"
          txtresfile = f"{video_title}.txt"
          mp42file =   f"{video_title}.mp4"
         cmd(f'''yt-dlp -f 18 -ciw  -o "{mp42file}" "{link}"''')
         bot.send_video(ytplstid, mp42file,caption=video_title)
         os.remove(mp42file)
         os.remove(temptxt)
     elif dlmode == "vid720":
      for i in range(1,plstnumbofvid):
         cmd(f'sed -n {i}p ytplst.txt > "{temptxt}"')
         with open(temptxt, 'r') as file:
           link = file.read().rstrip('\n')  
         with YoutubeDL() as ydl: 
          info_dict = ydl.extract_info(f'{link}', download=False)
          video_url = info_dict.get("url", None)
          video_id = info_dict.get("id", None)
          video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "") 
          mp32file =   f"{video_title}.mp3"
          txtresfile = f"{video_title}.txt"
          mp42file =   f"{video_title}.mp4"
         cmd(f'''yt-dlp -f 22 -ciw  -o "{mp42file}" "{link}"''')
         bot.send_video(ytplstid, mp42file,caption=video_title)
         os.remove(mp42file)
         os.remove(temptxt)
     else : 
      for i in range(1,plstnumbofvid):
         cmd(f'sed -n {i}p ytplst.txt > "{temptxt}"')
         with open(temptxt, 'r') as file:
           link = file.read().rstrip('\n')  
         with YoutubeDL() as ydl: 
          info_dict = ydl.extract_info(f'{link}', download=False)
          video_url = info_dict.get("url", None)
          video_id = info_dict.get("id", None)
          video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "") 
          mp32file =   f"{video_title}.mp3"
          txtresfile = f"{video_title}.txt"
          mp42file =   f"{video_title}.mp4"
         cmd(f'''yt-dlp -ciw  --extract-audio --audio-format mp3  -o "{video_title}"  "{link}"''')
         bot.send_audio(ytplstid, mp32file,caption=video_title)
         os.remove(mp32file)
         os.remove(temptxt)
     os.remove("ytplst.txt")





@bot.on_message(filters.command('upld') & filters.text & filters.private)
def command2(bot,message):
     url = message.text.split("upld ", maxsplit=1)[1]
     upld_id = message.from_user.id
     a= urlparse(url).path 
     url_parsed = urlparse(url)
     a = unquote(url_parsed.path)
     filename =a.split("/")[-1] 
     if filename.endswith('.mp3' or '.m4a' or '.ogg') :
      cmd(f'''wget -O "{filename}" "{url}"''')
      with open(filename,'rb') as f : 
        bot.send_audio(upld_id,f)
     elif filename.endswith('.mp4' or '.mkv' or '.wmv') :
      cmd(f'''wget -O "{filename}" "{url}"''')
      with open(filename,'rb') as f : 
       bot.send_video(upld_id,f)
     else :
      cmd(f'''wget -O "{filename}" "{url}"''')
      with open(filename,'rb') as f : 
       bot.send_document(upld_id,f)
@bot.on_message(filters.command('clear') & filters.private)
def command2(bot,message):
    os.remove("ytplst.txt")
    os.remove("yttransy.txt")
    shutil.rmtree("./mergy/")
    shutil.rmtree("./downloads/")

queeq = []   
@bot.on_message(filters.private & filters.incoming & filters.voice | filters.audio | filters.video | filters.document | filters.photo | filters.animation )
async def _telegram_file(client, message):
 global user_id ,file_path,filename,nom,ex,mp4file,mp3file,m4afile,spdrateaud,mergdir,trimdir,result,nepho
 if len(queeq) == 0 : 
    pass
 else :
    await asyncio.sleep(30)
    queeq.clear()
    pass
 nepho = message
 user_id = nepho.from_user.id
 queeq.append(user_id)
 x =  await nepho.download(file_name="./downloads/")
 file_path = x.replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "")
 if file_path == x :
     pass
 else :
     os.rename(x,file_path)
 await nepho.reply(text = CHOOSE_UR_AUDIO_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AUDIO_MODE_BUTTONS))
 filename = os.path.basename(file_path)
 nom,ex = os.path.splitext(filename)
 mp4file = f"{nom}.mp4"
 mp3file = f"{nom}.mp3"
 m4afile = f"{nom}.m4a"
 mergdir = f"./mergy/{mp3file}"
 trimdir = f"./trimmo/{mp3file}" 
 result = f"{nom}.txt"    
 @bot.on_callback_query()
 async def callback_query(CLIENT,CallbackQuery): 
  global amplemode
  await CallbackQuery.edit_message_text("جار العمل")
  if CallbackQuery.data == "amplifyaud":
     await CallbackQuery.edit_message_text(text = CHOOSE_UR_AMPLE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AMPLE_MODE_BUTTONS))
  elif CallbackQuery.data == "comp":
   await CallbackQuery.edit_message_text(text = CHOOSE_UR_COMP_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_COMP_MODE_BUTTONS) )
  elif  CallbackQuery.data == "compmod1":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 10k "{mp3file}" -y ''' )
    await bot.send_audio(user_id, mp3file)
    os.remove(file_path) 
    os.remove(mp3file) 
  elif  CallbackQuery.data == "titled":
      os.rename(file_path,filename)
      await bot.send_document(user_id, filename)
      await CallbackQuery.edit_message_text("تم الإرسال  ") 
      os.remove(filename)
  elif  CallbackQuery.data == "voicy":   
    await CallbackQuery.edit_message_text("جار تغيير الصوت ") 
    cmd(f'''ffmpeg -i "{file_path}" -af asetrate=44100*0.9,aresample=44100,atempo=1/0.9 "{mp3file}"''')
    await bot.send_audio(user_id, mp3file)
    os.remove(file_path) 
    os.remove(mp3file) 
  elif  CallbackQuery.data == "thisisvid":
     os.rename(file_path,"./downloads/subsvid.mp4")
     await CallbackQuery.edit_message_text("الآن أرسل الصوت الجديد ثم اختر إبدال الآن") 
  elif  CallbackQuery.data == "thisisimage":
     os.rename(file_path,"./downloads/imagetovid.jpg")
     await CallbackQuery.edit_message_text("الآن أرسل الصوت  ثم اختر منتجة الآن") 

  elif  CallbackQuery.data == "subs":
     await CallbackQuery.edit_message_text(text = CHOOSE_UR_SUBS_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SUBS_MODE_BUTTONS))
  elif  CallbackQuery.data == "imagetovid":
     await CallbackQuery.edit_message_text(text = CHOOSE_UR_MON_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MON_MODE_BUTTONS))
  elif  CallbackQuery.data == "subsnow":
      await CallbackQuery.edit_message_text("جار الإبدال ") 
      cmd(f'''ffmpeg -i "./downloads/subsvid.mp4" -i "{file_path}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
      await bot.send_video(user_id, mp4file)
      os.remove(file_path) 
      os.remove(mp4file) 
  elif  CallbackQuery.data == "montagnow":
      global thisismontagaudio
      thisismontagaudio = file_path
      await CallbackQuery.edit_message_text(text = CHOOSE_UR_RESO_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_RESO_MODE_BUTTONS))
  elif CallbackQuery.data == "normalvideo":
      await CallbackQuery.edit_message_text("جار المنتجة ") 
      cmd(f'''ffmpeg -i "{thisismontagaudio}" -q:a 0 -map a "./downloads/temp{mp3file}" -y ''')
      cmd(f'''ffmpeg -r 1 -loop 1 -y -i  "./downloads/imagetovid.jpg" -i "./downloads/temp{mp3file}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 "{mp4file}"''')
      await bot.send_video(user_id, mp4file)
      os.remove(file_path) 
      os.remove(mp4file) 
  elif CallbackQuery.data == "ytshort":
      await CallbackQuery.edit_message_text("جار المنتجة ") 
      cmd(f'''ffmpeg -i "{thisismontagaudio}" -q:a 0 -map a "./downloads/temp{mp3file}" -y ''')
      cmd(f'''ffmpeg -r 1 -loop 1 -y -i  "./downloads/imagetovid.jpg" -i "./downloads/temp{mp3file}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1080:1920 "{mp4file}"''')
      await bot.send_video(user_id, mp4file)
      os.remove(file_path) 
      os.remove(mp4file) 
  elif  CallbackQuery.data == "compmod2":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 20k "{mp3file}" -y ''' )
    await bot.send_audio(user_id, mp3file)
    os.remove(file_path) 
    os.remove(mp3file) 

  elif  CallbackQuery.data == "compmod3":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 30k "{mp3file}" -y ''' )
    await bot.send_audio(user_id, mp3file)
    os.remove(file_path) 
    os.remove(mp3file)  

  elif  CallbackQuery.data == "compmod4":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 40k "{mp3file}" -y ''' )
    await bot.send_audio(user_id, mp3file)
    os.remove(file_path) 
    os.remove(mp3file) 

  elif  CallbackQuery.data == "compmod5":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 50k "{mp3file}" -y ''' )
    await bot.send_audio(user_id, mp3file)
    os.remove(file_path) 
    os.remove(mp3file) 

  elif CallbackQuery.data == "conv" :
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_CONV_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_CONV_MODE_BUTTONS))
  elif CallbackQuery.data == "audconv" :
   await CallbackQuery.edit_message_text("جار التحويل ") 
   cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3file}" -y ''')
   await  bot.send_audio(user_id, mp3file)
   os.remove(file_path) 
   os.remove(mp3file) 
  elif CallbackQuery.data == "audconvm4a" :
   await CallbackQuery.edit_message_text("جار التحويل ") 
   cmd(f'''ffmpeg -i "{file_path}" -c:a aac -b:a 192k "{m4afile}" -y ''')
   await bot.send_document(user_id, m4afile)
   os.remove(file_path) 
   os.remove(m4afile) 

  elif CallbackQuery.data == "vidconv" :
   await CallbackQuery.edit_message_text("جار التحويل " ) 
   cmd(f'''ffmpeg -i "{file_path}" -codec copy "{mp4file}" -y ''')
   await bot.send_video(user_id, mp4file)
   os.remove(file_path) 
   os.remove(mp4file) 

  elif CallbackQuery.data == "trim" :
   await nepho.reply_text("الآن أرسل نقطة البداية والنهاية بهذه الصورة \n\n hh:mm:ss/hh:mm:ss",reply_markup=ForceReply(True))
   await CallbackQuery.edit_message_text("👇") 
  elif CallbackQuery.data == "mod1":
      amplemode = 5
      await CallbackQuery.edit_message_text(text = CHOOSE_UR_FILE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS))
  elif CallbackQuery.data == "mod2":
      amplemode = 10
      await CallbackQuery.edit_message_text(text = CHOOSE_UR_FILE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS))
  elif CallbackQuery.data == "mod3":
      amplemode = 15
      await CallbackQuery.edit_message_text(text = CHOOSE_UR_FILE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS))
  elif CallbackQuery.data == "mod4" :
      amplemode = 20
      await CallbackQuery.edit_message_text(text = CHOOSE_UR_FILE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS))
  elif CallbackQuery.data == "mod5":
      amplemode = 25
      await CallbackQuery.edit_message_text(text = CHOOSE_UR_FILE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS) )

  elif CallbackQuery.data == "aud":
    await CallbackQuery.edit_message_text("جار التضخيم ")
    cmd(f'''ffmpeg -i "{file_path}" -filter:a volume={amplemode}dB "{mp3file}"''')
    await bot.send_audio(user_id, mp3file)
    os.remove(file_path) 
    os.remove(mp3file) 

  elif CallbackQuery.data == "vid":
    await CallbackQuery.edit_message_text("جار التضخيم " )
    cmd(f'''ffmpeg -i "{file_path}" -filter:a volume={amplemode}dB "{mp3file}"''')
    cmd(f'''ffmpeg -i "{file_path}" -i "{mp3file}" -c:v copy -map 0:v:0 -map 1:a:0 "{filename}"''')
    await bot.send_video(user_id, filename) 
    os.remove(file_path) 
    os.remove(filename) 

  elif CallbackQuery.data == "audtrim":
    await CallbackQuery.edit_message_text("جار القص")  
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "trim{mp3file}" -y ''')
    cmd(f'''ffmpeg -i "trim{mp3file}" -ss {strt_point} -to {end_point} -c copy "{mp3file}" -y ''')
    await  bot.send_audio(user_id, mp3file)
    os.remove(file_path) 
    os.remove(mp3file) 
    os.remove(f"trim{mp3file}")
      
  elif CallbackQuery.data == "vidtrim":
    await CallbackQuery.edit_message_text("جار القص")  
    cmd(f'''ffmpeg -i "{file_path}" -ss {strt_point} -strict -2 -to {end_point} -c:a aac -codec:v h264 -b:v 1000k "{mp4file}" -y ''')
    await bot.send_video(user_id, mp4file)   
    os.remove(file_path) 
    os.remove(mp4file) 
  elif CallbackQuery.data == "renm":
    await CallbackQuery.edit_message_text("👇") 
    await nepho.reply_text("الآن أدخل الاسم الجديد ",reply_markup=ForceReply(True))
  elif CallbackQuery.data == "audrenm":
    await CallbackQuery.edit_message_text("👇")
    await  bot.send_audio(user_id, newfile)
    os.remove(newfile)
  elif CallbackQuery.data == "vidrenm":
    await CallbackQuery.edit_message_text("👇")
    await  bot.send_video(user_id, newfile)
    os.remove(newfile)
  elif CallbackQuery.data == "docrenm":
    await CallbackQuery.edit_message_text("👇")
    await bot.send_document(user_id, newfile)
    os.remove(newfile)
  elif CallbackQuery.data == "transcribe":
    try: 
      with open('transcription.txt', 'r') as fh:
        if os.stat('transcription.txt').st_size == 0: 
            pass
        else:
            CallbackQuery.edit_message_text("هناك عملية تفريغ تتم الآن")
            return
    except FileNotFoundError: 
      pass  
    await CallbackQuery.edit_message_text("جار التفريغ")
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3file}" -y ''')  
    cmd(f'''python3 speech.py RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH "{mp3file}" "transcription.txt" ''')
    os.rename("transcription.txt",result)
    await bot.send_document(user_id, result)
    await CallbackQuery.edit_message_text("تم التفريغ ✅  ")   
    os.remove(file_path) 
    os.remove(mp3file) 
    os.remove(result) 
  elif CallbackQuery.data == "mute":
    await CallbackQuery.edit_message_text("جار الكتم")
    cmd(f'''ffmpeg -i "{file_path}" -c copy -an "{mp4file}"''')
    await bot.send_document(user_id, mp4file)
    os.remove(file_path) 
    os.remove(mp4file) 

  elif CallbackQuery.data == "speedy":
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_SPEED_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SPEED_MODE_BUTTONS))
  elif CallbackQuery.data == "spd1":
    global spdratevid
    spdratevid = 0.8
    global spdrateaud
    spdrateaud = 1.25
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_FILESPED_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS))
  elif CallbackQuery.data == "spd2":
    spdratevid = 0.66666666666
    spdrateaud = 1.5
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_FILESPED_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS))
  elif CallbackQuery.data == "spd3":
    spdratevid = 0.57142857142
    spdrateaud = 1.75
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_FILESPED_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS))
  elif CallbackQuery.data == "spd4":
    spdratevid = 0.5
    spdrateaud = 2
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_FILESPED_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS))
  elif CallbackQuery.data == "speedfileaud":
    await CallbackQuery.edit_message_text("جار التسريع")
    cmd(f'''ffmpeg -i "{file_path}" -filter:a "atempo={spdrateaud}" -vn "{mp3file}" -y ''')
    await bot.send_audio(user_id, mp3file) 
    os.remove(file_path) 
    os.remove(mp3file) 
  
  
  elif CallbackQuery.data == "speedfilevid":
    await CallbackQuery.edit_message_text("جار التسريع")
    cmd(f'''ffmpeg -i "{file_path}" -filter_complex "[0:v]setpts={spdratevid}*PTS[v];[0:a]atempo={spdrateaud}[a]" -map "[v]" -map "[a]" "{mp4file}" -y ''')
    await  bot.send_video(user_id,mp4file)
    os.remove(file_path) 
    os.remove(mp4file) 

  elif CallbackQuery.data == "audmerge":
    await CallbackQuery.edit_message_text("جار الإضافة ")
    audmergelist.append(file_path)
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_MERGE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MERGE_BUTTONS))
  elif CallbackQuery.data == "mergenow":
    await CallbackQuery.edit_message_text("جار الدمج") 
    cmd(f'''mkdir mergy''')
    for x in range(0,len(audmergelist)) :
     mp3merge = f"{nom}{random.randint(0,100)}.mp3"
     cmd(f'''ffmpeg -i "{audmergelist[x]}" -q:a 0 -map a "{mp3merge}" -y ''')
     os.remove(audmergelist[x])
     with open('list.txt','a') as f:
      f.write(f'''file '{mp3merge}' \n''')
    cmd(f'''ffmpeg -f concat -safe 0 -i list.txt "{mp3file}" -y ''')
    await bot.send_audio(user_id, mp3file)
    os.remove("list.txt")
    os.remove(mp3file)
    shutil.rmtree('./mergy/') 
    audmergelist.clear()
  elif CallbackQuery.data == "splitty":
    await CallbackQuery.edit_message_text("جار التقسيم") 
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a mod.mp3 -y''')
    cmd(f'mkdir parts')
    cmd(f'''ffmpeg -i "mod.mp3" -f segment -segment_time 300 -c copy "./parts/{nom}%09d.wav" -y''')
    dir_path = "./parts/"
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
                            count += 1
                            numbofitems=count
    if numbofitems<10 :
        
     coca=0
     while (coca < numbofitems): 
             pathy=f"./parts/{nom}00000000{coca}.wav"
             reso = f"{nom}00000000{coca}.mp3"
             cmd(f'''ffmpeg -i "{pathy}" -q:a 0 -map a "{reso}" -y''')
             await bot.send_audio(user_id, reso)
             os.remove(reso)
             coca += 1 
    else :
     coca=0 
     while (coca < 10): 
             pathy=f"./parts/{nom}00000000{coca}.wav"
             reso = f"{nom}00000000{coca}.mp3"
             cmd(f'''ffmpeg -i "{pathy}" -q:a 0 -map a "{reso}" -y''')
             await bot.send_audio(user_id, reso)
             os.remove(reso)
             coca += 1        
     coca=10
     while (coca < numbofitems ): 
             pathy=f"./parts/{nom}0000000{coca}.wav"
             reso = f"{nom}00000000{coca}.mp3"
             cmd(f'''ffmpeg -i "{pathy}" -q:a 0 -map a "{reso}" -y''')
             await  bot.send_audio(user_id, reso)
             os.remove(reso)
             coca += 1                                      
    await shutil.rmtree('./parts/') 
    os.remove("mod.mp3") 
    os.remove(file_path) 
  elif CallbackQuery.data == "OCR":
    await CallbackQuery.edit_message_text("جار التفريغ")
    lang_code = "ara"
    data_url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang_code}.traineddata"
    dirs = r"/usr/share/tesseract-ocr/4.00/tessdata"
    path = os.path.join(dirs, f"{lang_code}.traineddata")
    data = requests.get(data_url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
    open(path, 'wb').write(data.content)
    text = pytesseract.image_to_string(file_path, lang=f"{lang_code}")
    textspaced = re.sub(r'\r\n|\r|\n', ' ', text)
    await nepho.reply(textspaced[:-1], quote=True, disable_web_page_preview=True)
    os.remove(file_path) 
  elif CallbackQuery.data == "pdfOCR":
    try: 
      with open('final.txt', 'r') as fh:
        if os.stat('final.txt').st_size == 0: 
            pass
        else:
            await CallbackQuery.edit_message_text("هناك تفريغ يتم الآن ") 
            return
    except FileNotFoundError: 
     pass  
    await CallbackQuery.edit_message_text("جار التفريغ")
    cmd('mkdir temp')
    pdf = pdfium.PdfDocument(f'{file_path}')
    n_pages = len(pdf)
    for page_number in range(n_pages):
     page = pdf.get_page(page_number)
     pil_image = page.render_topil(
        scale=1,
        rotation=0,
        crop=(0, 0, 0, 0),
        colour=(255, 255, 255, 255),
        annotations=True,
        greyscale=False,
        optimise_mode=pdfium.OptimiseMode.NONE,
    )
     pil_image.save(f"./temp/image_{page_number+1}.png")
    os.remove(file_path) 
    count = 0
    for path in os.listdir("./temp/"):
                if os.path.isfile(os.path.join("./temp/", path)):
                            count += 1
                            numbofitems=count
    coca=1
    final = numbofitems 
    while (coca < final): 
     cmd(f'''sh textcleaner -g "./temp/image_{coca}.png" temp.png ''')
     lang_code = "ara"
     data_url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang_code}.traineddata"
     dirs = r"/usr/share/tesseract-ocr/4.00/tessdata"
     path = os.path.join(dirs, f"{lang_code}.traineddata")
     data = requests.get(data_url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
     open(path, 'wb').write(data.content)
     text = pytesseract.image_to_string(f"temp.png" , lang=f"{lang_code}")
     textspaced = re.sub(r'\r\n|\r|\n', ' ', text)
     with open("final.txt",'a') as f:
      f.write(f'''{textspaced} \n''')
     coca +=1
    os.rename("final.txt",result)
    await bot.send_document(user_id, result)
    shutil.rmtree('./temp/') 
    os.remove(result)
  elif CallbackQuery.data == "pdfcompress":
      await CallbackQuery.edit_message_text("جار الضغط")
      PDFNet.Initialize("demo:1676040759361:7d2a298a03000000006027df7c81c9e05abce088e7286e8312e5e06886"); doc = PDFDoc(f"{file_path}")
      doc.InitSecurityHandler()
      Optimizer.Optimize(doc)
      doc.Save(f"{filename}", SDFDoc.e_linearized)
      doc.Close()
      await bot.send_document(user_id, filename)
      os.remove(file_path) 
      os.remove(filename) 
  elif CallbackQuery.data == "pdfmerge":
      pdfdir = f"pdfmerge/{filename}"
      cmd("mkdir pdfmerge")
      cmd(f'''mv "{file_path}" ./pdfmerge/''')
      with open('pdfy.txt','a') as f:
       f.write(f'''{pdfdir} \n''')  
      await CallbackQuery.edit_message_text(text = CHOOSE_UR_PDFMERGE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_PDFMERGE_MODE_BUTTONS))
  elif CallbackQuery.data == "pdfmergenow":
      await CallbackQuery.edit_message_text("جار الدمج")
      pdfs = []
      with open("pdfy.txt", "r") as file:
       for line in file:
        pdfs.append(line.strip())
      merger = PdfMerger()
      for pdf in pdfs:
       merger.append(pdf)
      pdfmerged = f"{filename}.pdf"
      merger.write(pdfmerged)
      merger.close()
      await  bot.send_document(user_id,pdfmerged)
      shutil.rmtree("./pdfmerge/")
      cmd(f'''rm "{pdfmerged}" pdfy.txt''')
      os.remove(pdfmerged);os.remove("pdfy.txt")

  elif CallbackQuery.data == "pdftrim":
      await CallbackQuery.edit_message_text("👇")
      await nepho.reply_text(" الآن أرسل نقطة البداية والنهاية بهذه الصورة \n start-end ",reply_markup=ForceReply(True))
  elif CallbackQuery.data == "upldarch":
      if user_id==6234365091 :
         await CallbackQuery.edit_message_text("جار الرفع")
         cmd(f'''rclone copy "{file_path}" 'myarchive':"{bucketname}"''')
         os.remove(file_path)
         await CallbackQuery.edit_message_text("تم الرفع")
      else :
         await CallbackQuery.edit_message_text("هذه الميزة متوفرة لمالك البوت فقط")
  elif CallbackQuery.data == "rmvlines":
      await CallbackQuery.edit_message_text("جار العمل")
      with open(file_path, 'r') as file:
           text = file.read().replace("\n", " ")
      with open(filename,'a') as f:
       f.write(text)
      await bot.send_document(user_id,filename) 
      os.remove(file_path)
      os.remove(filename)
  elif CallbackQuery.data == "vidasp":
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_VIDRES_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_VIDRES_MODE_BUTTONS))
  elif CallbackQuery.data == "vidresnow11":
    await  CallbackQuery.edit_message_text("جار التحويل")
    cmd(f'''ffmpeg -i "{file_path}" -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1:color=black" "{mp4file}"''')
    await bot.send_document(user_id,mp4file) 
  elif CallbackQuery.data == "vidresnow169":
    await  CallbackQuery.edit_message_text("جار التحويل")
    cmd(f'''ffmpeg -i "{file_path}" -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:-1:-1:color=black" "{mp4file}"''')
    await bot.send_video(user_id,mp4file) 
  elif CallbackQuery.data == "rmvsilence" :
   await  CallbackQuery.edit_message_text("جار إزالة الصمت")
   cmd(f'''ffmpeg -i "{file_path}" -af "silenceremove=start_periods=1:stop_periods=-1:start_threshold=-30dB:stop_threshold=-50dB:start_silence=2:stop_silence=2" "{mp3file}"''')
   await bot.send_audio(user_id,mp3file)
   os.remove(file_path)
   os.remove(mp3file)
  elif CallbackQuery.data == "imagestitch" :
     imagedic.append(file_path)
     await CallbackQuery.edit_message_text(text = PRESS_MERGE_IMAGE,reply_markup = InlineKeyboardMarkup(PRESS_MERGE_IMAGE_BUTTONS))
  elif CallbackQuery.data == "imagemergenow" :
          await CallbackQuery.edit_message_text(text = PRESS_MERGEMODE_IMAGE,reply_markup = InlineKeyboardMarkup(PRESS_MERGEMODE_IMAGE_BUTTONS))
  elif CallbackQuery.data == "sidebyside" :
     output_img = f"{nom}.jpg"
     image1 = str(imagedic[0])
     image2 = str(imagedic[1])
     merged = merge_images2( image1, image2 )
     merged.save(output_img) 
     if len(imagedic) > 2 :
        for x in range(2,len(imagedic)) :
          image1 = output_img
          image2 = str(imagedic[x])
          merged = merge_images2( image1, image2 )
          merged.save(output_img) 
     await bot.send_document(user_id,output_img)
     for x in range(0,len(imagedic)) :
      os.remove(str(imagedic[x]))
     imagedic.clear()
     os.remove(output_img)

  elif CallbackQuery.data == "updown" :
     output_img = f"{nom}.jpg"
     image1 = imagedic[0]
     image2 = imagedic[1]
     merged = merge_images1( image1, image2 )
     merged.save(output_img) 
     if len(imagedic) > 2 :
        for x in range(2,len(imagedic)) :
          image1 = output_img
          image2 = str(imagedic[x])
          merged = merge_images1( image1, image2 )
          merged.save(output_img) 
     else :
        pass
     await bot.send_document(user_id,output_img)
     for x in range(0,len(imagedic)) :
      os.remove(str(imagedic[x]))
     imagedic.clear()
     os.remove(output_img)
  elif CallbackQuery.data == "imagetogif" :
      await nepho.reply_text("الآن أرسل مدة الفيديو بالثانية بهذه الصورة \n t=المدة",reply_markup=ForceReply(True))
  elif CallbackQuery.data == "imagetopdf" :
    imagepdfdic1.append(file_path)
    global imagey
    imagey = Image.open(imagepdfdic1[0]).convert('RGB')
    if len(imagepdfdic1) > 1 :
     image2 = Image.open(file_path).convert('RGB')
     imagepdfdic.append(image2)
    await CallbackQuery.edit_message_text(text = THE_LAST_IMAGE,reply_markup = InlineKeyboardMarkup(THE_LAST_IMAGE_BUTTONS))
  elif CallbackQuery.data == "convnow" :
    pdffile = f"{nom}.pdf"
    imagey.save(pdffile,save_all=True, append_images=imagepdfdic)
    await bot.send_document(user_id,pdffile)
    os.remove(pdffile)
    for x in range(0,len(imagepdfdic1)) :
      os.remove(str(imagepdfdic1[x]))
    imagepdfdic1.clear()
    imagepdfdic.clear()
  elif CallbackQuery.data == "vidsrt" :
     if len(vidsrt) == 0 or len(vidsrt) > 2 :
        vidsrt.clear()
        vidsrt.append(file_path)
        await CallbackQuery.edit_message_text("الآن أرسل الفيديو")
     elif len(vidsrt) == 1 : 
        vidsrt.append(file_path)
        subfile = vidsrt[0]
        vidfile = vidsrt[1]
        cmd(f'''ffmpeg -i "{vidfile}" -filter_complex subtitles='{subfile}' -c:a copy "{mp4file}"''')
        await bot.send_video(user_id,mp4file)
        os.remove(subfile)
        os.remove(vidfile)
        os.remove(mp4file)
  elif CallbackQuery.data == "normaltrim" :
         await CallbackQuery.edit_message_text(text = CHOOSE_UR_FILETRIM_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILETRIM_MODE_BUTTONS))
  elif CallbackQuery.data == "reversetrim" :
         await CallbackQuery.edit_message_text(text = CHOOSE_UR_RTRIMFILE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_RTRIMFILE_MODE_BUTTONS))
  elif CallbackQuery.data == "rtrimaud" :
     starsec = re.split(':',strt_point)
     if len(starsec) == 3 :
        strtseconds = int(starsec[0])*60*60 + int(starsec[1])*60 + int(starsec[2])
     elif len(starsec) == 2 : 
         strtseconds = int(starsec[0])*60 + int(starsec[1])
     elif len(starsec) == 1 : 
        strtseconds =  int(starsec[0])
     endsec = re.split(':',end_point)
     if len(endsec) == 3 :
        endseconds = int(endsec[0])*60*60 + int(endsec[1])*60 + int(endsec[2])
     elif len(endsec) == 2 : 
         endseconds = int(endsec[0])*60 + int(endsec[1])
     elif len(endsec) == 1 : 
        endseconds =  int(endsec[0])
     cmd(f'''ffmpeg -i "{file_path}" -af "aselect='not(between(t,{strtseconds},{endseconds}))'" "{mp3file}"''')
     await bot.send_audio(user_id,mp3file)
     os.remove(mp3file)
     os.remove(file_path)

     


     
  queeq.clear()


     





     
@bot.on_message(filters.private & filters.reply & filters.regex("="))
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          timeofvidstoned = message.text 
          msgid = message.reply_to_message_id
          await bot.delete_messages(user_id,msgid)
          await message.delete()
          startend = re.split('=',timeofvidstoned)
          timeofvid  = int(startend[1])  
          cmd(f'''ffmpeg -loop 1 -i "{file_path}" -c:v libx264 -t {timeofvid} -pix_fmt yuv420p -vf scale=1920:1080 "mod{mp4file}"''') 
          cmd(f'''ffmpeg -i "mod{mp4file}" -f lavfi -i anullsrc -map 0:v -map 1:a -c:v copy -shortest "{mp4file}"''')
          await bot.send_video(user_id,mp4file) 
          os.remove(mp4file)
          os.remove(f"mod{mp4file}")
          os.remove(file_path)

@bot.on_message(filters.private & filters.reply & filters.regex('/'))
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          endstart = message.text 
          msgid = message.reply_to_message_id
          await bot.delete_messages(user_id,msgid)
          await message.delete()
          global strt_point
          global end_point
          strt, end = os.path.split(endstart);strt_point=strt 
          end_point = end
          await message.reply(text = CHOOSE_UR_TRIMMODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_TRIMMODE_BUTTONS))
@bot.on_message(filters.private & filters.reply & filters.regex("-"))
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          pstartpend = message.text 
          msgid = message.reply_to_message_id
          await bot.delete_messages(user_id,msgid)
          await message.delete()
          global pdfstrt_point
          global pdfend_point
          startend = re.split('-',pstartpend)
          pdfstrt_point=int(startend[0])
          pdfend_point = int(startend[1])
          pages = (pdfstrt_point, pdfend_point)
          reader = PdfReader(file_path)
          writer = PdfWriter()
          page_range = range(pages[0], pages[1] + 1)
          for page_num, page in enumerate(reader.pages, 1):
           if page_num in page_range:
            writer.add_page(page)
           with open(filename, 'wb') as out:
            writer.write(out)
          with open(filename,'rb') as f : 
            await bot.send_document(user_id,f)
          os.remove(file_path) 
          os.remove(filename)
@bot.on_message(filters.private & filters.reply )
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          newname = message.text 
          msgid = message.reply_to_message_id
          await bot.delete_messages(user_id,msgid)
          await message.delete()
          global newfile
          newfile = f"{newname}{ex}"
          os.rename(file_path,newfile)
          await message.reply(text = CHOOSE_UR_FILERENM_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILERENM_MODE_BUTTONS))
        
bot.run()
