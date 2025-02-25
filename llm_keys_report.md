# LLM API Key Findings Report

Scan Date: 2025-02-25 11:52:48

## Summary

- Total repositories scanned: 360
- Repositories with LLM API keys: 79
- Total LLM API keys found: 88
- Valid LLM API keys: 0
- Invalid LLM API keys: 88

**Note:** This report was generated in test mode.

## Key Types Found

- Unknown LLM API: 1 total, 0 valid
- OpenAI API: 16 total, 0 valid
- Google Gemini/PaLM API: 70 total, 0 valid
- Cohere API: 1 total, 0 valid

## Detailed Findings

### catsanzsh/GPTPrompts

**File:** GPT-X.md

- [❌ Invalid] Unknown LLM API key (redacted: your...here)
  - Context: `reter.log', level=logging.INFO)
openai.api_key = '[REDACTED]'
logging.warning("NVIDIA GPU not available, falli`
  - ❓ Could not notify repository owner

### Bluenot3/VIP_GPT

**File:** .py

- [❌ Invalid] OpenAI API key (redacted: sk-C...e4fJ)
  - Context: `port openai
import gradio as gr
openai.api_key = "[REDACTED]"

messages = [{"role": "system", "content": "You `
  - ❓ Could not notify repository owner

### feenixmd/FEENIX-MD-V5

**File:** set.js

- [❌ Invalid] OpenAI API key (redacted: sk-w...qi0v)
  - Context: `  OPENAI_API_KEY : process.env.OPENAI_API_KEY || '[REDACTED]',
    URL : process.env.BOT_MENU_LINKS || 'https:`
  - ❓ Could not notify repository owner

### mxrah10/toxicity-censor

**File:** api.js

- [❌ Invalid] OpenAI API key (redacted: sk-k...hXZx)
  - Context: `let prompt = null;

const apiKey = "[REDACTED]"; //use your own api key >:(
const url = 'https:/`
  - ❓ Could not notify repository owner

### Buddha0338/Astoria

**File:** ai.js

- [❌ Invalid] OpenAI API key (redacted: sk-w...CQ8y)
  - Context: `st configuration = new Configuration({
  apiKey: '[REDACTED]'
             
});
const openai = new OpenAIApi(c`
  - ❓ Could not notify repository owner

### SanjeevScript/Synthax-Submission

**File:** AI.JS

- [❌ Invalid] OpenAI API key (redacted: sk-k...7F4R)
  - Context: `t.getElementById('response');

const API_KEY = '[REDACTED]';

form.addEventListener('submit', async (e) =>`
  - ❓ Could not notify repository owner

### vsvaidya27/Yield

**File:** gpt.js

- [❌ Invalid] OpenAI API key (redacted: sk-O...E8B7)
  - Context: `baseURL: 'https://api.red-pill.ai/v1',
  apiKey: '[REDACTED]',
})


export async function getBestPool() {
    `
  - ❓ Could not notify repository owner

### Friska42/animatePolisislot

**File:** tes.js

- [❌ Invalid] OpenAI API key (redacted: sk-Y...Srh4)
  - Context: `// [REDACTED]
import { Configuration, OpenAIApi } from "openai"`
  - ❓ Could not notify repository owner

### SammyLifetime/Sammy

**File:** z2.js

- [❌ Invalid] OpenAI API key (redacted: sk-1...PjWQ)
  - Context: `etStreamFromURL } = global.utils;
const apiKey = "[REDACTED]";

module.exports = {
  config: {
    name: "imag`
  - ❓ Could not notify repository owner

### PuneethMyadam/AgriQGPT

**File:** apikey.env

- [❌ Invalid] OpenAI API key (redacted: sk-Y...pPlp)
  - Context: `apikey = "[REDACTED]"`
  - ❓ Could not notify repository owner

### goiliace/Health-Assitance

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...bOVs)
  - Context: `GOOGLE_API_KEY = "[REDACTED]"
GOOGLE_CSE_ID = "12b568fa2ea4b49dd"
MODEL_NAME =`
  - ❓ Could not notify repository owner

### project-violet/violet

**File:** tag-info/a.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...ae-8)
  - Context: `.__run())
        logger.info("Done.")


Request("[REDACTED]").run()`
  - ❓ Could not notify repository owner

