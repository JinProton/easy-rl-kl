import os
import git
from openxlab.model import download

LLM_PATH = './OpenLMLab/InternLM-chat-7b'
EASY_RL_PATH = './datawhalechina/easy-rl'
ST_PATH = './data/model/sentence-transformer'
ABS_ST_PATH = os.path.abspath(ST_PATH)

def download_repo():

    # 下载 InternLM-chat-7b 模型
    download(model_repo='OpenLMLab/InternLM-chat-7b', output=LLM_PATH)

    # 指定要下载的仓库的 URL，这里默认选择 easy-rl，也可以选择其他知识库
    repo_url = 'https://github.com/datawhalechina/easy-rl.git'
    # 'https://github.com/datawhalechina/fun-rec.git',
    # 'https://github.com/datawhalechina/competition-baseline.git',
    # 'https://github.com/datawhalechina/joyful-pandas.git'

    # 下载知识库
    if not os.path.exists(EASY_RL_PATH):
        print(EASY_RL_PATH)
        git.Repo.clone_from(repo_url, EASY_RL_PATH)

    # 下载 sentence-transformer 模型
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
    # 下载模型
    if not os.path.exists(ABS_ST_PATH):
        print(ABS_ST_PATH)
        os.system(f'huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir {ABS_ST_PATH}')
