import docx
from datetime import datetime
import torch
from seamless_communication.models.inference import Translator


translator = Translator("seamlessM4T_medium",vocoder_name_or_card="vocoder_36langs", device=torch.device("cpu"), dtype=torch.float32)


doc = docx.Document("./source.docx")

all_paras = doc.paragraphs

timestamp = datetime.now()
file_name = '%s.txt'%timestamp

with open(file_name, 'w') as f:

    for para in all_paras:
        translated_text,_,_ = translator.predict(para.text,"t2tt","rus",src_lang="eng")
        print(translated_text)
        print("-------")
        f.write(translated_text)
        f.write('\n')
            