### echoyuzhou/ticktock_text_api

**File:** kb.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...cfG8)
  - Context: `d()
def NE_disp(name_entity_list):
    api_key = '[REDACTED]'
    response_disp_list =[]
    for item in name_`
  - ❓ Could not notify repository owner

### PaulKinlan/PSITools

**File:** run.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...uGr0)
  - Context: `oogleapis.com/pagespeedonline/v1/runPagespeed?key=[REDACTED]&strategy=mobile&screenshot=true&url="

request_qu`
  - ❓ Could not notify repository owner

### PiDronics/monitoring-automated-hydroponics-system

**File:** env.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...0GG4)
  - Context: ` dynamic.
auth_cred = {
            "API_KEY": "[REDACTED]",
            "AUTH_DOMAIN": "pidronics.firebase`
  - ❓ Could not notify repository owner

### vignesh07/there-will-be-blood

**File:** GCM.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...vPJE)
  - Context: `from gcm import GCM
import access_gcm
#gcm = GCM('[REDACTED]')
data = {'message': 'testing'}

gcmm = access_gc`
  - ❓ Could not notify repository owner

### arj7192/yc-ml

**File:** yc.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...5H_Y)
  - Context: `tube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = '[REDACTED]'


def get_comment_threads(youtube, video_id, com`
  - ❓ Could not notify repository owner

### SudodevsHQ/drplantnik

**File:** s.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...DfmE)
  - Context: `port requests
import json
start_index = 0
key =  "[REDACTED]"
cx = "002299373873344878019:yf5tyg0gmnq"
q = "he`
  - ❓ Could not notify repository owner

### purusharths/rajasthan_hackathon

**File:** fsm.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...QOjE)
  - Context: `0
SPEED_LIMIT = 75


handler = googlemaps.Client("[REDACTED]")
epochstart = time.time()
class Signal_sim:
    `
  - ❓ Could not notify repository owner

### agscala/groupme-john-cena

**File:** yt.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...oOjg)
  - Context: `/v3/search?part=snippet&q="+formatted_query+"&key=[REDACTED]")
	id = x.json()["items"][0]['id']['videoId']
	re`
  - ❓ Could not notify repository owner

### Zusyaku/Tools-Termux-Kali-Linux

**File:** ytviews-master/sub.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...cskk)
  - Context: `/www.googleapis.com/youtube/v3/videos?id={ur}&key=[REDACTED]&part=id,%20snippet", headers=ua).text
     h=json`
  - ❓ Could not notify repository owner

### yashahuja31/coal-mines-carbon-emission-calculator

**File:** cb.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...2FZQ)
  - Context: `mport Image
import base64


gen_ai_api_key = "[REDACTED]"

gen_ai_api_url = "https://generativelanguage.`
  - ❓ Could not notify repository owner

### hcn1z1/HC-RAT

**File:** HC.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...bGOw)
  - Context: `   self.firebaseConfig = {
            "apiKey": "[REDACTED]",

            "authDomain": "keylogger-8d7ca.fir`
  - ❓ Could not notify repository owner

### dpshah23/Desktop_Assistant

**File:** ai.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...b3Mw)
  - Context: `wn
import speak as sp



genai.configure(api_key='[REDACTED]')
model = genai.GenerativeModel('gemini-pro')
def`
  - ❓ Could not notify repository owner

### Rdxcj/Testq

**File:** A.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...yUAc)
  - Context: `tps://www.youtube.com',
}

params = {
    'key': '[REDACTED]',
    'prettyPrint': 'false',
}

json_data = {
  `
  - ❓ Could not notify repository owner

### ragavadk1/fbyt

**File:** yt3.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...yUAc)
  - Context: `ttps://www.youtube.com',
}
params = {
    'key': '[REDACTED]',
    'prettyPrint': 'false',
}
json_data = {
   `
  - ❓ Could not notify repository owner

### arifistifik/sbt

**File:** sb.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...HSP8)
  - Context: `ch?part=snippet&maxResults=10&q={}&type=video&key=[REDACTED]".format(str(search)))
                           `
  - ❓ Could not notify repository owner

### firefighter-system/Hardware-Device

