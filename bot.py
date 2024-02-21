global temptxt,imagedic,imagepdfdic
montaglist = []
vidsubslist = []
imagedic = []
imagepdfdic = []
imagepdfdic1 = []
vidsrt = []
audmergelist = []
vidmergelist = []
pdfqueemerge = []
queeq = []   
imageforms = [".jpg",".png"]
audioforms = [".mp3",".ogg",".m4a"]
videoforms = [".mp4",".mkv"]
temptxt = "res.txt"
import tika
tika.initVM()
from tika import parser
from oauth2client.file import Storage
from httplib2 import HttpLib2Error
from oauth2client.client import (
    OAuth2WebServerFlow,
    FlowExchangeError,
    OAuth2Credentials,
)
from http.client import (
    NotConnected,
    IncompleteRead,
    ImproperConnectionState,
    CannotSendRequest,
    CannotSendHeader,
    ResponseNotReady,
    BadStatusLine,
)

from apiclient import http, errors, discovery
from pyrogram import Client, filters,enums,StopTransmission
from zipfile import ZipFile 
import os ,re , random ,shutil,asyncio ,pytesseract,requests,logging,time,string,datetime,httplib2
from typing import Optional, Tuple, Union
from os import system as cmd
from youtube_transcript_api import YouTubeTranscriptApi
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery , ForceReply,Message
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
async def Coloringfunc(y):
   color = y
   if exo in imageforms :
      imgfile = f"{nom}.jpg"
      if color == "g" : 
       cmd(f'''sh color2gray -f rms "{file_path}" "{imgfile}" ''')
      elif color == "y" :
         cmd (f'''sh coloration -h 60 -s 50 -l 0 "{file_path}" "{imgfile}" '''  )
      elif color == "b":
          cmd (f'''sh coloration -h 180 -s 50 -l 0 "{file_path}" "{imgfile}" '''  )
      elif color == "r":
          cmd (f'''sh coloration -h 0 -s 50 -l 0 "{file_path}" "{imgfile}" '''  )
      elif color == "p":
         cmd (f'''sh coloration -h 330 -s 50 -l 0 "{file_path}" "{imgfile}" '''  )
      await bot.send_photo(user_id,imgfile)
      os.remove(file_path)
      os.remove(imgfile)
   elif exo == ".pdf":
    cmd('mkdir rvtemp')
    cmd('mkdir grtemp')
    pdf = pdfium.PdfDocument(file_path)
    n_pages = len(pdf)
    if color == "g":
     for page_number in range(n_pages):
      page = pdf.get_page(page_number)
      pil_image = page.render_topil(
        scale=1,
        rotation=0,
        crop=(0, 0, 0, 0),
        colour=(255, 255, 255, 255),
        annotations=True,
        greyscale=True,
        optimise_mode=pdfium.OptimiseMode.NONE,)
      pil_image.save(f"./rvtemp/image_{page_number+1}.png")
     os.remove(file_path)
    else : 
       for page_number in range(n_pages):
        page = pdf.get_page(page_number)
        pil_image = page.render_topil(
         scale=1,
         rotation=0,
         crop=(0, 0, 0, 0),
         colour=(255, 255, 255, 255),
         annotations=True,
         greyscale=False,
         optimise_mode=pdfium.OptimiseMode.NONE,)
        pil_image.save(f"./rvtemp/image_{page_number+1}.png")
       os.remove(file_path)
    for x in range(1,n_pages+1): 
      if color == "g":
       os.rename(f"./rvtemp/image_{x}.png",f"./grtemp/image_{x}.png")  
      elif color == "y" :
         cmd (f'''sh coloration -h 60 -s 50 -l 0 "./rvtemp/image_{x}.png" "./grtemp/image_{x}.png" '''  )
      elif color == "b":
          cmd (f'''sh coloration -h 180 -s 50 -l 0 "./rvtemp/image_{x}.png" "./grtemp/image_{x}.png" '''  )
      elif color == "r":
          cmd (f'''sh coloration -h 0 -s 50 -l 0 "./rvtemp/image_{x}.png" "./grtemp/image_{x}.png" '''  )
      elif color == "p":
         cmd (f'''sh coloration -h 330 -s 50 -l 0 "./rvtemp/image_{x}.png" "./grtemp/image_{x}.png" '''  )
      imagepdfdic1.append(f"./grtemp/image_{x}.png")
      imagey = Image.open(imagepdfdic1[0]).convert('RGB')  
                  
    if len(imagepdfdic1) > 1 :
       for x in range(1,len(imagepdfdic1)):
        image2 = Image.open(imagepdfdic1[x]).convert('RGB')
        imagepdfdic.append(image2)
    pdffile = f"{nom}.pdf"
    imagey.save(pdffile,save_all=True, append_images=imagepdfdic)
    await bot.send_document(user_id,pdffile)
    os.remove(pdffile)
    shutil.rmtree("./rvtemp/")
    shutil.rmtree("./grtemp/")
    imagepdfdic1.clear()
    imagepdfdic.clear()

@bot.on_message(filters.command('apiswitch1') & filters.private)
def command2(bot,message):
   global CLIENT_ID,CLIENT_SECRET
   CLIENT_ID = "389708947332-oienmum8v600cegsnhb6puk4prsv3pf6.apps.googleusercontent.com"
   CLIENT_SECRET = "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"
   message.reply_text("تم ضبط الـapi ")
@bot.on_message(filters.command('apiswitch2') & filters.private)
def command2(bot,message):
   global CLIENT_ID,CLIENT_SECRET
   CLIENT_ID = "664256487809-21lnbeqr7cau7fng78oeli1bnqcjthvp.apps.googleusercontent.com"
   CLIENT_SECRET = "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"
   message.reply_text("تم ضبط الـapi ")



async def progress(
    cur: Union[int, float],
    tot: Union[int, float],
    start_time: float,
    status: str,
    snt: Message,
    c: bot,
    download_id: str,
):
    if not c.download_controller.get(download_id):
        raise StopTransmission

    try:
        diff = int(time.time() - start_time)

        if (int(time.time()) % 5 == 0) or (cur == tot):
            await asyncio.sleep(1)
            speed, unit = human_bytes(cur / diff, True)
            curr = human_bytes(cur)
            tott = human_bytes(tot)
            eta = datetime.timedelta(seconds=int(((tot - cur) / (1024 * 1024)) / speed))
            elapsed = datetime.timedelta(seconds=diff)
            progress = round((cur * 100) / tot, 2)
            text = f"{status}\n\n{progress}% done.\n{curr} of {tott}\nSpeed: {speed} {unit}PS"
            f"\nETA: {eta}\nElapsed: {elapsed}"
            await snt.edit_text(
                text=text,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Cancel!", f"cncl+{download_id}")]]
                ),
            )

    except Exception as e:
        pass
class MaxRetryExceeded(Exception):
    pass


class UploadFailed(Exception):
    pass


