import csv
import json
import os
import requests
from typing import List, Dict


class GeminiAnkiGenerator:  
    def __init__(self, vocabulary_file: str, use_ai: bool = False):
        self.vocabulary_file = vocabulary_file
        self.use_ai = use_ai
        self.flashcards = []
        
        # Get API key 
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if use_ai and not self.api_key:
            print("⚠️  Warning: GEMINI_API_KEY not found in environment variables!")
            print("   AI features will be disabled.")
            print("   Set it with: export GEMINI_API_KEY='your-api-key-here'")
            self.use_ai = False
        
        self.model = "models/gemini-2.5-flash"
        
        if self.api_key:
            self.api_url = f"https://generativelanguage.googleapis.com/v1/{self.model}:generateContent?key={self.api_key}"
    
    def generate_example_sentence_with_ai(self, word: str, kana: str, 
                                          meaning: str, jlpt_level: str = 'N5') -> Dict[str, str]:
        if not self.use_ai or not self.api_key:
            return {"example": "", "example_trans": "", "hanviet": ""}
        
        prompt = f"""Bạn là giáo viên tiếng Nhật chuyên nghiệp.

Cho từ vựng tiếng Nhật: "{word}" ({kana})
Nghĩa tiếng Việt: "{meaning}"
Cấp độ: {jlpt_level}

Hãy tạo:
1. Một câu ví dụ tiếng Nhật sử dụng từ này (phù hợp cấp độ {jlpt_level})
2. Bản dịch tiếng Việt của câu ví dụ
3. Âm Hán Việt của từ "{word}" (nếu có kanji, ví dụ: 天気 -> Thiên khí)

Yêu cầu:
- Câu ví dụ phải tự nhiên, thực tế, dễ hiểu
- Phù hợp với trình độ {jlpt_level}
- Ngắn gọn (không quá 15 từ)

Trả về ĐÚNG format JSON sau:
{{
  "example": "câu tiếng Nhật",
  "example_trans": "câu dịch tiếng Việt",
  "hanviet": "âm Hán Việt"
}}"""
        
        try:
            headers = {"Content-Type": "application/json"}
            data = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.7,
                    "topK": 40,
                    "topP": 0.95,
                    "maxOutputTokens": 1024,
                }
            }
            
            response = requests.post(self.api_url, headers=headers, json=data, timeout=30)
            if response.status_code != 200:
                print(f"⚠️  API Error {response.status_code}: {response.text}")
                return {"example": "", "example_trans": "", "hanviet": ""}
            
            result = response.json()
            text = result["candidates"][0]["content"]["parts"][0]["text"].strip()
            text = text.replace('```json', '').replace('```', '').strip()
            parsed = json.loads(text)
            
            return {
                "example": parsed.get("example", ""),
                "example_trans": parsed.get("example_trans", ""),
                "hanviet": parsed.get("hanviet", "")
            }
            
        except Exception as e:
            print(f"⚠️  Error: {e}")
            return {"example": "", "example_trans": "", "hanviet": ""}
    
    def read_vocabulary(self) -> List[Dict]:
        vocab_list = []
        if not os.path.exists(self.vocabulary_file):
            print(f"❌ Error: File {self.vocabulary_file} not found!")
            return vocab_list
        
        with open(self.vocabulary_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                vocab_list.append(row)
        
        print(f"✓ Loaded {len(vocab_list)} vocabulary items")
        return vocab_list
    
    def process_vocabulary(self) -> List[Dict]:
        vocab_list = self.read_vocabulary()
        if not vocab_list:
            print("❌ No vocabulary to process!")
            return []
        
        flashcards = []
        print(f"\n{'='*70}")
        print(f"Processing {len(vocab_list)} vocabulary items")
        print(f"AI Generation: {'Enabled ✓' if self.use_ai else 'Disabled ✗'}")
        print(f"{'='*70}\n")
        
        for i, vocab in enumerate(vocab_list, 1):
            word = vocab.get('Word', vocab.get('Kanji', ''))
            kana = vocab.get('Kana', vocab.get('Hiragana', ''))
            meaning = vocab.get('Meaning', vocab.get('Nghĩa tiếng Việt', ''))
            
            print(f"[{i}/{len(vocab_list)}] {word} ({kana})")
            
            has_examples = bool(
                vocab.get('Example', vocab.get('Câu ví dụ tiếng Nhật')) and 
                vocab.get('ExampleTrans', vocab.get('Câu ví dụ tiếng Việt'))
            )
            
            if not has_examples and self.use_ai:
                print(f"   🤖 Generating with AI...")
                jlpt_level = vocab.get('JLPT Level', vocab.get('JLPTLevel', 'N5'))
                examples = self.generate_example_sentence_with_ai(word, kana, meaning, jlpt_level)
                if examples['example']:
                    vocab['Example'] = examples['example']
                    vocab['ExampleTrans'] = examples['example_trans']
                    vocab['HanViet'] = examples['hanviet']
                    print(f"   ✓ Generated successfully")
                else:
                    print(f"   ⚠️  Generation failed, using empty values")
            elif has_examples:
                print(f"   ✓ Using existing examples")
            else:
                print(f"   ⊘ No examples (AI disabled)")
            
            flashcard = {
                'word': word,
                'kana': kana,
                'meaning': meaning,
                'example': vocab.get('Example', vocab.get('Câu ví dụ tiếng Nhật', '')),
                'example_trans': vocab.get('ExampleTrans', vocab.get('Câu ví dụ tiếng Việt', '')),
                'hanviet': vocab.get('HanViet', vocab.get('Danh mục', '')),
                'jlpt_level': vocab.get('JLPT Level', vocab.get('JLPTLevel', ''))
            }
            flashcards.append(flashcard)
        
        self.flashcards = flashcards
        print(f"\n{'='*70}")
        print(f"✓ Processed {len(flashcards)} flashcards successfully")
        with_examples = sum(1 for card in flashcards if card['example'])
        print(f"✓ {with_examples}/{len(flashcards)} cards have examples")
        print(f"{'='*70}\n")
        return flashcards
    
    def export_to_anki_csv(self, output_file: str = 'anki_import_gemini.csv'):
        if not self.flashcards:
            self.process_vocabulary()
        if not self.flashcards:
            print("❌ No flashcards to export!")
            return None
        
        output_path = os.path.abspath(output_file)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['Word','Kana','Meaning','Example','ExampleTrans','HanViet','JLPT Level'])
            for card in self.flashcards:
                writer.writerow([
                    card['word'], card['kana'], card['meaning'],
                    card['example'], card['example_trans'],
                    card['hanviet'], card['jlpt_level']
                ])
        print(f"✓ Exported {len(self.flashcards)} flashcards to: {output_path}")
        return output_path
    
    def export_to_json(self, output_file: str = 'flashcards_gemini.json'):
        if not self.flashcards:
            self.process_vocabulary()
        if not self.flashcards:
            print("❌ No flashcards to export!")
            return None
        
        output_path = os.path.abspath(output_file)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.flashcards, f, ensure_ascii=False, indent=2)
        print(f"✓ Exported flashcards to JSON: {output_path}")
        return output_path


