# Author ：梦情
# Time ：2023/4/5 21:46
# File : 扫码登录.py
import base64  # base64编解码模块
import io  # io模块用于处理二进制数据
import json  # json模块用于处理JSON数据
import websockets, asyncio  # websockets模块用于websocket连接，asyncio模块用于异步编程
import requests  # requests模块用于发送HTTP请求
from PIL import Image  # PIL模块用于图像处理

session = requests.session()  # 创建一个会话对象

# 显示图像的函数
def show_image(img):
    img = Image.open(io.BytesIO(img))  # 从二进制数据中读取图像
    img.show()  # 显示图像

# 验证二维码的函数
def validate_qr_code(qr_callback):
    """
    验证二维码
    :return: oncePassword, uuid
    """
    qr_page = "https://passport.zhihuishu.com/qrCodeLogin/getLoginQrImg"  # 智慧树二维码登录页面

    async def wait(url):
        async with websockets.connect(url, extra_headers=session.headers) as websocket:  # 异步连接websocket
            while True:
                msg = json.loads(await websocket.recv())  # 接收websocket消息，并将JSON字符串解码为Python对象
                print(msg)
                match msg["code"]:  # 匹配消息类型
                    case 0:
                        print(msg["msg"])
                    case 1:
                        print(msg["msg"])
                        return msg["oncePassword"], msg["uuid"]  # 返回一次性密码和UUID
                    case 2:
                        print(msg["msg"])
                        raise Exception(msg["msg"])  # 抛出异常
                    case _:
                        raise Exception(f"Unknown Response {msg.msg}")  # 抛出异常

    r = session.get(qr_page, timeout=10).json()  # 发送HTTP GET请求并解码JSON响应

    qrToken = r["qrToken"]  # 获取二维码token
    img = base64.b64decode(r["img"])  # 将Base64编码的图像数据解码为二进制数据
    qr_callback(img)  # 调用回调函数显示二维码图像
    return asyncio.get_event_loop().run_until_complete(
        wait(f"wss://appcomm-user.zhihuishu.com/app-commserv-user/websocket?qrToken={qrToken}"))  # 异步等待用户扫描二维码并返回相关信息

aa = validate_qr_code(qr_callback=show_image)  # 调用验证二维码函数，并传入显示图像的回调函数

print(aa)  # 打印返回的一次性密码和UUID
