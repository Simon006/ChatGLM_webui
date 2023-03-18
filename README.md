# ChatGLM_webui
This is a WebUI program based on ChatGLM 

## Background
The ChatGLM_WebUI web project aims to provide a convenient and intuitive interactive interface for users to easily converse with ChatGLM_WebUI. Users can enter text on the web page and ChatGLM_WebUI will generate corresponding responses based on the user's input. chatGLM_WebUI web project also provides some additional features, such as history, language selection, theme switching, etc., so that users can better use ChatGLM_WebUI. Project based on Tsinghua University's open source project in huggingface.[ChatGLM](https://github.com/THUDM/ChatGLM-6B)

Due to the small size of ChatGLM-6B, it is currently known to have considerable limitations, such as factual/mathematical logic errors, possible generation of harmful/biased content, weak contextual ability, self-awareness confusion, and Generate content that completely contradicts Chinese instructions for English instructions. Please understand these issues before use to avoid misunderstanding.

Here we propose a fine-tuned solution in the direction of intelligent customer service in future.


## Install
```shell
`pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117`
`pip install -r requirements.txt`
```

## ChatGLM-PreTrained
```shell
`https://huggingface.co/THUDM/chatglm-6b`
```

## Usage
### webui_demo
```shell
`python weiui_gradio.py` 
```

### cmd demo
```
`python cli_demo.py`
```

## Examples