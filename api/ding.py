import requests
import json


def send_message_to_ding(url):
    title = "自动化"
    message = "**{}**\n" \
              "- **加粗文本**\n" \
              "- *斜体文本*\n" \
              "- [链接地址]({})\n".format(title, url)
    # message = """
    # # **{}**
    # 这是一个示例消息，包含以下格式：
    # - **加粗文本**
    # - *斜体文本*
    # - [链接地址]({})
    # - 换行示例：
    #   换行后的内容
    # """.format(title, url)
    # 钉钉机器人的 Webhook 地址
    webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=38409aacf428f49294f334f0a3bf4778c0fd2af10c027f054e8f21384c87a2be"
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": message,
            # "at":"",
            # "isAtAll":""
        }
    }

    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    # 检查请求是否成功
    if response.status_code == 200:
        print("消息发送成功")
    else:
        print("消息发送失败")
