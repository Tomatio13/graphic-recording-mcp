# グラフィックレコーディング風HTML生成 MCP

このMCPサーバーは、Markdown形式のテキストを入力として受け取り、
グラフィックレコーディング風のHTMLを生成するためのプロンプトを返します。

# 利用イメージ
以下のようにMarkdownファイルをグラッフックレコードMCPに渡すようにプロンプトを実行してください。

```
NHKの最新ニュースを取得しMarkdownで要約後にグラッフックレコードに変換してください。
```

Makiさん(Sunwood-ai-labs)が公開されている「グラフィックレコーディング風インフォグラフィック変換プロンプト」を用いてHTMLを生成し、Claude DesktopのArtifactsで表示します。

## ディレクトリ構成

```
graphic-recording-mcp/
├── pyproject.toml        # プロジェクト設定ファイル
├── README.md             # このファイル
├── start.sh              # 起動スクリプト
└── src/
    └── graphic_recording_mcp/
        ├── __init__.py   # パッケージ初期化ファイル
        ├── main.py       # MCPサーバーのメイン実装
        └── infographic.md # グラフィックレコーディング生成用プロンプトテンプレート
```
## グラフィックレコーディング生成用プロンプトテンプレートの変更方法

Makiさん(Sunwood-ai-labs)が公開されている
[グラフィックレコーディング風インフォグラフィック変換プロンプト](https://github.com/Sunwood-ai-labs/MysticLibrary/tree/main/prompts/documentation)
のGraphic-recording-style-infographic-v2.mdをinfographic.mdとして格納しています。
変更する場合は、infographic.mdを変更してください。

## インストール方法

### 前提条件

- Python 3.12以上
- uv（`pip install uv`でインストール可能）

### インストール手順

#### 方法1: uvを使用した環境構築（推奨）

uvを使用して環境をセットアップします：

```bash
# uvをインストール
pip install uv

# リポジトリをクローンまたはダウンロード
git clone https://github.com/Tomatio13/graphic-recording-mcp.git
cd graphic-recording-mcp

# 仮想環境を作成し、依存関係をインストール
uv venv
uv pip install -e .
```

または、提供されている`start.sh`スクリプトを使用すると、自動的に環境がセットアップされます：

```bash
chmod +x start.sh
./start.sh
```

## 使用方法

### サーバーの起動

uvを使用して直接実行するには：

```bash
# uvコマンドでPythonモジュールを実行
uv run python -m src.graphic_recording_mcp.main
```

または、提供されている`start.sh`スクリプトを使用して起動することもできます：

```bash
./start.sh
```

##### claude_desktop_config.jsonの記述方法

Claude Desktopの設定ファイルは以下のような構造で記述します：

```json
{
  "mcpServers": {
    "graphic-recording": {
      "command": "sh",
      "args": [
        "/path/to/mcp-graphicrec-server/start.sh"
      ]
    }
  }
}
```
もしくは、以下のように直接uvコマンドを実行してください。

```json
{
  "mcpServers": {
    "graphic-recording": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "-m",
        "src.graphic_recording_mcp.main"
      ]
    }
  }
}
```

主な設定項目：
- `mcpServers`: MCPサーバーの設定を含むオブジェクト
  - `graphic-recording`: サーバーの識別子（任意の名前）
    - `command`: 実行するコマンド（通常は `sh`）
    - `args`: コマンドの引数（起動スクリプトのパス）

##### 設定ファイルの使用手順
以下、Linuxを前提としています。

1. `start.sh` ファイルに実行権限を付与します：
   ```bash
   chmod +x start.sh
   ```

2. Claude Desktopの設定ファイルを編集します：
   ```bash
   vi ~/.config/Claude/claude_desktop_config.json
   ```

3. 上記のJSONを既存の設定に追加します（既存のエントリがある場合は、`mcpServers` オブジェクト内に新しいエントリを追加）

4. Claude Desktopを再起動して設定を反映させます

### 謝辞
[Sunwood-ai-labs](https://github.com/Sunwood-ai-labs/MysticLibrary/tree/main/prompts/documentation)