# Introduction

This project was inspired by **nihongo‑anki‑gen**.  

When learning Japanese, I often face the problem of having too much vocabulary to memorize. As a learner preparing for the JLPT exam, I am busy with deadlines and do not have much time to add words manually into Anki. The most effective way for me to study is through vocabulary with example sentences and Han‑Viet readings. Therefore, I created this project to automate the process of learning Japanese vocabulary.

**The Goal**  
Automating the creation of Japanese Anki flashcards to save time and make vocabulary learning more effective.

# Japanese Vocabulary List

| Word     | Kana     | Meaning                          | Example | ExampleTrans | HanViet |
|----------|----------|----------------------------------|---------|--------------|---------|
| アルバイト | arubaito | việc làm thêm                    |         |              |         |
| パート     | paato    | việc làm thêm                    |         |              |         |
| 産業      | sangyou  | sản nghiệp                       |         |              |         |
| 工業      | kougyou  | công nghiệp                      |         |              |         |
| 技術      | gijutsu  | kỹ thuật                         |         |              |         |
| 法律      | houritsu | luật                             |         |              |         |
| 貿易      | boueki   | giao dịch, thương mại            |         |              |         |
| 翻訳      | honyaku  | dịch                             |         |              |         |
| 運転手    | untenshu | tài xế                           |         |              |         |
| 駅員      | ekiin    | nhân viên nhà ga                 |         |              |         |
| 看護師    | kangoshi | y tá                             |         |              |         |
| 警察      | keisatsu | cảnh sát                         |         |              |         |
| 公務員    | koumuin  | viên chức                        |         |              |         |
| 新聞社    | shinbunsha | tòa soạn báo                   |         |              |         |
| 習慣      | shuukan  | thói quen, phong tục             |         |              |         |
| アニメ    | anime    | anime, phim hoạt hình kiểu Nhật  |         |              |         |
| 漫画      | manga    | manga, truyện tranh kiểu Nhật    |         |              |         |
| ゲーム    | geemu    | game                             |         |              |         |
| バイオリン | baiorin  | violin                           |         |              |         |
| ロック    | rokku    | nhạc rock                        |         |              |         |
| 水泳      | suiei    | bơi lội                          |         |              |         |
| 泳ぎ方    | oyogikata | cách bơi                        |         |              |         |
| 見物      | kenbutsu | tham quan                        |         |              |         |
| 柔道      | juudou   | võ Judo                          |         |              |         |
| 小説      | shousetsu | tiểu thuyết                     |         |              |         |
| 番組      | bangumi  | chương trình tivi, kênh          |         |              |         |
| 遊び      | asobi    | trò chơi                         |         |              |         |
| 踊り      | odori    | nhảy múa                         |         |              |         |

#  Step 1: Get a Gemini API Key

## 1.1 Access Google AI Studio
Go to [Google AI Studio](https://aistudio.google.com/app/apikey)

## 1.2 Create an API Key
- Log in with your Google Account  
- Click **Get API key**  
- Click **Create API key**  
- Copy the API key (format: `AIzaSy...`)

## 1.3 Save the API Key
 **IMPORTANT**: Do not share your API key with anyone!

#  Step 2: Set Up the API Key

## Windows Powershell
```powershell
[System.Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'your-api-key-here', 'User')
```
## macOS / Linux
```bash
export GEMINI_API_KEY="your-api-key-here"
```
# Verify API Key
## Windows (cmd)
```cmd
echo %GEMINI_API_KEY%
```
## macOS / Linux
```bash
echo $GEMINI_API_KEY
```
#  Step 3: Install Dependencies
##  Before Installing Dependencies: Set Up a Virtual Environment
To keep your project isolated and avoid conflicts with system-wide Python packages, you should always create and activate a virtual environment first.
## Windows
```powershell
# 1. Create a virtual environment named "venv"
python -m venv venv

# 2. Activate the virtual environment
venv\Scripts\activate

# 3. Verify activation (your prompt should show (venv))
```
## Linux / macOS
```bash
# 1. Create a virtual environment named "venv"
python3 -m venv venv

# 2. Activate the virtual environment
source venv/bin/activate

# 3. Verify activation (your prompt should show (venv))
```
## Windows && Linux / macOS
```powershell
  pip install requests
```
#  Step 4: Usage
## Use Arguments
```powershell
# With AI generation
python gemini_anki_generator.py my_vocab.csv --ai

# Without AI
python gemini_anki_generator.py my_vocab.csv
```
#  CSV Input Format
## Recommended Header
```powershell
Word,Kana,Meaning,Example,ExampleTrans,HanViet,JLPT Level
天気,てんき,Weather,,,Thiên khí,N5
勉強,べんきょう,Study,,,Miễn cưỡng,N5
Word,Kana,Meaning,Example,ExampleTrans,HanViet,JLPT Level
天気,てんき,Weather,,,Thiên khí,N5
勉強,べんきょう,Study,,,Miễn cưỡng,N5
```
#  Workflow with AI
```powershell
1. Create CSV with vocabulary (Word, Kana, Meaning)
   ↓
2. Run script with --ai flag
   ↓
3. AI generates:
   - Japanese example sentence
   - Vietnamese translation
   - Sino-Vietnamese reading
   ↓
4. Export to CSV and JSON
   ↓
5. Import into Anki
```
#  Tips & Tricks
## Test with a few words first
```powershell
python gemini_anki_generator.py test_vocab.csv --ai --test
```
#  Notes 

## Large Batch Processing
If your vocabulary file has more than 50 words, the AI may take extra time. Be patient!

## Rate Limits
The Gemini API enforces usage limits. If errors occur, wait a few minutes and retry.

## Save API Calls
Use AI only for words that don’t already have examples, to reduce unnecessary API usage.

## Check Results
Review the generated JSON file to ensure the AI output is correct.

#  Troubleshooting

## Common Issues

- ❌ **GEMINI_API_KEY not found** → API key not set  
- ❌ **API request error** → Internet issue, invalid key, or rate limit exceeded  
- ❌ **Error parsing API response** → AI returned invalid JSON  
- ⚠️ **AI generation failed** → Timeout or invalid response







