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

# 🔑 Step 1: Get a Gemini API Key

## 1.1 Access Google AI Studio
Go to [Google AI Studio](https://aistudio.google.com/app/apikey)

## 1.2 Create an API Key
- Log in with your Google Account  
- Click **Get API key**  
- Click **Create API key**  
- Copy the API key (format: `AIzaSy...`)

## 1.3 Save the API Key
⚠️ **IMPORTANT**: Do not share your API key with anyone!

# 💻 Step 2: Set Up the API Key

## Windows Powershell
```powershell
[System.Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'your-api-key-here', 'User')
```
## macOS / Linux
```powershell
export GEMINI_API_KEY="your-api-key-here"
```
### ✅ Verify API Key
## Windows (cmd)
```powershell
echo %GEMINI_API_KEY%
```
## macOS / Linux
```powershell
echo $GEMINI_API_KEY
```





