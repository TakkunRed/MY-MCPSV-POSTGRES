import httpx
from mcp.server.fastmcp import FastMCP
import logging
import os

API_BASE = "http://127.0.0.1:8000"

mcp = FastMCP("MY-MCPSV-POSTGRES")

# ---- ログ設定（root logger に直接追加） ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "mcp.log")

root = logging.getLogger()
root.setLevel(logging.INFO)

fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
fh.setFormatter(formatter)

root.addHandler(fh)
# ---------------------------------------------

logger = logging.getLogger("MY-MCPSV-POSTGRES")

@mcp.tool()
def get_inventory(
        category: str = "",
        stock_le: int | None = None,
        stock_ge: int | None = None,
):
    """
    在庫管理システムの商品在庫を検索する。在庫数の上限、下限で商品を絞り込むことができます。

    入力:
    - category (str): 商品カテゴリ。例: "果物", "飲料", "菓子"
    - stock_le (int | None): 在庫数の上限
    - stock_ge (int | None): 在庫数の下限
    出力:
    - item_no: 商品番号
    - item_name: 商品名
    - category: 商品カテゴリ
    - stock_qty: 在庫数
    """

    logger.info(f"引数: category={category}, stock_le={stock_le}, stock_ge={stock_ge}")

    params = {}

    # category は空文字で来る可能性があるため、空文字は無視
    if category != "":
        params["category"] = category

    if stock_le is not None:
        params["stock_le"] = stock_le

    if stock_ge is not None:
        params["stock_ge"] = stock_ge

    response = httpx.get(f"{API_BASE}/inventory/get", params=params)
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")