class YouTube:

    MAX_RETRIES = 10

    RETRIABLE_EXCEPTIONS = (
        HttpLib2Error,
        IOError,
        NotConnected,
        IncompleteRead,
        ImproperConnectionState,
        CannotSendRequest,
        CannotSendHeader,
        ResponseNotReady,
        BadStatusLine,
    )

    RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

    def __init__(self, auth: discovery.Resource, chunksize: int = -1):
        self.youtube = auth
        self.request = None
        self.chunksize = chunksize
        self.response = None
        self.error = None
        self.retry = 0

    def upload_video(
        self, video: str, properties: dict, progress: callable = None, *args
    ) -> dict:
        self.progress = progress
        self.progress_args = args
        self.video = video
        self.properties = properties

        body = dict(
            snippet=dict(
                title=self.properties.get("title"),
                description=self.properties.get("description"),
                categoryId=self.properties.get("category"),
            ),
            status=dict(privacyStatus=self.properties.get("privacyStatus")),
        )

        media_body = http.MediaFileUpload(
            self.video,
            chunksize=self.chunksize,
            resumable=True,
        )

        self.request = self.youtube.videos().insert(
            part=",".join(body.keys()), body=body, media_body=media_body
        )
        self._resumable_upload()
        return self.response

    def _resumable_upload(self) -> dict:
        response = None
        while response is None:
            try:
                status, response = self.request.next_chunk()
                if response is not None:
                    if "id" in response:
                        self.response = response
                    else:
                        self.response = None
                        raise UploadFailed(
                            "The file upload failed with an unexpected response:{}".format(
                                response
                            )
                        )
            except errors.HttpError as e:
                if e.resp.status in self.RETRIABLE_STATUS_CODES:
                    self.error = "A retriable HTTP error {} occurred:\n {}".format(
                        e.resp.status, e.content
                    )
                else:
                    raise
            except self.RETRIABLE_EXCEPTIONS as e:
                self.error = "A retriable error occurred: {}".format(e)

            if self.error is not None:
                self.retry += 1

                if self.retry > self.MAX_RETRIES:
                    raise MaxRetryExceeded("No longer attempting to retry.")

                max_sleep = 2 ** self.retry
                sleep_seconds = random.random() * max_sleep
                time.sleep(sleep_seconds)
class Uploader:
    def __init__(self, file: str, title: Optional[str] = None):
        self.file = file
        self.title = title
        self.video_category = {
            1: "Film & Animation",
            2: "Autos & Vehicles",
            10: "Music",
            15: "Pets & Animal",
            17: "Sports",
            19: "Travel & Events",
            20: "Gaming",
            22: "People & Blogs",
            23: "Comedy",
            24: "Entertainment",
            25: "News & Politics",
            26: "Howto & Style",
            27: "Education",
            28: "Science & Technology",
            29: "Nonprofits & Activism",
        }

    async def start(self, progress: callable = None, *args) -> Tuple[bool, str]:
        self.progress = progress
        self.args = args

        await self._upload()

        return self.status, self.message

    async def _upload(self) -> None:
        try:
            loop = asyncio.get_running_loop()

            auth = GoogleAuth(CLIENT_ID, CLIENT_SECRET)

            if not os.path.isfile("auth_token.txt"):
                self.status = False
                self.message = "أنت لم تقم بالمصادقة بعد !."
                return

            auth.LoadCredentialsFile("auth_token.txt")
            google = await loop.run_in_executor(None, auth.authorize)
            categoryId = 27
            categoryName = self.video_category[categoryId]
            title = self.title if self.title else os.path.basename(self.file)
            title = (
                (title)
                .replace("<", "")
                .replace(">", "")[:100]
            )
            description = (""+ "\n")[:5000]
            privacyStatus = "private"
            properties = dict(
                title=title,
                description=description,
                category=categoryId,
                privacyStatus=privacyStatus,
            )
            youtube = YouTube(google)
            r = await loop.run_in_executor(
                None, youtube.upload_video, self.file, properties
            )


            video_id = r["id"]
            self.status = True
            self.message = (
                f"[{title}](https://youtu.be/{video_id}) uploaded to YouTube under category "
                f"{categoryId} ({categoryName})"
            )
        except Exception as e:
            self.status = False
            self.message = f"Error occuered during upload.\nError details: {e}"



class AuthCodeInvalidError(Exception):
    pass


class InvalidCredentials(Exception):
    pass


class NoCredentialFile(Exception):
    pass


class GoogleAuth:
    OAUTH_SCOPE = ["https://www.googleapis.com/auth/youtube.upload"]
    REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
    API_SERVICE_NAME = "youtube"
    API_VERSION = "v3"

    def __init__(self, CLIENT_ID: str, CLIENT_SECRET: str):
        self.flow = OAuth2WebServerFlow(
            CLIENT_ID, CLIENT_SECRET, self.OAUTH_SCOPE, redirect_uri=self.REDIRECT_URI
        )
        self.credentials: Optional[OAuth2Credentials] = None

    def GetAuthUrl(self) -> str:
        return self.flow.step1_get_authorize_url()

    def Auth(self, code: str) -> None:
        try:
            self.credentials = self.flow.step2_exchange(code)
        except FlowExchangeError as e:
            raise AuthCodeInvalidError(e)
        except Exception:
            raise

    def authorize(self):
        try:
            if self.credentials:
                http = httplib2.Http()
                self.credentials.refresh(http)
                http = self.credentials.authorize(http)
                return discovery.build(
                    self.API_SERVICE_NAME, self.API_VERSION, http=http
                )
            else:
                raise InvalidCredentials("No credentials!")
        except Exception:
            raise

    def LoadCredentialsFile(self, cred_file: str) -> None:
        if not os.path.isfile(cred_file):
            raise NoCredentialFile(
                "No credential file named {} is found.".format(cred_file)
            )
        storage = Storage(cred_file)
        self.credentials = storage.get()

    def SaveCredentialsFile(self, cred_file: str) -> None:
        storage = Storage(cred_file)
        storage.put(self.credentials)
@bot.on_message( filters.private & filters.incoming & filters.command("authhelp"))
async def _help(bot,message):
    auth = GoogleAuth(CLIENT_ID,CLIENT_SECRET)
    url = auth.GetAuthUrl()
    button = [
            [InlineKeyboardButton(text="Authentication URL", url=url)],
        ]
    await message.reply_text(
        text="الآن قم بتفعيل الـapi",
        reply_markup=InlineKeyboardMarkup(button),
    )


help_callback_filter = filters.create(
    lambda _, __, query: query.data.startswith("help+")
)


@bot.on_message(filters.private & filters.incoming & filters.command("authorise"))
async def _auth(c: bot, m: Message) -> None:
    if len(m.command) == 1:
        await m.reply_text("لم تعطني أي كود !", True)
        return

    code = m.command[1]

    try:
        auth = GoogleAuth(CLIENT_ID, CLIENT_SECRET)

        auth.Auth(code)

        auth.SaveCredentialsFile("auth_token.txt")

        msg = await m.reply_text("تمت المصادقة بنجاح ", True)
        with open("auth_token.txt", "r") as f:
            cred_data = f.read()

    except Exception as e:
        await m.reply_text("فشلت المصادقة للأسف", True)

