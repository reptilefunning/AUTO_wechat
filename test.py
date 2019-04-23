import time
import multiprocessing
import json
import requests
import datetime
import threading
from queue import Queue
import schedule
import wxpy
from weather import WeatherSpider
from soul import Soul
bot = wxpy.Bot(cache_path=True)
    
def send():

    wea_ls = '早上好，今天又是元气满满的一天\n' + '西昌' + WeatherSpider('101271610').run() +'您可以：'+ '\n回复"成都"获取成都天气\n回复"唯美"随机获取励志唯美语录'+'\n调试bug请无视'
    send_queue = Queue()

    fris = bot.friends().search('')
    for fri in fris:
        # print(fri)
        send_queue.put(fri)
    t_list = []
    for i in range(3):
        t_msend = threading.Thread(target=more_thread, args=(send_queue, wea_ls))
        t_list.append(t_msend)
    for t in t_list:
        t.setDaemon(True)  
        t.start()
    for q in [send_queue]:
        q.join()  
    print("主线程结束")

def more_thread(send_queue, wea_ls):
    while True:
        try:
            friend = send_queue.get()
            friend.send(wea_ls)
            print("发送成功，a:",friend)
           
        except Exception as ret:
          
            time.sleep(1)
        send_queue.task_done()

@bot.register()
def rcv_message(msg):

    sender = str(msg.sender)

    if '<MP:'in str(sender)  or '<Group:' in str(sender):
        return
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    recv_save = ''
    rev_save = '发送人:'+ sender +" 内容:"+ msg.text + ' ' + now
    print(rev_save)
    with open('wechat.md','a') as f:
        f.write(rev_save)
        f.write('\n')
    if msg.text == '成都':
        wea_cd = '成都' + WeatherSpider('101270101').run()
        return wea_cd
    elif msg.text == '唯美':
        return Soul()
    else:
        try:
            return robot_tuling(msg.text)
        except Exception as ret:
            fri_me = bot.friends().search('virtual')[0]
            fri_me.send("发送错误，信息:%s" % ret)
            return ("主人不在所以我智商为0了，请尝试下回复(唯美)随机获取励志唯美语句") 

def robot_tuling(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "a3c47b29c1cd497e87ab03eb6e566f32"
    payload = {
        "key": api_key,
        "info": text,
    }
    rec = requests.post(url, data=json.dumps(payload))
    result = json.loads(rec.content)
    # print(result["text"])
    if result["text"] == "亲爱的，当天请求次数已用完。":
        return "主人不在所以我智商为0了，尝试下回复(唯美)随机获取励志唯美语句"
    return result["text"]

def main():
    print("程序开始运行...")
    schedule.every().day.at("10:01").do(send)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    