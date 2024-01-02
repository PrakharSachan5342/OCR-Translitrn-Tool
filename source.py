!pip install easyocr
from PIL import Image
import easyocr

# Path to the Tesseract executable
tesseract_cmd = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Tesseract-OCR"

# Initialize the easyocr reader for Sindhi
reader = easyocr.Reader(['sd'])

# Load the image (upload it to Colab or provide the file path)
image_path = '/content/sindhi_text.jpeg'  # Replace with your image file name
sindhi_image = Image.open(image_path)

# Perform OCR to extract Sindhi text
results = reader.readtext(image_path)
recognized_text = [result[1] for result in results]
sindhi_text = '\n'.join(recognized_text)

def sindhi_to_devanagari(sindhi_text):
    # Define a dictionary for Sindhi to Devanagari transliteration
    transliteration_dict = {
        'آ': 'आ',
        'ا': 'अ',
        'ب': 'ब',
        'پ': 'प',
        'ت': 'त',
        'ٽ': 'ट',
        'ٹ': 'ट',
        'ث': 'स',
        'ج': 'ज',
        'ڄ': 'ड़',
        'ڊ': 'ड',
        'ڈ': 'ड',
        'ح': 'ह',
        'خ': 'ख',
        'د': 'द',
        'ڍ': 'द',
        'ڏ': 'द',
        'ڌ': 'द',
        'ذ': 'ज़',
        'ر': 'र',
        'ڙ': 'ड़',
        'ز': 'ज़',
        'ژ': 'ज़',
        'س': 'स',
        'ش': 'श',
        'ص': 'स',
        'ض': 'ज़',
        'ع': 'अ',
        'غ': 'ग',
        'ف': 'फ',
        'ق': 'क़',
        'ڪ': 'क',
        'ک': 'क',
        'ڪ': 'क',
        'گ': 'ग',
        'ڳ': 'ग़',
        'ڱ': 'ड़',
        'ل': 'ल',
        'م': 'म',
        'ن': 'न',
        'ڻ': 'ण',
        'ڼ': 'ण',
        'ڽ': 'ण',
        'ه': 'ह',
        'و': 'व',
        'ء': 'अ',
        'ي': 'य',
        '۽': 'य',
        '۾': 'य',
        'ئ': 'अ',
        'ى': 'य',
        'ۏ': 'व',
        'ٻ': 'ब',
        'ٺ': 'ठ',
        'ٿ': 'ट',
        'ڀ': 'ब',
        'ؤ': 'व',
        '٭': 'ऱ',
        'ڃ': 'च',
        'ڻ': 'ण',
        'ڨ': 'फ़',
        'ﻁ': 'च',
        'ڪ': 'क',
        '٪': '%',
        '،': ',',
        '؛': ';',
        '؟': '?',
    }

    devanagari_text = ''.join([transliteration_dict.get(char, char) for char in sindhi_text])

    return devanagari_text

# Transliterate Sindhi text to Devanagari
devanagari_text = sindhi_to_devanagari(sindhi_text)

# Print the transliterated Devanagari text
print(devanagari_text)
