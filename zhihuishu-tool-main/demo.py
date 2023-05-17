# Author ：梦情
# Time ：2023/4/4 16:11
# File : demo.py
import requests
from Crypto.Cipher import AES
import base64
# from zhs_api import Course,ZHSEncrypt
import time



HOME_PAGE_AES_KEY = '7q9oko0vqb3la20r'
# 通用IV，MODE
ZHS_AES_IV = '1g3qqdh4jvbskb9x'

ZHS_AES_MODE = AES.MODE_CBC
# 共享学分课视频页AES Key
STUDY_VIDEO_AES_KEY = 'azp53h0kft7qi78q'
# 共享学分课问答页AES Key
QA_AES_KEY = 'w1k5ntxecb8wmbc2'



class AESEncrypt:
    # 这里的AES字符串加密参考了 https://zhuanlan.zhihu.com/p/184968023
    def __init__(self, key, iv, mode):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')
        self.mode = mode

    def pkcs7padding(self, text):
        """明文使用PKCS7填充 """
        bs = 16
        length = len(text)
        bytes_length = len(text.encode('utf-8'))
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        padding_text = chr(padding) * padding
        self.coding = chr(padding)
        return text + padding_text

    def aes_encrypt(self, content):
        """ AES加密 """
        cipher = AES.new(self.key, self.mode, self.iv)
        # 处理明文
        content_padding = self.pkcs7padding(content)
        # 加密
        encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
        # 重新编码
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result

    def aes_decrypt(self, content):
        """AES解密 """
        cipher = AES.new(self.key, self.mode, self.iv)
        content = base64.b64decode(content)
        text = cipher.decrypt(content).decode('utf-8')
        return text.rstrip(self.coding)

class ZHSEncrypt:
    """
    智慧树自写加密算法集
    """
    def get_zwsds(id):
        zwsds = base64.b64encode(id.encode("utf-8")).decode("utf-8")
        return zwsds

    def gen_watch_point(start_time, end_time=300):
        """
        生成watchPoint（提交共享学分课视频进度接口用）
        :param start_time: 起始视频进度条时间，秒
        :param end_time: 提交时距离起始时间的间隔，秒。默认为正常观看时请求database接口的间隔时间
        """
        record_interval = 1990
        total_study_time_interval = 4990
        cache_interval = 180000
        database_interval = 300000
        watch_point = None
        total_stydy_time = start_time
        for i in range(int(end_time * 1000)):
            if i % total_study_time_interval == 0:
                total_stydy_time += 5
            if i % record_interval == 0 and i >= record_interval:
                t = int(total_stydy_time / 5) + 2
                if watch_point is None:
                    watch_point = '0,1,'
                else:
                    watch_point += ','
                watch_point += str(t)
        return watch_point

    def get_ev( t: list, key='zzpttjd'):
        """
        D26666 key:zzpttjd
        D24444 key:zhihuishu
        生成参数ev（提交共享学分课视频进度接口用）
        见面课页面加密参数D24444也使用此加密
        :param t:
        请注意，此列表不同接口顺序不同
        以下为Database进度提交接口的顺序
        [
           recruitId,
           lessonId,
           smallLessonId, （对应"videoSmallLessons": 下的ID， 没有为0）
           lastViewVideoId,
           videoDetail.chapterId,
           data.studyStatus, （str e.g:  "0"）
           parseInt(this.playTimes),(提交到进度的时间，比如从5秒观看到25秒，那么这里提交了20秒)
           parseInt(this.totalStudyTime),
           i.i(p.g) (ablePlayerX('container').getPosition())   （str e.g:  "00:04:43"）
         ],
         以下为见面课提交的参数列表：
         [recruitId, liveCourseId, userId, relativeTime, watchType, curVideoId]
        """
        # _d = 'zzpttjd'
        _d = key

        # Y/
        def y(_t):
            e_2 = str(hex(_t))[2:]
            if len(e_2) < 2:
                return '0' + e_2
            else:
                return e_2

        # Z
        e = ''
        for j in t:
            e += str(j) + ';'
        e = e[0:len(e) - 1]
        # X
        e_1 = ''
        for i in range(len(e)):
            n = ord(e[i]) ^ ord(_d[i % len(_d)])
            e_1 += y(n)
        return e_1



aes = AESEncrypt(key=STUDY_VIDEO_AES_KEY, iv=ZHS_AES_IV, mode=ZHS_AES_MODE)

url = 'https://studyservice-api.zhihuishu.com/gateway/t/v1/learning/saveDatabaseIntervalTimeV2'


watch_point = ZHSEncrypt.gen_watch_point(start_time=1)


sdsew = ZHSEncrypt.get_zwsds(id="8060324824")

zwsds_data = [
  165501,
  1000217175,
  0,
  12032801,
  1000088193,
  "0",
  45,
  315,
  "00:05:29",
  "dDxOw5rQzhs"
]
zwsds = ZHSEncrypt.get_ev(zwsds_data)

courseId = ''


raw_data = f'{{"ewssw":"{watch_point}",' \
           f'"sdsew":"{sdsew}",' \
           f'"courseId":{courseId},' \
           f'"zwsds":{zwsds},' \
           f'"dateFormate":{int(round(time.time()) * 1000)}}}'

print(raw_data)

# session = requests.Session()
#
# secret_str = aes.aes_encrypt(raw_data)
# data = {"secretStr": secret_str}
#
# r = session.post(url, data=data)



