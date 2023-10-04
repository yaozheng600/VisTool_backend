from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/get_data', methods=['POST'])
def get_data():
    data_json = request.get_json()  # 获取从前端发送的 JSON 数据
    # 在这里处理接收到的数据并创建 Pandas DataFrame
    # 假设数据是一个包含字典的列表
    df_received = pd.DataFrame(data_json)

    # 从已有的 CSV 文件加载数据
    try:
        df_existing = pd.read_csv('existing_data.csv')
    except FileNotFoundError:
        df_existing = pd.DataFrame()  # 如果文件不存在，创建一个空的 DataFrame

    # 合并接收到的数据和已有的数据
    df_combined = pd.concat([df_existing, df_received], ignore_index=True)

    # 保存合并后的数据为 CSV 文件
    df_combined.to_csv('existing_data.csv', index=False)

    return jsonify({"message": "数据接收成功并追加到 existing_data.csv", "data": df_combined.to_dict()})


if __name__ == '__main__':
    app.run(debug=True)
