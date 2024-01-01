'''
该代码用于个人python课程学习
python大作业的“数据提取可视化”部分
2024/1/1
'''
import json
import csv

# 读取 JSON 文件
with open('C:/Users/swert/Desktop/Python12.31-1.5/result/json/res_ssl.json', 'r') as json_file:
    data = json.load(json_file)

# 初始化
stream_data = {}

# 遍历每个数据流
for entry in data:
    if '_source' in entry and 'tcp' in entry['_source']['layers']:
        tls_stream = entry['_source']['layers']['tcp']['tcp.stream']
        tcp_len = entry['_source']['layers']['tcp']['tcp.len']

        if tls_stream in stream_data:
            stream_data[tls_stream]['TCP_len'].append(tcp_len)
        else:
            stream_data[tls_stream] = {'SNI': ' ', 'TCP_len': [tcp_len]}

    if '_source' in entry and 'ssl' in entry['_source']['layers'] and 'ssl.record' in entry['_source']['layers']['ssl'] and 'ssl.handshake' in entry['_source']['layers']['ssl']['ssl.record'] and 'Extension: server_name' in entry['_source']['layers']['ssl']['ssl.record']['ssl.handshake']:
        if 'Server Name Indication extension' in entry['_source']['layers']['ssl']['ssl.record']['ssl.handshake']['Extension: server_name']:
            ssl_extension = entry['_source']['layers']['ssl']['ssl.record']['ssl.handshake']['Extension: server_name']['Server Name Indication extension']['ssl.handshake.extensions_server_name']
            if ssl_extension:
                sni_value = entry['_source']['layers']['ssl']['ssl.record']['ssl.handshake']['Extension: server_name']['Server Name Indication extension']['ssl.handshake.extensions_server_name']
                stream_data[tls_stream]['SNI'] = sni_value

# 打开 CSV 文件进行写操作
with open('./CSV/res.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # 写入 CSV 文件的标题行
    fieldnames = ['Stream_num', 'SNI'] + [f'Packet{i}_len' for i in range(1, max(map(len, (entry['TCP_len'] for entry in stream_data.values())), default=1) + 1)]
    csv_writer.writerow(fieldnames)

    # 写入数据行
    for stream_num, stream_info in stream_data.items():
        row = [stream_num, stream_info['SNI']] + stream_info['TCP_len']
        csv_writer.writerow(row)

print("FINISHED!")
