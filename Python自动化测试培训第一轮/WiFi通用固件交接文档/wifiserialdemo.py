
import time
import serial
import threading
import queue


mac_que = queue.Queue()


conn = serial.Serial(port="com3", baudrate=9600, timeout=3)

def deal_cmd_list(cache_list, result_list, check=False):
    # 拼包方法，并对拼接好的正确包进行处理
    if type(cache_list) != type([]):
        reason = "[debugger  ] deal_cmd_list error type !! need data list type list."
        raise Exception(reason)
    # 如果长度小于7个不成为命令：
    if len(cache_list) < 7:
        return result_list
    # 如果 第一位不为 55， 舍弃 55 该位, 进入下一个循环
    if cache_list[0] != 85:
        del cache_list[0]
        return deal_cmd_list(cache_list, result_list, check)
    # 如果 第二位不为 aa， 舍弃 第一, 进入下一个循环
    if cache_list[1] != 170:
        del cache_list[0]
        return deal_cmd_list(cache_list, result_list, check)
    protocol = "protocol"
    # 如果 第三位不为 00， 舍弃 55 aa, 进入下一个循环（假定第三位version一定是 00， 如果协议有变需更改该规则）
    if protocol == "gateway":
        version_list = [0, 1]
    else:
        version_list = [0]
    if cache_list[2] not in version_list:
        del cache_list[0:3]
        return deal_cmd_list(cache_list, result_list, check)
    # 第4,5号位为数据长度
    data_len = cache_list[4] * 256 + cache_list[5]
    cmd_len = 6 + data_len + 1
    # 当命令长度小于该命令应该有的长度时，等待继续读取
    if len(cache_list) < cmd_len:
        test_result = deal_cmd_list(cache_list[3:], [], True)
        if not test_result:
            return result_list
        del cache_list[0:3]
        return deal_cmd_list(cache_list, result_list, check)
    # 如果校验值匹配，则为正常命令， 不正常，则砍掉命令头 55 aa, 继续解析
    calc_sum = sum(cache_list[:cmd_len - 1]) % 256
    if calc_sum != cache_list[cmd_len - 1]:
        del cache_list[0:2]
        return deal_cmd_list(cache_list, result_list, check)
    result_list.append(cache_list[:cmd_len])
    if check:
        return result_list
    del cache_list[0:cmd_len]
    return deal_cmd_list(cache_list, result_list, check)

def do_serial():

    cmd_list = []
    while True:
        readdata = conn.read(1)
        readdata = readdata + conn.read(conn.in_waiting)
        data_list = [x for x in readdata]
        cmd_list.extend(data_list)
        result_list = deal_cmd_list(cmd_list, [])
        for one_cmd in result_list:
            if one_cmd[3] == 0:
                conn.write([85, 170, 3, 0, 0, 1, 0, 3])
            elif one_cmd[3] == 1:
                conn.write([85, 170, 3, 1, 0, 47, 123, 34, 112, 34, 58, 32, 34, 115, 121, 102, 120, 114, 102, 114, 108, 106, 100, 50, 103, 104, 116, 97, 49, 34, 44, 32, 34, 118, 34, 58, 32, 34, 49, 46, 48, 46, 48, 34, 44, 32, 34, 109, 34, 58, 32, 48, 125, 233])
            elif one_cmd[3] == 2:
                conn.write([85, 170, 3, 2, 0, 0, 4])
            elif one_cmd[3] == 3:
                conn.write([85, 170, 3, 3, 0, 0, 5])
            elif one_cmd[3] == 15:
                mac_que.put(one_cmd)



def deal_userinfo():
    t = threading.Thread(target=do_serial)
    t.setDaemon(True)
    t.start()


def test():
    time.sleep(15)
    conn.write([85, 170, 3, 15, 0, 0, 17])
    print("get mac92...................")
    result = mac_que.get(timeout=15)
    print(f"result9444444444:{result}")
    memery = result[5:-1]
    print(f"memery:{memery}")




if __name__ == "__main__":
    deal_userinfo()
    test()