async def downloadtoserver(x):
 global user_id ,file_path,filename,nom,ex,mp4file,mp3file,m4afile,spdrateaud,mergdir,trimdir,result
 h = await x.download(file_name="./downloads/")
 file_path = h.replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "")
 if file_path == h :
     pass
 else :
     os.rename(x,file_path)
 filename = os.path.basename(file_path)
 nom,ex = os.path.splitext(filename)
 mp4file = f"{nom}.mp4"
 mp3file = f"{nom}.mp3"
 user_id = x.from_user.id
 m4afile = f"{nom}.m4a"
 mergdir = f"./mergy/{mp3file}"
 trimdir = f"./trimmo/{mp3file}"
 result = f"{nom}.txt" 
async def compressaud(rate):
    await downloadtoserver(nepho)
    cmd(f''' ffmpeg -i "{file_path}" -b:a "{rate}" "{mp3file}" -y ''' )
    await bot.send_audio(user_id, mp3file)
    os.remove(file_path) 
    os.remove(mp3file) 
async def amplify(amplemode):
 if exo in audioforms :
        cmd(f'''ffmpeg -i "{file_path}" -filter:a volume={amplemode}dB "{mp3file}"''')
        await bot.send_audio(user_id, mp3file)
        os.remove(file_path) 
        os.remove(mp3file) 
 elif exo in videoforms :
        cmd(f'''ffmpeg -i "{file_path}" -filter:a volume={amplemode}dB "{mp3file}"''')
        cmd(f'''ffmpeg -i "{file_path}" -i "{mp3file}" -c:v copy -map 0:v:0 -map 1:a:0 "{filename}"''')
        await bot.send_video(user_id, filename) 
        os.remove(file_path) 
        os.remove(filename) 
async def convy(k):
   await downloadtoserver(nepho)
   if k == "m4afile" :
       cmd(f'''ffmpeg -i "{file_path}" -c:a aac -b:a 192k "{m4afile}" -y ''')
       await bot.send_audio(user_id, m4afile)
       os.remove(file_path) 
       os.remove(m4afile) 
   elif k == "mp3file" :
      cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3file}" -y ''')
      await  bot.send_audio(user_id, mp3file)
      os.remove(file_path) 
      os.remove(mp3file)
   elif k == "mp4file" :
      cmd(f'''ffmpeg -i "{file_path}" -codec copy "{mp4file}" -y ''')
      await bot.send_video(user_id, mp4file)
      os.remove(file_path) 
      os.remove(mp4file) 
async def spoody(spdrateaud,spdratevid):
    if exo in audioforms :
      cmd(f'''ffmpeg -i "{file_path}" -filter:a "atempo={spdrateaud}" -vn "{mp3file}" -y ''')
      await bot.send_audio(user_id, mp3file) 
      os.remove(file_path) 
      os.remove(mp3file) 
    elif exo in videoforms :
       cmd(f'''ffmpeg -i "{file_path}" -filter_complex "[0:v]setpts={spdratevid}*PTS[v];[0:a]atempo={spdrateaud}[a]" -map "[v]" -map "[a]" "{mp4file}" -y ''')
       await  bot.send_video(user_id,mp4file)
       os.remove(file_path) 
       os.remove(mp4file) 
   
def merge_images1(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    (width1, height1) = image1.size
    (width2, height2) = image2.size
    result_width = max(width1,width2)
    result_height = height1 + height2
    result = Image.new('RGB', (result_width, result_height))
    iso1 = image1.resize((result_width,height1))
    iso2 = image2.resize((result_width,height2))
    result.paste(iso1, box=(0, 0))
    result.paste(iso2, box=(0, height1))
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
    
    [InlineKeyboardButton("تضخيم  ",callback_data="amplifyaud"),InlineKeyboardButton("قص ",callback_data="trim"),InlineKeyboardButton("ضغط ",callback_data="comp")],
    [InlineKeyboardButton("تسريع ",callback_data="speedy"),InlineKeyboardButton("تحويل ",callback_data="conv"),InlineKeyboardButton("تفريغ ",callback_data="transcribe")], 
    [InlineKeyboardButton("دمج  ",callback_data="audmerge"),InlineKeyboardButton("إعادة التسمية ",callback_data="renm")],
    [InlineKeyboardButton("تغيير الصوت",callback_data="voicy"),InlineKeyboardButton("تقسيم الصوتية ",callback_data="splitty"),InlineKeyboardButton("إزالة الصمت",callback_data="rmvsilence")],
    [InlineKeyboardButton("عكس pdf",callback_data="reversepdf"),InlineKeyboardButton("تلوين",callback_data="coloring")],
[InlineKeyboardButton("الرفع لأرشيف",callback_data="upldarch"),InlineKeyboardButton("الرفع ليوتيوب",callback_data="upldtout")],
    [InlineKeyboardButton("ضغط الملفات ",callback_data="zipfile"),InlineKeyboardButton("استخراج",callback_data="unzip")],
    [InlineKeyboardButton(" ترجمة + فيديو",callback_data="vidsrt"),InlineKeyboardButton("تغيير الأبعاد  ",callback_data="vidasp"),InlineKeyboardButton("منتجة فيديو ",callback_data="imagetovid")],
    [InlineKeyboardButton("إبدال صوت الفيديو ",callback_data="subs"),InlineKeyboardButton("صورة إلى gif",callback_data="imagetogif"),InlineKeyboardButton("كتم الصوت ",callback_data="mute")]
    
   
]

PRESS_MERGE_IMAGE = "الآن أرسل الصورة الأخرى و اختر دمج الآن "
PRESS_MERGE_IMAGE_BUTTONS = [
    [InlineKeyboardButton("دمج الآن ",callback_data="imagemergenow")]
     ]

YOUR_COLOR_MODE = "اختر نمط التلوين"
YOUR_COLOR_MODE_BUTTONS = [
    [InlineKeyboardButton("رمادي",callback_data="Grayscale")],
    [InlineKeyboardButton("أحمر",callback_data="red")],
    [InlineKeyboardButton("أخضر",callback_data="green")],
    [InlineKeyboardButton("أصفر",callback_data="yellow")],
    [InlineKeyboardButton("أزرق فاتح",callback_data="whiteblue")],
    [InlineKeyboardButton("أرجواني",callback_data="purple")]
     ]
PRESS_ZIP_FILE = "بعد الانتهاء من إرسال الملفات , اضغط تحويل الآن "
PRESS_ZIP_FILE_BUTTONS = [
    [InlineKeyboardButton("تحويل الآن",callback_data="zipnow")]
     ]
