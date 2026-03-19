"""- Processing time (latency per audio file)
- Accuracy (Word Error Rate – WER, Character Error Rate – CER)
- Hallucination rate (insertion errors or unsupported content generation)"""
from jiwer import cer ,wer
import requests
import os 
import json
import librosa 


def get_transcript(audio_file_path, api_url, api_key,lang):

    if lang=='en':
        api_url=f"{api_url}/transcribe/english"
    
    elif lang=='ta':
        api_url=f"{api_url}/transcribe/tamil"

    elif lang=='hin':
        api_url=f"{api_url}/transcribe/hindi"

    else :
        api_url=f"{api_url}/translate"

    print(api_url)

      
    

    try:
        headers = {
            "X-API-Key": api_key
        }

        files = {
            "file": open(audio_file_path, "rb")
        }

        response = requests.post(api_url, headers=headers, files=files)

        
        response.raise_for_status()

        data = response.json()
        latency=data.get("processing_time",data)


        
        return data.get("transcription", data) , latency

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

    finally:
        files["file"].close()





if __name__=="__main__":
    API_key="key_scooby_doo"
    json_name="uttarpradesh_hindi"
    lang="hin"
    folder_path='Real_Time_DHL\\UttarPradesh-Hindi'

    results={}   # format is like {'file_name':[transcript,processing_time]
    
    for filename in os.listdir(folder_path):
        file_path=os.path.join(folder_path,filename)

        print(f"Processing language:{folder_path}")

        print("file_path:",file_path)

        audio ,sr=librosa.load(file_path, sr=16000)
        duration = len(audio) / sr

        print("duration:",duration)

        transcription,latency=get_transcript(file_path,api_url='http://14.195.197.108:5005',api_key=API_key,lang=lang)

        results[filename]={"transcript":transcription,"latency":latency,"duration":duration}

    with open(f'{json_name}.json','w',encoding='utf-8') as f :
        json.dump(results, f ,indent=4, ensure_ascii=False)

    print("Results stored")