def batch_process_vocabulary(input_csv: str, output_csv: str = 'anki_gemini.csv', use_ai: bool = False):
    print("\n" + "="*70)
    print(" "*20 + "GEMINI AI FLASHCARD GENERATOR")
    print("="*70)
    
    generator = GeminiAnkiGenerator(input_csv, use_ai=use_ai)
    flashcards = generator.process_vocabulary()
    if not flashcards:
        print("❌ No flashcards generated!")
        return None, None
    
    csv_path = generator.export_to_anki_csv(output_csv)
    json_path = generator.export_to_json()
    
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate Anki flashcards with Gemini AI')
    parser.add_argument('input_file', nargs='?', help='Input CSV file with vocabulary')
    parser.add_argument('-o', '--output', default='anki_gemini.csv', help='Output CSV filename')
    parser.add_argument('-a', '--ai', action='store_true', help='Enable AI generation')
    parser.add_argument('--test', action='store_true', help='Test with sample data')
    
    args = parser.parse_args()
    
    if args.test:
        # Tạo file test
        test_file = 'test_vocab.csv'
        with open(test_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Word','Kana','Meaning','Example','ExampleTrans','HanViet','JLPT Level'])
            writer.writerow(['天気','てんき','Thời tiết','','','','N5'])
            writer.writerow(['勉強','べんきょう','Học tập','','','','N5'])
        print(f"✓ Created test file: {test_file}")
        args.input_file = test_file
    
    if not args.input_file:
        print("❌ No input file specified!")
        return
    
    batch_process_vocabulary(args.input_file, args.output, use_ai=args.ai)


if __name__ == "__main__":
    import sys
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Program interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
