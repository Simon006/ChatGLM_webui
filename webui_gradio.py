from transformers import AutoModel, AutoTokenizer
import gradio as gr

#place your THUDM/chatglm-6b  here
model_dir = r"D:\ChatGLM-系列项目\ChatGLM-6B-main\THUDM\chatglm-6b"
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
# model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().cuda()
# 改用4-bit加载
model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().quantize(4).cuda()
model = model.eval()

MAX_TURNS = 20
MAX_BOXES = MAX_TURNS * 2


def predict(input, history=None):
    if history is None:
        history = []
    response, history = model.chat(tokenizer, input, history)
    updates = []
    for query, response in history:
        updates.append(gr.update(visible=True, value="用户：" + query))
        updates.append(gr.update(visible=True, value="ChatGLM-6B：" + response))
    if len(updates) < MAX_BOXES:
        updates = updates + [gr.Textbox.update(visible=False)] * (MAX_BOXES - len(updates))
    return [history] + updates

def clear(histroy):
    histroy = []
    updates = []
    updates = updates + [gr.Textbox.update(visible=False)] * (MAX_BOXES - len(updates))  
    return [histroy] + updates

with gr.Blocks() as demo:
    state = gr.State([])
    text_boxes = []
    for i in range(MAX_BOXES):
        if i % 2 == 0:
            text_boxes.append(gr.Markdown(visible=False, label="Question："))
        else:
            text_boxes.append(gr.Markdown(visible=False, label="Answer："))

    with gr.Row():
        with gr.Column(scale=4):
            txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)
        with gr.Column(scale=1):
            button1 = gr.Button("Generate")
        with gr.Column(scale=1):
            button2 = gr.Button("clear")
    # click(fn,input,output)        
    button1.click(predict, [txt, state], [state] + text_boxes)
    button2.click(clear,[],[state]+text_boxes)
demo.queue().launch(share=True)