CHOOSE_UR_VIDMERGE_MODE = "الآن أرسل الفيديوهات الأخرى و اختر دمج الآن "
CHOOSE_UR_VIDMERGE_MODE_BUTTONS= [
    [InlineKeyboardButton("دمج الآن ",callback_data="vidmergenow")]
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


@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت متعدد الاستعمالات , فقط أرسل الفيديو أو الصوتية أو الملف هنا\n\n [طريقة استعمال البوت](https://telegra.ph/%D8%B7%D8%B1%D9%8A%D9%82%D8%A9-%D8%A7%D8%B3%D8%AA%D8%B9%D9%85%D8%A7%D9%84-%D8%A7%D9%84%D8%A8%D9%88%D8%AA-01-20) \n\n [لبقية البوتات](https://t.me/sunnay6626/2) ",disable_web_page_preview=True)

@bot.on_message(filters.command('setbucket') & filters.text & filters.private)
def command9(bot,message):
  global bucketname
  bucketname = message.text.split("setbucket", maxsplit=1)[1]
  bucketname = bucketname.replace(" ", "")
  message.reply_text("تم ضبط المعرف ")

@bot.on_message(filters.command('ytsub') & filters.text & filters.private)
def command20(bot,message):
     dlmode = message.text.split(" ")[-1] 
     ytlink = message.text.split("ytsub", maxsplit=1)[1].replace(" ", "")
     yt_id = message.from_user.id
     with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{ytlink}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "")
        subfile = f"{video_title}.txt"
     srt = YouTubeTranscriptApi.get_transcript(video_id,languages=['ar'])
     with open(subfile, "w") as f:
            for i in srt:
             f.write(f" {i['text']} ")
     bot.send_document(yt_id,subfile)
     os.remove(subfile)
        

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
     try : 
      for i in range(1,numbofvid):
         cmd(f'sed -n {i}p yttransy.txt > "{temptxt}"')
         with open(temptxt, 'r') as file:
           link = file.read().rstrip('\n')  
         with YoutubeDL() as ydl: 
          info_dict = ydl.extract_info(f'{link}', download=False)
          video_url = info_dict.get("url", None)
          video_id = info_dict.get("id", None)
          video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "") 
          subfile = f"{video_title}.txt"
         srt = YouTubeTranscriptApi.get_transcript(video_id,languages=['ar'])
         with open(subfile, "w") as f:
            for i in srt:
             f.write(f" {i['text']} ")
         bot.send_document(yttransyid,subfile)
         os.remove(subfile)
      os.remove("yttransy.txt")
  
     except FileNotFoundError :
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
    shutil.rmtree("./vidmerge/")
    shutil.rmtree("./vidmerge2/")
    shutil.rmtree("./downloads/")
    audmergelist.clear()
    vidmergelist.clear()


    ########### الوظائف الرئيسية ###########

@bot.on_message(filters.private & filters.incoming & filters.voice | filters.audio | filters.video | filters.document | filters.photo | filters.animation )
async def _telegram_file(client, message):
 if len(queeq) == 0 : 
    pass
 else :
    await asyncio.sleep(30)
    queeq.clear()
    pass
 queeq.append(message.from_user.id)
 global  replo,nepho,temponame,nomo,exo
 nepho = message
 #print(nepho)
 if nepho.photo :
  nomo = nepho.photo.file_unique_id
  exo = ".jpg"
 elif nepho.voice :
  nomo = nepho.voice.file_unique_id
  exo = ".ogg"
 elif nepho.audio : 
  temponame = nepho.audio.file_name
  nomo,exo = os.path.splitext(temponame)
 elif nepho.video : 
  nomo = nepho.video.file_unique_id
  exo = ".mp4"
 elif nepho.document  : 
  temponame = nepho.document.file_name
  nomo,exo = os.path.splitext(temponame)
 replo = await nepho.reply(text = CHOOSE_UR_AUDIO_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AUDIO_MODE_BUTTONS))
 
 @bot.on_callback_query()
 async def callback_query(CLIENT,CallbackQuery): 

