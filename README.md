# MY-MCPSV-POSTGRES

## 説明
FastAPI、FastMCPを使って、PostgreSQLにアクセスするMCP Serverのサンプルソース
初めてMCP Serverを開発する人向けのサンプルソースを提供

## 使い方

### テーブルとデータを準備する

* `create_inventory.sql`を使ってPostgreSQLにinventoryテーブルを作成
* `sample_data.csv`をロードする

### APIを準備する
* uv をインストールする
    ```
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

* プロジェクトフォルダを作成し、python仮想環境を作成する
    ```
    cd MY-MCPSV-POSTGRES
    uv init API-SERVER
    ```
* パッケージをインストールする
    ```
    cd API-SERVER
    uv add fastapi uvicorn
    uv add "psycopg[binary]"
    ```
* `main.py` を`API-SERVER`フォルダに配置し、接続文字列をご自身の環境に合わせて更新する。接続文字列は、`main.py`の`DB_PATH`変数に設定されています。

* FastAPIを起動する
    ```
    uv run uvicorn main:app --reload
    ```

### MCP Serverを準備する

* プロジェクトフォルダを作成し、python仮想環境を作成する
    ```
    cd MY-MCPSV-POSTGRES
    uv init MCP-SERVER
    ```

* パッケージをインストールする
    ```
    uv add "mcp[cli]"
    uv add httpx
    ```

* `server.py` を`MCP-SERVER`フォルダに配置

* MCP Server を起動する
    ```
    uv run mcp dev server.py
    ```

### クライアントにMCP Serverを設定する

* `mcp.json`に追加する。
  Claude Desktopの場合は、`claude_desktop_config.json`
    ```
    "mcpServers": { 
        "INVENTORY": {
        "command": "uv",
        "args": [
            "run",
            "--directory",
            "C:\\MY-MCPSV-POSTGRES\\MCP-SERVER",
            "python",
            "server.py"
        ]
        }
    },
    ```