**File:** rm.py

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...WWPI)
  - Context: `om pyrebase import pyrebase

config = {"apiKey": "[REDACTED]",
              "authDomain": "firefightingmonito`
  - ❓ Could not notify repository owner

### jgthms/juketube

**File:** app.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...k1vY)
  - Context: `e/v3/search', {
        params: {
          key: '[REDACTED]',
          type: 'video',
          maxResults: `
  - ❓ Could not notify repository owner

### mbebenita/WasmExplorer

**File:** v2.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...vjZU)
  - Context: `googleJSClientLoaded() {
  gapi.client.setApiKey("[REDACTED]");
  gapi.client.load('urlshortener', 'v1', funct`
  - ❓ Could not notify repository owner

### jcubic/jquery.terminal-www

**File:** sw.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...YuQA)
  - Context: `saging.js');

var firebaseConfig = {
    apiKey: "[REDACTED]",
    authDomain: "jcubic-1500107003772.firebasea`
  - ❓ Could not notify repository owner

### ue/neleryasak

**File:** fb.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...-YLU)
  - Context: `/analytics';

const firebaseConfig = {
  apiKey: '[REDACTED]',
  authDomain: 'neleryasak.firebaseapp.com',
  p`
  - ❓ Could not notify repository owner

### divyanshu013/no-crackers

**File:** env.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...2Cn4)
  - Context: `export default {
  apiKey: '[REDACTED]',
  authDomain: 'no-crackers.firebaseapp.com',
  `
  - ❓ Could not notify repository owner

### mlassoff/Vanilla_JavaScript_Project

**File:** key.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...f3jU)
  - Context: `let googleKey = "[REDACTED]";
`
  - ❓ Could not notify repository owner

### omarcusdev/fadergs-wpp-com-ia

**File:** v3.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...b43k)
  - Context: `ative-ai');
const genAI = new GoogleGenerativeAI('[REDACTED]');

wppconnect
  .create({
    session: 'sessionN`
  - ❓ Could not notify repository owner

### Shubh2-0/Youtube-Clone

**File:** my.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...wTRU)
  - Context: `show)


 async function show (){

let API_KEYS =["[REDACTED]","[REDACTED]","AIzaS`
  - ❓ Could not notify repository owner
- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...ME1M)
  - Context: `9wTRU","AIzaSyASPLAWmjCPDRoiMtt1AHGQ0TGyRx9wTRU","[REDACTED]","AIzaSyA8HVQEsyROLmeZ4P3GhKRCU2BajTnJUNc","AIzaS`
  - ❓ Could not notify repository owner
- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...JUNc)
  - Context: `9wTRU","AIzaSyBihnXKUmx9h6DHAlTNkrZ-6znzrz3ME1M","[REDACTED]","AIzaSyAgE8JOY06kJSUxBYYXCGKhQnhx1qD8jdA"]

let `
  - ❓ Could not notify repository owner
- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...8jdA)
  - Context: `3ME1M","AIzaSyA8HVQEsyROLmeZ4P3GhKRCU2BajTnJUNc","[REDACTED]"]

let num= Math.floor(Math.random()*3)
 
let API`
  - ❓ Could not notify repository owner
- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...ZASU)
  - Context: `empty()




// function empty(){

// let api_key="[REDACTED]";
// let channel_http="https://www.googleapis.com`
  - ❓ Could not notify repository owner

### nimash3eshan/COMBook

**File:** tb.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...1jIY)
  - Context: `nfiguration
const firebaseConfig = {
    apiKey: "[REDACTED]",
    authDomain: "combook-676c6.firebaseapp.com"`
  - ❓ Could not notify repository owner

### mskogen/APCS-BlizzardKicker

**File:** map.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...DNa8)
  - Context: ` src="https://maps.googleapis.com/maps/api/js?key=[REDACTED]&callback=initMap"
      async defer></script>
/`
  - ❓ Could not notify repository owner
- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...wJeE)
  - Context: `+Colorado+Boulder&destination=Copper+Mountain&key=[REDACTED]

not sure the best way to run this. XMLHttpRequ`
  - ❓ Could not notify repository owner

### artik-snu/soscon-dashboard