########## خواص التضخيم ###########

  if CallbackQuery.data == "amplifyaud":
     await CallbackQuery.edit_message_text(text = CHOOSE_UR_AMPLE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AMPLE_MODE_BUTTONS))
  elif CallbackQuery.data == "mod1":
      await CallbackQuery.edit_message_text("جار التضخيم ")
      await downloadtoserver(nepho)
      await amplify(5)
      await CallbackQuery.edit_message_text("تم التضخيم ✅  ")
      queeq.clear()   
     

  elif CallbackQuery.data == "mod2":
      await CallbackQuery.edit_message_text("جار التضخيم ")
      await downloadtoserver(nepho)
      await amplify(10)
      await CallbackQuery.edit_message_text("تم التضخيم ✅  ")
      queeq.clear()   
      
  elif CallbackQuery.data == "mod3":
      await CallbackQuery.edit_message_text("جار التضخيم ")
      await downloadtoserver(nepho)
      await amplify(15)
      await CallbackQuery.edit_message_text("تم التضخيم ✅  ") 
      queeq.clear()  

  elif CallbackQuery.data == "mod4" :
      await CallbackQuery.edit_message_text("جار التضخيم ")
      await downloadtoserver(nepho)
      await amplify(20)
      await CallbackQuery.edit_message_text("تم التضخيم ✅  ")
      queeq.clear()   

  elif CallbackQuery.data == "mod5":
      await CallbackQuery.edit_message_text("جار التضخيم ")
      await downloadtoserver(nepho)
      await amplify(25)
      await CallbackQuery.edit_message_text("تم التضخيم ✅  ") 
      queeq.clear()  


 ########## خواص الضغط ###########

  
  elif CallbackQuery.data == "comp":
   await CallbackQuery.edit_message_text("معالجة ⏱️")
   if exo == ".pdf":
      await downloadtoserver(nepho)
      await CallbackQuery.edit_message_text("جار الضغط")
      PDFNet.Initialize("demo:1676040759361:7d2a298a03000000006027df7c81c9e05abce088e7286e8312e5e06886"); doc = PDFDoc(f"{file_path}")
      doc.InitSecurityHandler()
      Optimizer.Optimize(doc)
      doc.Save(f"{filename}", SDFDoc.e_linearized)
      doc.Close()
      await bot.send_document(user_id, filename)
      await CallbackQuery.edit_message_text("تم الضغط ✅  ")   
      os.remove(file_path) 
      os.remove(filename)
      queeq.clear() 
   elif exo in videoforms:
    await downloadtoserver(nepho)
    cmd(f'''ffmpeg -y -i "{file_path}" -vf "setpts=1*PTS" -r 10 "{mp4file}"''')
    await bot.send_video(user_id,mp4file)
    await CallbackQuery.edit_message_text("تم الضغط ✅  ")   
    os.remove(mp4file)
    os.remove(file_path)
    queeq.clear()
   elif exo in audioforms:
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_COMP_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_COMP_MODE_BUTTONS) )
  elif  CallbackQuery.data == "compmod1":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    await compressaud("10k")
    await CallbackQuery.edit_message_text("تم الضغط ✅  ") 
    queeq.clear()  

  elif  CallbackQuery.data == "compmod2":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    await compressaud("20k")
    await CallbackQuery.edit_message_text("تم الضغط ✅  ") 
    queeq.clear()  

  elif  CallbackQuery.data == "compmod3":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    await compressaud("30k") 
    await CallbackQuery.edit_message_text("تم الضغط ✅  ") 
    queeq.clear()  

  elif  CallbackQuery.data == "compmod4":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    await compressaud("40k")
    await CallbackQuery.edit_message_text("تم الضغط ✅  ")
    queeq.clear()

  elif  CallbackQuery.data == "compmod5":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    await compressaud("50k")
    await CallbackQuery.edit_message_text("تم الضغط ✅  ")   
    queeq.clear()

 ########## خاصية التسريع  ###########
       
  elif CallbackQuery.data == "speedy":
    await CallbackQuery.edit_message_text("معالجة ⏱️")
    await downloadtoserver(nepho)
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_SPEED_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SPEED_MODE_BUTTONS))
  elif CallbackQuery.data == "spd1":
   await CallbackQuery.edit_message_text("جار التسريع")
   await spoody(0.8,1.25)
   await CallbackQuery.edit_message_text("تم التسريع ✅  ") 
   queeq.clear()  

  elif CallbackQuery.data == "spd2":
    await CallbackQuery.edit_message_text("جار التسريع")
    await spoody(1.5,0.66666666666)
    await CallbackQuery.edit_message_text("تم التسريع ✅  ") 
    queeq.clear()
  elif CallbackQuery.data == "spd3":
    await CallbackQuery.edit_message_text("جار التسريع")
    await spoody(1.75,0.57142857142)
    await CallbackQuery.edit_message_text("تم التسريع ✅  ") 
    queeq.clear()
  elif CallbackQuery.data == "spd4":
    await CallbackQuery.edit_message_text("جار التسريع")
    await spoody(2,0.5) 
    await CallbackQuery.edit_message_text("تم التسريع ✅  ") 
    queeq.clear()

  


 ########## خواص التحويل ###########

  elif CallbackQuery.data == "conv" :
    await CallbackQuery.edit_message_text("معالجة ⏱️")
    if exo in imageforms :
      await downloadtoserver(nepho)
      imagepdfdic1.append(file_path)
      global imagey
      imagey = Image.open(imagepdfdic1[0]).convert('RGB')
      if len(imagepdfdic1) > 1 :
       image2 = Image.open(file_path).convert('RGB')
       imagepdfdic.append(image2)
      await CallbackQuery.edit_message_text(text = THE_LAST_IMAGE,reply_markup = InlineKeyboardMarkup(THE_LAST_IMAGE_BUTTONS))
    else :
     await CallbackQuery.edit_message_text(text = CHOOSE_UR_CONV_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_CONV_MODE_BUTTONS))
    queeq.clear() 
  elif CallbackQuery.data == "audconv" :
   await CallbackQuery.edit_message_text("جار التحويل ") 
   await convy("mp3file")
   await CallbackQuery.edit_message_text("تم التحويل ✅  ") 
   queeq.clear()

  elif CallbackQuery.data == "audconvm4a" :
   await CallbackQuery.edit_message_text("جار التحويل ") 
   await convy("m4afile")
   await CallbackQuery.edit_message_text("تم التحويل ✅  ") 
   queeq.clear()
   
  elif CallbackQuery.data == "vidconv" :
   await CallbackQuery.edit_message_text("جار التحويل ") 
   await convy("mp4file")
   await CallbackQuery.edit_message_text("تم التحويل ✅  ") 
   queeq.clear()


  elif CallbackQuery.data == "convnow" :
    pdffile = f"{nom}.pdf"
    imagey.save(pdffile,save_all=True, append_images=imagepdfdic)
    await bot.send_document(user_id,pdffile)
    await CallbackQuery.edit_message_text("تم التحويل ✅  ") 
    os.remove(pdffile)
    for x in range(0,len(imagepdfdic1)) :
      os.remove(str(imagepdfdic1[x]))
    imagepdfdic1.clear()
    imagepdfdic.clear()
    queeq.clear()


 ########## خاصية تغيير الصوت ###########

  elif  CallbackQuery.data == "voicy":  
    await CallbackQuery.edit_message_text("جار تغيير الصوت ") 
    if exo in audioforms :
     await downloadtoserver(nepho)
     cmd(f'''ffmpeg -i "{file_path}" -af asetrate=44100*0.75,aresample=44100,atempo=4/3 "{mp3file}"''')
     await bot.send_audio(user_id, mp3file)
    elif exo in videoforms :
       await downloadtoserver(nepho)
       cmd(f'''ffmpeg -i "{file_path}" -af asetrate=44100*0.75,aresample=44100,atempo=4/3 "{mp3file}"''')
       cmd(f'''ffmpeg -i "{file_path}" -i "{mp3file}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
       await bot.send_video(user_id,mp4file)
       os.remove(mp4file)
    await CallbackQuery.edit_message_text("تم تحويل الصوت ✅  ") 
    os.remove(file_path) 
    os.remove(mp3file) 
    queeq.clear()


 ########## إبدال صوت الفيديو ###########

  elif  CallbackQuery.data == "subs":
      await CallbackQuery.edit_message_text("معالجة ⏱️")
      if exo in videoforms and len(vidsubslist) == 0 :
         await downloadtoserver(nepho)
         vidsubslist.append(file_path)
         await CallbackQuery.edit_message_text("الآن أرسل الصوتية")
      elif exo in videoforms and len(vidsubslist) == 1 :
       await downloadtoserver(nepho)
       await CallbackQuery.edit_message_text("جار الإبدال ") 
       cmd(f'''ffmpeg -i "{file_path}" -i "{vidsubslist[0]}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
       await bot.send_video(user_id, mp4file)
       await CallbackQuery.edit_message_text("تم الإبدال ✅  ") 
       os.remove(file_path) 
       os.remove(mp4file) 
       os.remove(vidsubslist[0]) 
       vidsubslist.clear()
      elif exo in audioforms and len(vidsubslist) == 0 :
        await downloadtoserver(nepho)
        vidsubslist.append(file_path)
        await CallbackQuery.edit_message_text("الآن أرسل الفيديو")
      elif exo in audioforms and len(vidsubslist) == 1 :
       await downloadtoserver(nepho)
       await CallbackQuery.edit_message_text("جار الإبدال ") 
       cmd(f'''ffmpeg -i "{vidsubslist[0]}" -i "{file_path}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
       await bot.send_video(user_id, mp4file)
       await CallbackQuery.edit_message_text("تم الإبدال ✅  ")
       os.remove(file_path) 
       os.remove(mp4file) 
       os.remove(vidsubslist[0]) 
       vidsubslist.clear()
      queeq.clear()


  ########## خاصية المنتجة  ###########

  elif  CallbackQuery.data == "imagetovid":
     await CallbackQuery.edit_message_text("معالجة ⏱️")
     if (exo in imageforms) and len(montaglist) == 0 :
      await downloadtoserver(nepho)
      montaglist.append(file_path)
      await CallbackQuery.edit_message_text("الآن أرسل الصوتية") 
     elif (exo in imageforms) and len(montaglist) == 1 :
      await CallbackQuery.edit_message_text("جار المنتجة") 
      await downloadtoserver(nepho)
      cmd(f'''ffmpeg -i "{montaglist[0]}" -q:a 0 -map a "{mp3file}" -y ''')
      cmd(f'''ffmpeg -r 1 -loop 1 -y -i  "{file_path}" -i "{mp3file}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 "{mp4file}"''')
      await bot.send_video(user_id, mp4file)
      await CallbackQuery.edit_message_text("تمت المنتجة  ✅  ")
      os.remove(file_path) 
      os.remove(mp4file)
      os.remove(mp3file) 
      os.remove(montaglist[0]) 
      montaglist.clear()
     elif exo in audioforms and len(montaglist) == 0 :
      await downloadtoserver(nepho)
      montaglist.append(file_path)
      await CallbackQuery.edit_message_text("الآن أرسل الصورة") 
     elif exo in audioforms and len(montaglist) == 1 :
      await CallbackQuery.edit_message_text("جار المنتجة") 
      await downloadtoserver(nepho)
      cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3file}" -y ''')
      cmd(f'''ffmpeg -r 1 -loop 1 -y -i  "{montaglist[0]}" -i "{mp3file}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 "{mp4file}"''')
      await bot.send_video(user_id, mp4file)
      await CallbackQuery.edit_message_text("تمت المنتجة  ✅  ")
      os.remove(file_path) 
      os.remove(mp4file)
      os.remove(mp3file) 
      os.remove(montaglist[0])
      montaglist.clear()
     queeq.clear()



 ########## خواص القص ###########

  elif CallbackQuery.data == "trim" :
    await CallbackQuery.edit_message_text("معالجة ⏱️")
    await replo.delete()
    if exo == ".pdf":
      await nepho.reply_text(" الآن أرسل نقطة البداية والنهاية بهذه الصورة \n start-end ",reply_markup=ForceReply(True))
    else :
      await nepho.reply_text("الآن أرسل نقطة البداية والنهاية بهذه الصورة \n\n hh:mm:ss/hh:mm:ss",reply_markup=ForceReply(True))
  elif CallbackQuery.data == "normaltrim" :
    if exo in audioforms :
       await CallbackQuery.edit_message_text("جار القص")  
       await downloadtoserver(nepho)
       cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "trim{mp3file}" -y ''')
       cmd(f'''ffmpeg -i "trim{mp3file}" -ss {strt_point} -to {end_point} -c copy "{mp3file}" -y ''')
       await  bot.send_audio(user_id, mp3file)
       await CallbackQuery.edit_message_text("تم القص  ✅  ")
       os.remove(file_path) 
       os.remove(mp3file) 
       os.remove(f"trim{mp3file}")
    elif exo in videoforms :
      await CallbackQuery.edit_message_text("جار القص")  
      await downloadtoserver(nepho)
      cmd(f'''ffmpeg -i "{file_path}" -ss {strt_point} -strict -2 -to {end_point} -c:a aac -codec:v h264 -b:v 1000k "{mp4file}" -y ''')
      await bot.send_video(user_id, mp4file)  
      await CallbackQuery.edit_message_text("تم القص  ✅  ") 
      os.remove(file_path) 
      os.remove(mp4file) 
    queeq.clear()
  elif CallbackQuery.data == "reversetrim" :
     await CallbackQuery.edit_message_text("جار القص  ")
     await downloadtoserver(nepho)
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
     await CallbackQuery.edit_message_text("تم القص  ✅  ")
     os.remove(mp3file)
     os.remove(file_path)
     queeq.clear()
  
  
 ########## خاصية إعادة التسمية ###########

  elif CallbackQuery.data == "renm":
    await replo.delete()
    await nepho.reply_text("الآن أدخل الاسم الجديد ",reply_markup=ForceReply(True))

 ########## خاصية التفريغ  ###########
  
  elif CallbackQuery.data == "transcribe":
   await CallbackQuery.edit_message_text("معالجة ⏱️")
   await downloadtoserver(nepho)
   if exo in audioforms or exo in videoforms :
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
   elif  exo == ".pdf":
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
    await CallbackQuery.edit_message_text("تم التفريغ  ✅  ")
    shutil.rmtree('./temp/') 
    os.remove(result)
   elif  exo in imageforms :
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
    await CallbackQuery.edit_message_text("تم التفريغ  ✅  ")
    os.remove(file_path) 
   queeq.clear()

 ########## خاصية كتم الفيديو ###########

  elif CallbackQuery.data == "mute":
    await CallbackQuery.edit_message_text("معالجة ⏱️")
    await downloadtoserver(nepho)
    await CallbackQuery.edit_message_text("جار الكتم")
    cmd(f'''ffmpeg -i "{file_path}" -c copy -an "{mp4file}"''')
    await bot.send_document(user_id, mp4file)
    await CallbackQuery.edit_message_text("تم الكتم  ✅  ")
    os.remove(file_path) 
    os.remove(mp4file) 
    queeq.clear()

 ##########  خواص الدمج ###########


  elif CallbackQuery.data == "audmerge":
    await CallbackQuery.edit_message_text("معالجة ⏱")
    if exo in audioforms:
     await CallbackQuery.edit_message_text("جار الإضافة ")
     audmergelist.append(nepho)
     await CallbackQuery.edit_message_text(text = CHOOSE_UR_MERGE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MERGE_BUTTONS))
    elif exo in videoforms : 
     vidmergelist.append(nepho)
     await CallbackQuery.edit_message_text(text = CHOOSE_UR_VIDMERGE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_VIDMERGE_MODE_BUTTONS))
    elif exo in imageforms:
     imagedic.append(file_path)
     await CallbackQuery.edit_message_text(text = PRESS_MERGE_IMAGE,reply_markup = InlineKeyboardMarkup(PRESS_MERGE_IMAGE_BUTTONS))
    elif exo == ".pdf":
      pdfqueemerge.append(nepho)
      await CallbackQuery.edit_message_text(text = CHOOSE_UR_PDFMERGE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_PDFMERGE_MODE_BUTTONS))
    queeq.clear()  

  elif CallbackQuery.data == "mergenow":
    await CallbackQuery.edit_message_text("جار الدمج") 
    cmd(f'''mkdir mergy''')
    for x in range(0,len(audmergelist)) :
     await downloadtoserver(audmergelist[x])
     tempmp3 = f"{random.randint(1,1000)}{ex}"
     os.replace(file_path,tempmp3)
     mp3merge = f"./mergy/{random.randint(0,1000)}.mp3"
     cmd(f'''ffmpeg -i "{tempmp3}" -q:a 0 -map a "{mp3merge}" -y ''')
     os.remove(tempmp3)
     with open('list.txt','a') as f:
      f.write(f'''file '{mp3merge}' \n''')
    cmd(f'''ffmpeg -f concat -safe 0 -i list.txt "{mp3file}" -y ''')
    await bot.send_audio(user_id, mp3file)
    await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
    os.remove("list.txt")
    os.remove(mp3file)
    shutil.rmtree('./mergy/') 
    audmergelist.clear()
    queeq.clear()
  
  elif CallbackQuery.data == "pdfmergenow":
      await CallbackQuery.edit_message_text("جار الدمج")
      for x in range(0,len(pdfqueemerge)):
       await downloadtoserver(pdfqueemerge[x])
       pdfdir = f"pdfmerge/{filename}"
       cmd("mkdir pdfmerge")
       cmd(f'''mv "{file_path}" ./pdfmerge/''')
       with open('pdfy.txt','a') as f:
        f.write(f'''{pdfdir} \n''')
      pdfqueemerge.clear()  
      pdfs = []
      with open("pdfy.txt", "r") as file:
       for line in file:
        pdfs.append(line.strip())
      merger = PdfMerger()
      for pdf in pdfs:
       merger.append(pdf)
      pdfmerged = filename
      merger.write(pdfmerged)
      merger.close()
      await  bot.send_document(user_id,pdfmerged)
      await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
      shutil.rmtree("./pdfmerge/")
      os.remove(pdfmerged);os.remove("pdfy.txt")
      queeq.clear()

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
     await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
     for x in range(0,len(imagedic)) :
      os.remove(str(imagedic[x]))
     imagedic.clear()
     os.remove(output_img)
     queeq.clear()

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
     await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
     for x in range(0,len(imagedic)) :
      os.remove(str(imagedic[x]))
     imagedic.clear()
     os.remove(output_img)
     queeq.clear()

  elif  CallbackQuery.data == "vidmergenow" :
     await CallbackQuery.edit_message_text("جار الدمج")
     for x in range(0,len(vidmergelist)):
        await downloadtoserver(vidmergelist[x])
        cmd("mkdir data")
        tempmp4file = f"./data/{mp4file}"
        os.rename(file_path,tempmp4file)
        vidmergelist[x] = tempmp4file
     for x in range(1,len(vidmergelist)):
        cmd(f'''ffmpeg -i "{vidmergelist[0]}" -i "{vidmergelist[1]}"  -filter_complex "[0]scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1[v0];[1]scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1[v1];[v0][0:a:0][v1][1:a:0]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" "mod.mp4"''') 
        os.rename("mod.mp4",mp4file)
        if len(vidmergelist) > 2:
         vidmergelist.remove(vidmergelist[0])
         vidmergelist.remove(vidmergelist[0])
         vidmergelist.insert(0,mp4file)

     await bot.send_video(user_id,mp4file)
     await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
     shutil.rmtree("./data/")
     os.remove(mp4file)
     vidmergelist.clear()
     queeq.clear()   

      ###### خاصية التقسيم #######

  elif CallbackQuery.data == "splitty":
    await CallbackQuery.edit_message_text("جار التقسيم")
    await downloadtoserver(nepho)
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
    await CallbackQuery.edit_message_text("تم التقسيم  ✅  ")
    os.remove("mod.mp3") 
    os.remove(file_path) 
    queeq.clear()


    ########## خاصية الرفع لأرشيف
  
  elif CallbackQuery.data == "upldarch":
      if nepho.from_user.id==6234365091 :
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         await downloadtoserver(nepho)
         await CallbackQuery.edit_message_text("جار الرفع")
         cmd(f'''rclone copy "{file_path}" 'myarchive':"{bucketname}"''')
         os.remove(file_path)
         await CallbackQuery.edit_message_text("تم الرفع  ✅  ")
      else :
         await CallbackQuery.edit_message_text("هذه الميزة متوفرة لمالك البوت فقط")
      queeq.clear()

##### تغيير أبعاد الفيديو ######
  
  elif CallbackQuery.data == "vidasp":
    await CallbackQuery.edit_message_text("معالجة ⏱️")
    await downloadtoserver(nepho)
    if exo in videoforms:
     await CallbackQuery.edit_message_text(text = CHOOSE_UR_VIDRES_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_VIDRES_MODE_BUTTONS))
   # elif ex == ".png" or ex == ".jpg":
    #  await replo.delete()
     # await nepho.reply_text("الآن أدخل أبعاد الصورة الجديدة بهذه الصورة \n lenght:width ",reply_markup=ForceReply(True))

  elif CallbackQuery.data == "vidresnow11":
    await  CallbackQuery.edit_message_text("جار التحويل")
    cmd(f'''ffmpeg -i "{file_path}" -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1:color=black" "{mp4file}"''')
    await bot.send_document(user_id,mp4file) 
    await CallbackQuery.edit_message_text("تم التحويل   ✅  ")
    os.remove(mp4file)
    os.remove(file_path)
    queeq.clear()

  elif CallbackQuery.data == "vidresnow169":
    await  CallbackQuery.edit_message_text("جار التحويل")
    cmd(f'''ffmpeg -i "{file_path}" -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:-1:-1:color=black" "{mp4file}"''')
    await bot.send_video(user_id,mp4file) 
    await CallbackQuery.edit_message_text("تم التحويل  ✅  ")
    os.remove(mp4file)
    os.remove(file_path)
    queeq.clear()

########### خاصية إزالة الصمت ##########

  elif CallbackQuery.data == "rmvsilence" :
   await  CallbackQuery.edit_message_text("جار إزالة الصمت")
   await downloadtoserver(nepho)
   cmd(f'''ffmpeg -i "{file_path}" -af "silenceremove=start_periods=1:stop_periods=-1:start_threshold=-30dB:stop_threshold=-50dB:start_silence=2:stop_silence=2" "{mp3file}"''')
   await bot.send_audio(user_id,mp3file)
   await CallbackQuery.edit_message_text("تمت إزالة الصمت  ✅  ")
   os.remove(file_path)
   os.remove(mp3file)
   queeq.clear()

   ######## تحويل الصورة إلى gif##########
 
  elif CallbackQuery.data == "imagetogif" :
      await replo.delete()
      await nepho.reply_text("الآن أرسل مدة الفيديو بالثانية بهذه الصورة \n t=المدة",reply_markup=ForceReply(True))

      ######### ترجمة + فيديو ############
  
  elif CallbackQuery.data == "vidsrt" :
     await CallbackQuery.edit_message_text("معالجة ⏱️")
     await downloadtoserver(nepho)
     if (len(vidsrt) == 0 or len(vidsrt) > 2 ) and (exo == ".ass" or exo == ".srt") :
        vidsrt.clear()
        vidsrt.append(file_path)
        await CallbackQuery.edit_message_text("الآن أرسل الفيديو")
     elif (len(vidsrt) == 0 or len(vidsrt) > 2 ) and (exo in videoforms) :
        vidsrt.clear()
        vidsrt.append(file_path)
        await CallbackQuery.edit_message_text("الآن أرسل ملف الترجمة")

     elif (len(vidsrt) == 1) and (exo in videoforms ) :  
        await CallbackQuery.edit_message_text("جار الدمج ⏱️")
        subfile = vidsrt[0]
        vidfile = file_path
        cmd(f'''ffmpeg -i "{vidfile}" -filter_complex subtitles='{subfile}' -c:a copy "{mp4file}"''')
        await bot.send_video(user_id,mp4file)
        await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
        os.remove(subfile)
        os.remove(vidfile)
        os.remove(mp4file)
        vidsrt.clear()
     elif (len(vidsrt) == 1) and (exo == ".ass" or exo == ".srt") : 
        await CallbackQuery.edit_message_text("جار الدمج ⏱️")
        subfile = file_path
        vidfile = vidsrt[0]
        cmd(f'''ffmpeg -i "{vidfile}" -filter_complex subtitles='{subfile}' -c:a copy "{mp4file}"''')
        await bot.send_video(user_id,mp4file)
        await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
        os.remove(subfile)
        os.remove(vidfile)
        os.remove(mp4file)
        vidsrt.clear()
     queeq.clear()
  
  ######### خاصية عكس الـpdf  #########

  
  elif  CallbackQuery.data == "reversepdf" :
    await CallbackQuery.edit_message_text("جار العكس")
    await downloadtoserver(nepho)
    cmd('mkdir rvtemp')
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
        optimise_mode=pdfium.OptimiseMode.NONE,)
     pil_image.save(f"./rvtemp/image_{page_number+1}.png")
    os.remove(file_path)
    rpdfpage = [] 
    for x in range(1,n_pages+1):
      page=f"./rvtemp/image_{x}.png"
      rpdfpage.append(page)
    rpdfpage.reverse()
    imagey = Image.open(rpdfpage[0]).convert('RGB')
    for x in range(1,len(rpdfpage)):
     image2 = Image.open(rpdfpage[x]).convert('RGB')
     imagepdfdic.append(image2)
    pdffile = f"{nom}.pdf"
    imagey.save(pdffile,save_all=True, append_images=imagepdfdic)
    await bot.send_document(user_id,pdffile)
    await CallbackQuery.edit_message_text("تم العكس  ✅  ")
    os.remove(pdffile)
    shutil.rmtree("./rvtemp/")
    imagepdfdic.clear()
    rpdfpage.clear()
    queeq.clear()
  elif  CallbackQuery.data == "coloring" :
   await CallbackQuery.edit_message_text(text = YOUR_COLOR_MODE,reply_markup = InlineKeyboardMarkup(YOUR_COLOR_MODE_BUTTONS))

  elif  CallbackQuery.data == "Grayscale" :
   await CallbackQuery.edit_message_text("جار التلوين")
   await downloadtoserver(nepho)
   await Coloringfunc("g")
   await CallbackQuery.edit_message_text("تم التلوين ✅  ") 
   queeq.clear()
  elif  CallbackQuery.data == "red" :
   await CallbackQuery.edit_message_text("جار التلوين")
   await downloadtoserver(nepho)
   await Coloringfunc("r")
   await CallbackQuery.edit_message_text("تم التلوين ✅  ") 
   queeq.clear()
  elif  CallbackQuery.data == "yellow" :
   await CallbackQuery.edit_message_text("جار التلوين")
   await downloadtoserver(nepho)
   await Coloringfunc("y")
   await CallbackQuery.edit_message_text("تم التلوين ✅  ") 
   queeq.clear()
  elif  CallbackQuery.data == "purple" :
   await CallbackQuery.edit_message_text("جار التلوين")
   await downloadtoserver(nepho)
   await Coloringfunc("p")
   await CallbackQuery.edit_message_text("تم التلوين ✅  ") 
   queeq.clear()
  elif  CallbackQuery.data == "whiteblue" :
   await CallbackQuery.edit_message_text("جار التلوين")
   await downloadtoserver(nepho)
   await Coloringfunc("b")
   await CallbackQuery.edit_message_text("تم التلوين ✅  ") 
   queeq.clear()




    ############  خاصية الأرشفة ######## 

  elif  CallbackQuery.data == "zipfile" :
    await CallbackQuery.edit_message_text("معالجة ⏱️")
    await downloadtoserver(nepho)
    cmd('mkdir zipdir')
    mergeviditem = f"./zipdir/{filename}"
    os.rename(file_path,mergeviditem)
    await CallbackQuery.edit_message_text(text =PRESS_ZIP_FILE,reply_markup = InlineKeyboardMarkup(PRESS_ZIP_FILE_BUTTONS))
  elif  CallbackQuery.data == "zipnow" :
    await CallbackQuery.edit_message_text("جار الأرشفة  ⏱️  ")
    zipfile = f"{nom}.zip"
    shutil.make_archive(nom, 'zip', './zipdir/')
    await bot.send_document(user_id,zipfile)
    await CallbackQuery.edit_message_text("تمت الأرشفة  ✅  ")
    os.remove(zipfile)
    shutil.rmtree("./zipdir/")
    queeq.clear()

    ############خواص الاستخراج ###########

  elif  CallbackQuery.data == "unzip" :
   await CallbackQuery.edit_message_text("جار الاستخراج ⏱️")
   await downloadtoserver(nepho)
   unzippath = "./unzipprocess/"
   cmd(f'mkdir "{unzippath}"')
   if ex == ".zip":
     with ZipFile(file_path, 'r') as zObject: 
      zObject.extractall(path=unzippath) 
     files = os.listdir(unzippath)
     for x in range(0,len(files)):
      sentfile = f"{unzippath}{files[x]}"
      tempnom,tempex = os.path.splitext(files[x])
      itsextension = tempex
      if itsextension == ".mp3" or itsextension == ".m4a" or itsextension == ".ogg":
        await bot.send_audio(user_id,sentfile)
      elif itsextension == ".mp4" or itsextension == ".mkv" :
        await bot.send_video(user_id,sentfile)
      elif itsextension == ".jpg" or itsextension == ".png" :
        await bot.send_photo(user_id,sentfile)
      else :
          await bot.send_document(user_id,sentfile)
     shutil.rmtree(unzippath)  
   elif ex == ".pdf":
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
     pil_image.save(f"{unzippath}image_{page_number+1}.png")
    os.remove(file_path) 
    images = os.listdir(unzippath)
    for x in range(0,len(images)):
      sentfile = f"{unzippath}{images[x]}"
      await bot.send_document(user_id,sentfile)
    shutil.rmtree(unzippath)
   elif ex == ".epub":
       parsed = parser.from_file(file_path)
       textfile = f"{nom}.txt"
       finaltext = parsed['content'].replace('\n',' ')
       with open(textfile, "a") as f:     
        f.write(f" {finaltext} ")
       await bot.send_document(user_id,textfile)
       os.remove(textfile)
       os.remove(file_path)
      
   await CallbackQuery.edit_message_text("تم الاستخراج  ✅  ")
   queeq.clear()

    ############ خاصية الرفع ليوتيوب ###########

  elif  CallbackQuery.data == "upldtout" :
    if nepho.from_user.id ==6234365091 :
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         await downloadtoserver(nepho)
         videoupldtitle = nepho.caption
         upload = Uploader(file_path,videoupldtitle )
         snt = await CallbackQuery.edit_message_text("جار الرفع")
         link = await upload.start(progress,snt)
         await snt.edit_text(text=link, parse_mode=enums.ParseMode.MARKDOWN)
         os.remove(file_path)
    else :
         await CallbackQuery.edit_message_text("هذه الميزة متوفرة لمالك البوت فقط")
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
          queeq.clear()

 @bot.on_message(filters.private & filters.reply & filters.regex('/'))
 async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          endstart = message.text 
          tempid = message.from_user.id
          msgid = message.reply_to_message_id
          await bot.delete_messages(tempid,msgid)
          await message.delete()
          global strt_point
          global end_point
          strt, end = os.path.split(endstart);strt_point=strt 
          end_point = end
          await message.reply(text = CHOOSE_UR_TRIMMODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_TRIMMODE_BUTTONS))
          queeq.clear()
 @bot.on_message(filters.private & filters.reply & filters.regex("-"))
 async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          await downloadtoserver(nepho)
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
          queeq.clear()
 @bot.on_message(filters.private & filters.reply )
 async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          newname = message.text 
          await downloadtoserver(nepho)
          msgid = message.reply_to_message_id
          await bot.delete_messages(user_id,msgid)
          await message.delete()
          global newfile
          newfile = f"{newname}{ex}"
          os.rename(file_path,newfile)
          if exo in audioforms :
            await bot.send_audio(user_id,newfile)
          elif exo in videoforms  :
            await bot.send_video(user_id,newfile)
          elif exo in imageforms :
            await bot.send_photo(user_id,newfile)
          else : 
             await bot.send_document(user_id,newfile)
          os.remove(newfile)
          queeq.clear()





        
bot.run()
