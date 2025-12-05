import re
from distro import name
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from glob import glob


def fetch_housing_price_data(url):
    """
    拉取国家统计局网站的房价数据并解析表一和表二
    """

    # 发送请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = "utf-8"

        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            return None, None

        # 解析HTML
        soup = BeautifulSoup(response.text, "html.parser")
        # 解析表格名称以确定索引
        text = soup.get_text()
        newName = list(
            set(
                re.findall(
                    r"表\d：\s*\d{4}年\d{1,2}月70个大中城市新建商品住宅销售价格指数",
                    text,
                )
            )
        )[0]
        newIndex = int(newName[1]) - 1
        oldName = list(
            set(
                re.findall(
                    r"表\d：\s*\d{4}年\d{1,2}月70个大中城市二手住宅销售价格指数", text
                )
            )
        )[0]
        oldIndex = int(oldName[1]) - 1

        # 查找所有表格
        tables = soup.find_all("table")

        if len(tables) < 2:
            print(f"找到的表格数量不足，只有 {len(tables)} 个表格")
            return None, None

        # 解析表一：新建商品住宅销售价格指数
        table1_data = parse_table(tables[newIndex], newName)

        # 解析表二：二手住宅销售价格指数
        table2_data = parse_table(tables[oldIndex], oldName)

        return table1_data, table2_data

    except Exception as e:
        print(f"发生错误: {str(e)}")
        return None, None


def parse_table(table, table_name):
    """
    解析HTML表格并转换为DataFrame
    """
    rows = []
    headers = []

    # 提取表头
    thead = table.find("thead")
    if thead:
        header_rows = thead.find_all("tr")
        for tr in header_rows:
            ths = tr.find_all(["th", "td"])
            if not headers:
                headers = [th.get_text(strip=True) for th in ths]

    # 如果没有thead，尝试从第一行获取表头
    if not headers:
        first_row = table.find("tr")
        if first_row:
            ths = first_row.find_all(["th", "td"])
            headers = [th.get_text(strip=True) for th in ths]

    # 提取数据行
    tbody = table.find("tbody")
    if tbody:
        trs = tbody.find_all("tr")
    else:
        trs = table.find_all("tr")[1:]  # 跳过表头行

    for tr in trs:
        cells = tr.find_all(["td", "th"])
        row_data = [cell.get_text(strip=True) for cell in cells]
        if row_data and any(row_data):  # 排除空行
            rows.append(row_data)

    # 创建DataFrame
    if rows:
        print(f"\n{table_name}")
        print("-" * 80)
        df = pd.DataFrame(rows, columns=headers if headers else None)
        print(df)
        return df
    else:
        print(f"{table_name} - 未找到数据")
        return None


def save_to_csv(table1_df, table2_df, tableName):
    """
    将两个表格分别保存为CSV文件
    """
    try:
        if table1_df is not None:
            table1_df.to_csv(
                f"data/NewHousePrice/{tableName}.csv", index=False, encoding="utf-8-sig"
            )
            print(f"\n表1已保存到: data/NewHousePrice/{tableName}.csv")
        if table2_df is not None:
            table2_df.to_csv(
                f"data/OldHousePrice/{tableName}.csv",
                index=False,
                encoding="utf-8-sig",
            )
            print(f"表2已保存到: data/OldHousePrice/{tableName}.csv")
    except Exception as e:
        print(f"保存CSV时发生错误: {str(e)}")


def load():
    result = {}
    files = glob("data/RawData/raw*.json")
    for filename in files:
        with open(filename, "r") as fp:
            data = json.load(fp)
            for item in data["resultDocs"]:
                title = item["data"]["titleO"]
                url = item["data"]["url"]
                if re.match(
                    r"^\d{4}年\d{1,2}月份70个大中城市商品住宅销售价格变动情况$", title
                ):
                    result[title] = url
                    print(f"{title}: {url}")
    return result


def run(url, tableName):
    print(f"正在拉取数据: {tableName} {url}")
    print("=" * 80)
    # 拉取并解析数据
    table1, table2 = fetch_housing_price_data(url)
    # 保存数据
    if table1 is not None or table2 is not None:
        # 保存为CSV（两个独立文件）
        save_to_csv(table1, table2, tableName)
    else:
        print("\n未能获取到有效数据")


def main():
    result = load()
    for tableName, url in result.items():
        # 执行拉取表格
        run(url, tableName)


if __name__ == "__main__":
    main()
