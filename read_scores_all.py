import json
import os
import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Please provide the folder path as a command-line argument.")
    sys.exit(1)

folder = sys.argv[1]
res = {}


for f_name in os.listdir(folder):
    if not os.path.isdir(os.path.join(folder, f_name)):
        continue
    for model_name in  os.listdir(os.path.join(folder, f_name)):
        if not os.path.isdir(os.path.join(folder, f_name, model_name)):
            continue
        print(f_name, model_name)
        res[f_name+'/'+model_name] = {}
        r = res[f_name+'/'+model_name]
        fld = os.path.join(folder, f_name, model_name)
        for filename in os.listdir(fld):
            if filename.endswith('.json'):
                if filename == "model_meta.json":
                    continue
                file_path = os.path.join(fld, filename)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    r[filename[:-4]] = data['metrics']['NDCG']['NDCG@10']

# You can print or use the `res` dictionary as needed.
print(res)

desired_order = [
    #"deepvk_ruModernBERT-base/797f7ff2a4c6e873525e7c3f0a2afb5746bd226f",
    #"RuModernBERT-base_bs64_lr_2e-05/checkpoint-12400",
    #"RuModernBERT-base_bs64_lr_2e-05_1/checkpoint-33600",
    #"RuModernBERT-base_bs64_lr_2e-05_2/checkpoint-82600",
    #"RuModernBERT-base_bs128_lr_2e-05_2nd_epoch/checkpoint-27200",
    #"RuModernBERT-base_bs128_lr_2e-05_2nd_epoch_1/checkpoint-45400",
    #"RuModernBERT-base_bs128_lr_2e-05_2nd_epoch_2/checkpoint-51400",
    "Qwen/Qwen3-Embedding-0.6B",
    "Qwen/Qwen3-Embedding-4B",
    "Qwen/Qwen3-Embedding-8B",
    "fyaronskiy/code_retriever_ru_en",
    "fyaronskiy/code_retriever_ru_en_512",
    "fyaronskiy/code_retriever_ru_en_256",
    "fyaronskiy/code_retriever_ru_en_128",
    "fyaronskiy/code_retriever_ru_en_64",
    #"nomic-ai/CodeRankEmbed",
    #"BAAI/bge-code-v1",
]

df = pd.DataFrame({k: res[k] for k in desired_order if k in res})
# df = pd.DataFrame(res)
df.to_csv(os.path.join(folder,'results.csv'))