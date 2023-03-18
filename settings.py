from transformers import AutoModel, AutoTokenizer

model_dir = r"D:\ChatGLM-系列项目\ChatGLM-6B-main\THUDM\chatglm-6b"
log_dir = r"D:\ChatGLM-系列项目\MY_ChatGLM\ChatGLM_webui\log"
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)



# 改用4-bit量化加载  6G显存   use this code if you have 6G avaliable in GPU
model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().quantize(4).cuda()

# 改用16G显存对应的模型
# model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().cuda()