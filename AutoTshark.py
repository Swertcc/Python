'''
该代码用于个人python课程学习
python大作业的“自动化Tshark流量采集”部分
2024/1/4
'''
import time
import logging
import subprocess
from selenium import webdriver


def start_tshark(output_file):
    # 启动tshark，将流量输出到指定文件
    command = ["D:\\Wireshark\\tshark.exe", "-i", "\\Device\\NPF_{86922588-9E46-40DE-9BCC-86EA2F3AE778}", "-w", output_file]

    # 使用subprocess.Popen异步启动tshark
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    time.sleep(2)  # 给tshark一些时间来启动
    return process
def stop_tshark(process):
    # 终止tshark进程
    process.terminate()
    process.communicate()  # 等待进程完成

def visit_website(url, num_visits, count):
    # 创建浏览器驱动
    driver = webdriver.Chrome()
    # 命名每个pcap文件，例如：result_1.pcapng
    pcap_filename = f"C:\\Users\\swert\\Desktop\\Python12.31-1.5\\result\\pnc\\result_{count}.pcapng"
    # 启动新的tshark捕获流量
    tshark_process = start_tshark(pcap_filename)

    for visit_count in range(1, num_visits + 1):

        driver.get(url)
        logger.info(f'the {visit_count} time to {url}: {driver.title}')
        time.sleep(3)  # 可根据需要调整等待时间

        # 使用tshark停止流量捕获并保存到pcap文件中
        #stop_tshark()

    # 关闭浏览器驱动
    driver.quit()

    # 最后一次访问结束后停止tshark
    stop_tshark(tshark_process)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    websites_file = "website.txt"
    num_visits = 100
    count = 1
    with open(websites_file, "r") as file:
        websites = file.read().splitlines()

    for website in websites:
        visit_website(website, num_visits, count)
        count += 1