**File:** fcm.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...j_YU)
  - Context: `var FCM = require('fcm-push');

var serverKey = '[REDACTED]';
var fcm = new FCM(serverKey);

var dtoken = "cn`
  - ❓ Could not notify repository owner

### cc5-team-blue/habbits

**File:** db.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...VFC8)
  - Context: `ase from 'firebase';

const config = {
  apiKey: '[REDACTED]',
  authDomain: 'test-d3d42.firebaseapp.com',
  d`
  - ❓ Could not notify repository owner

### brandly/harvard-food-trucks-cli

**File:** cli.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...AXxs)
  - Context: `oISOString(),
    orderBy: 'startTime',
    key: '[REDACTED]'
  }
}).then((res) => {
  const items = res.data.`
  - ❓ Could not notify repository owner

### joshkmartinez/youtube-views

**File:** api.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...IXV8)
  - Context: `ls%2Cstatistics&id=' +
        id +
        '&key=[REDACTED]'
    )
    .then(response => {
      views = resp`
  - ❓ Could not notify repository owner

### BabyGupta05/faballey

**File:** CSR.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...qGjE)
  - Context: `
// let apiKey="[REDACTED]";
// let url =`https://www.youtube.com/watch?v=ZP`
  - ❓ Could not notify repository owner

### dannam83/Pijns

**File:** App.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...cFGQ)
  - Context: `
    super();
    const config = {
      apiKey: '[REDACTED]',
      authDomain: 'pijns-dc1c1.firebaseapp.com'`
  - ❓ Could not notify repository owner

### Anjalita/LifeLink-Blood-and-Health-Network

**File:** in.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...-Ro0)
  - Context: `nfiguration
const firebaseConfig = {
  apiKey: "[REDACTED]",
  authDomain: "blood-and-hospital-finder-main.`
  - ❓ Could not notify repository owner

### SrijanSahaySrivastava/Quizzy

**File:** x.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...2cxU)
  - Context: `ative-ai";

const genAI = new GoogleGenerativeAI("[REDACTED]");

async function run() {
  const model = genAI.`
  - ❓ Could not notify repository owner

### bryantee/YouTube-API-Test

**File:** js.js

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...eVXc)
  - Context: `		q: state.searchTerm,
			maxResults: 5,
			key: '[REDACTED]'
		};
		url = 'https://www.googleapis.com/youtube`
  - ❓ Could not notify repository owner

### voteliquid/liquid.us

**File:** .template.env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...CbdQ)
  - Context: `ddress Autocompletion
export GOOGLE_GEOCODER_KEY="[REDACTED]"

# Affects Build Settings
export NODE_ENV="devel`
  - ❓ Could not notify repository owner

### ani-team/github-client

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...iJpk)
  - Context: `*/


# Firebase section
REACT_APP_FIREBASE_apiKey=[REDACTED]
REACT_APP_FIREBASE_authDomain=github-client-47c49`
  - ❓ Could not notify repository owner

### ezedinff/express-mongo-starter

**File:** variables.env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...vGv0)
  - Context: `smtp.mailtrap.io
MAIL_PORT=2525
PORT=7777
MAP_KEY=[REDACTED]
SECRET=snickers
KEY=sweetsesh`
  - ❓ Could not notify repository owner

### Flutter-Buddies/App

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...QH_c)
  - Context: `CALENDAR_KEY=[REDACTED]`
  - ❓ Could not notify repository owner

### chellyyyy/IE104_BakeryShop

**File:** .history/config_20221209221443.env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...8MHY)
  - Context: `APIKEY=[REDACTED]`
  - ❓ Could not notify repository owner

### SilvinPradhan/store-locator

**File:** .history/src/local_20201012132618.env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza..._oxg)
  - Context: `REACT_APP_KEY="[REDACTED]"`
  - ❓ Could not notify repository owner

**File:** .history/src/local_20201012132451.env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza..._oxg)
  - Context: `REACT_APP_GOOGLE_KEY="[REDACTED]"`
  - ❓ Could not notify repository owner

### junedkazi/dang-thats-delicious

**File:** variables.env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...iOKg)
  - Context: `HOST=mailtrap.io
MAIL_PORT=2525
PORT=7777
MAP_KEY=[REDACTED]
SECRET=snickers
KEY=sweetsesh
`
  - ❓ Could not notify repository owner

