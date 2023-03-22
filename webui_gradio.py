from transformers import AutoModel, AutoTokenizer
import gradio as gr
import uuid
from settings import model_dir,log_dir,model,tokenizer

#place your THUDM/chatglm-6b  here
# model_dir = r"D:\ChatGLM-系列项目\ChatGLM-6B-main\THUDM\chatglm-6b"
# log_dir = r"D:\ChatGLM-系列项目\MY_ChatGLM\ChatGLM_webui\log"


# tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
# model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().cuda()
# 改用4-bit加载
# model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().quantize(4).cuda()
model = model.eval()

MAX_TURNS = 20
MAX_BOXES = MAX_TURNS * 2


def predict(input, history=None):
    if history is None:
        history = []
    response, history = model.chat(tokenizer, input, history)
    updates = []
    for query, response in history:
        updates.append(gr.update(visible=True, value="User：" + query))
        updates.append(gr.update(visible=True, value="ChatGLM-6B：" + response))
    if len(updates) < MAX_BOXES:
        updates = updates + [gr.Textbox.update(visible=False)] * (MAX_BOXES - len(updates))
    return [history] + updates

def clear(histroy):
    histroy = []
    updates = []
    updates = updates + [gr.Textbox.update(visible=False)] * (MAX_BOXES - len(updates))  
    return [histroy] + updates

def save(history):
    uuid_key = uuid.uuid1()
    if history is None:
        history = []
        
    with open(log_dir+f"/saved_file_{uuid_key}.txt","a") as f:    
        for query, response in history:
            f.write("Q:"+query+"\n")
            f.write(response+"\n")
    return [history]


with gr.Blocks() as demo:
    gr.Markdown("""
    # Model based on ChatGLM-6b
    """)
    state = gr.State([])
    text_boxes = []
    for i in range(MAX_BOXES):
        if i % 2 == 0:
            text_boxes.append(gr.Markdown(visible=False, label="Question："))
        else:
            text_boxes.append(gr.Markdown(visible=False, label="Answer："))

    with gr.Row():
        with gr.Column(scale=20):
            txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)
        with gr.Column(scale=1):
            button1 = gr.Button("Generate")
        with gr.Column(scale=1):
            button2 = gr.Button("clear")    
        with gr.Column(scale=1):
            button3 = gr.Button("save")    
    # click(fn,input,output)        
    button1.click(predict, [txt, state], [state] + text_boxes)
    button2.click(clear,[],[state]+text_boxes)
    button3.click(save,[state],[state])
demo.queue().launch(share=True)
