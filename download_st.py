import os

ST_PATH = './data/model/sentence-transformer'

def download_st():
    # 下载 sentence-transformer 模型
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
    ABS_ST_PATH = os.path.abspath(ST_PATH)
    print(ABS_ST_PATH)
    # 下载模型
    os.system(f'huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir {ABS_ST_PATH}')

download_st()