### menglu95/react-Metronic-theme-2

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...BLC8)
  - Context: `REACT_APP_DEFAULTAUTH=fake

REACT_APP_APIKEY=[REDACTED]
REACT_APP_AUTHDOMAIN=themesbrand-admin.firebasea`
  - ❓ Could not notify repository owner

### AkimSolovyov/node

**File:** node-delicious/variables.env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...vGv0)
  - Context: `smtp.mailtrap.io
MAIL_PORT=2525
PORT=7777
MAP_KEY=[REDACTED]
SECRET=snickers
KEY=sweetsesh
`
  - ❓ Could not notify repository owner

### digita-webshop/digita-webshop-frontend

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...ISlk)
  - Context: `REACT_APP_GOOGLE_MAPS_API_KEY="[REDACTED]"
GENERATE_SOURCEMAP=false`
  - ❓ Could not notify repository owner

### Absolument-Oui/InfoGare

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...FVpM)
  - Context: `REACT_APP_FIREBASE_API_KEY="[REDACTED]"
REACT_APP_FIREBASE_AUTH_DOMAIN="infogares-f.fire`
  - ❓ Could not notify repository owner

### Suvink/e-waste-collector

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...81BM)
  - Context: `VUE_APP_APIKEY=[REDACTED]`
  - ❓ Could not notify repository owner

### ChrisOwen101/SouthAfricanCodeSchools

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...jBfo)
  - Context: `ge the data displayed.
REACT_APP_FIREBASE_API_KEY=[REDACTED]
REACT_APP_FIREBASE_AUTH_DOMAIN=southafricacodesch`
  - ❓ Could not notify repository owner

### clarkmalmgren/bolingbrook-church

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...wmQI)
  - Context: `REACT_APP_API_URL=/api
REACT_APP_MAPS_API_KEY=[REDACTED]
REACT_APP_OAUTH_CLIENT_ID=110300192266-iumh11t60u`
  - ❓ Could not notify repository owner

### onyx-nxt/COOL-BOI-BOT

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...Wlic)
  - Context: `R_API=c1ba87d2a335656425a17e4395303046
YT_API_KEY=[REDACTED]
JOKE_API=AuthDisabled
NODE_ENV=production`
  - ❓ Could not notify repository owner

### missionedweb/web_react

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...HJF8)
  - Context: `REACT_APP_FIREBASE_API_KEY=[REDACTED]
REACT_APP_FIREBASE_AUTH_DOMAIN=missioned-bb43f.fi`
  - ❓ Could not notify repository owner

### Simul8-OS/98ish

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...OHAI)
  - Context: `YOUTUBE_KEY = '[REDACTED]'`
  - ❓ Could not notify repository owner

### codetapacademy/codetap-cafe

**File:** .env

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...3on0)
  - Context: `FIREBASE_CONFIG="{\"apiKey\":\"[REDACTED]\",\"databaseURL\":\"https://codetap-cafe.firebase`
  - ❓ Could not notify repository owner

### curvedinf/dir-assistant

**File:** README.md

- [❌ Invalid] Google Gemini/PaLM API key (redacted: xxxx...xxxx)
  - Context: `DIR_ASSISTANT.LITELLM_API_KEYS]
GEMINI_API_KEY = "[REDACTED]"
```

LiteLLM supports all major LLM APIs, includ`
  - ❓ Could not notify repository owner

### pratxk007/office-app

**File:** lecx.txt

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...lAUs)
  - Context: `IC_CLERK_SIGN_UP_URL=/sign-up
NEXT_GEMINI_API_KEY=[REDACTED]

NEXT_PLAYHT_USER_ID = gL9eWzowaUND1wWODOgumqN6Er`
  - ❓ Could not notify repository owner

### amir-mostafa-hs/Code-Converter

**File:** note.txt

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...IF7g)
  - Context: `:[{"text": "Explain how AI works"}]
    }]
   }'

[REDACTED]`
  - ❓ Could not notify repository owner

### Janani-N14/Phonic-Flux

**File:** key.txt

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...mLCE)
  - Context: `gemini_api_key = '[REDACTED]'
`
  - ❓ Could not notify repository owner

### Kudamasangomai/businessdaily

**File:** keys.txt

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...4V_o)
  - Context: `#GOOGLE_API_KEY = "[REDACTED]"
GOOGLE_API_KEY = "AIzaSyB0jAipA0NLnAmwgxjeQ6eJpY`
  - ❓ Could not notify repository owner
- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...GRtc)
  - Context: `BsUNYd90GG2HV-73ETg-RDmdUx4V_o"
GOOGLE_API_KEY = "[REDACTED]"
INTEGRATION_ID = '13396',
INTEGRATION_KEY = 'af2`
  - ❓ Could not notify repository owner

### proxOP/RAG-law_test

**File:** .env.txt

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...mMCU)
  - Context: `GOOGLE_API_KEY="[REDACTED]"
`
  - ❓ Could not notify repository owner

### Santillan-Go/ai-app

**File:** text.txt

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...lyl4)
  - Context: `# GOOGLE_API_KEY="[REDACTED]"




# GOOGLE_CLIENT_ID="865101620485-v7sotr0a0lt`
  - ❓ Could not notify repository owner

### Dream1ance/Arc-lit

**File:** m.txt

- [❌ Invalid] Google Gemini/PaLM API key (redacted: AIza...hoaU)
  - Context: `to store your API key
import os
GOOGLE_API_KEY="[REDACTED]"
google_api_key = os.getenv('GOOGLE_API_KEY')
g`
  - ❓ Could not notify repository owner

### yihong0618/tg_bot_collections

**File:** README.md

- [❌ Invalid] OpenAI API key (redacted: ${AN...KEY})
  - Context: `d --name tg_bot_collections -e ANTHROPIC_API_KEY='[REDACTED]' -e TELEGRAM_BOT_TOKEN='${TELEGRAM_BOT_TOKEN}' --`
  - ❓ Could not notify repository owner

### instructlab/rag

**File:** Readme.md

- [❌ Invalid] OpenAI API key (redacted: your..._key)
  - Context: `# Set Anthropic API Key
export ANTHROPIC_API_KEY='[REDACTED]'

export OPENBLAS_NUM_THREADS=72
export OMP_NUM_T`
  - ❓ Could not notify repository owner

### Ayesha-Imr/Study-Space-RAG-Demo-App

**File:** env.txt

- [❌ Invalid] Cohere API key (redacted: <you...key>)
  - Context: `COHERE_API_KEY="[REDACTED]"
GROQ_API_KEY="<your-groq-api-key>"
`
  - ❓ Could not notify repository owner

### Clevrr-AI/Clevrr-Computer

**File:** .env_dev

- [❌ Invalid] OpenAI API key (redacted: <YOU...KEY>)
  - Context: `AZURE_OPENAI_API_KEY  = "[REDACTED]"
AZURE_OPENAI_ENDPOINT = "<YOUR_AZURE_ENDPOINT_UR`
  - ❓ Could not notify repository owner
- [❌ Invalid] OpenAI API key (redacted: <YOU...KEY>)
  - Context: ` "<YOUR_AZURE_DEPLOYMENT_NAME>"
GOOGLE_API_KEY = "[REDACTED]"
VERSION = "0.9.2" # Do not change this.
LAST_CHA`
  - ❓ Could not notify repository owner

### strnad/CrewAI-Studio

**File:** .env_example

- [❌ Invalid] OpenAI API key (redacted: FILL...-KEY)
  - Context: `# OPENAI_API_KEY="[REDACTED]"
# OPENAI_API_BASE="OPTIONAL-FILL-IN-YOUR-OPENAI-`
  - ❓ Could not notify repository owner
- [❌ Invalid] OpenAI API key (redacted: FILL..._KEY)
  - Context: `E="http://localhost:1234/v1"
# ANTHROPIC_API_KEY="[REDACTED]"
# AGENTOPS_API_KEY="FILL-IN-YOUR-AGENTOPS_API_KE`
  - ❓ Could not notify repository owner

### ehristoforu/TensorLM-webui

**File:** configure.txt

- [❌ Invalid] OpenAI API key (redacted: sk-U...oZKW)
  - Context: `tlm_version = 3.1.0

openai_key = [REDACTED] # this is test free key that can't work, go to ht`
  - ❓ Could not notify repository owner

