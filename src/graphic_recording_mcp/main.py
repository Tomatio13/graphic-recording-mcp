import os
from pathlib import Path
from fastmcp import FastMCP

# FastMCPインスタンスを作成
mcp = FastMCP("Graphic Recording MCP")

@mcp.tool()
def generate_graphic_recording(markdown: str) -> dict:
    """
    Markdownテキストからグラフィックレコーディング風HTMLを生成するプロンプトを返す
    
    Args:
        markdown: 変換するMarkdownテキスト
    
    Returns:
        プロンプトと指示を含む辞書
    """
    if not markdown:
        return {
            "error": "Markdownテキストが提供されていません。",
            "status": "error"
        }
    
    # infographic.mdからプロンプトテンプレートを読み込む
    current_dir = Path(__file__).parent
    infographic_path = current_dir / "infographic.md"
    
    try:
        with open(infographic_path, "r", encoding="utf-8") as f:
            prompt_template = f.read()
    except FileNotFoundError:
        return {
            "error": "infographic.mdファイルが見つかりません。",
            "status": "error"
        }
    
    # プロンプトテンプレートとMarkdownテキストを結合
    combined_prompt = f"{prompt_template}\n\n## 入力されたMarkdown\n\n{markdown}"
    
    # クライアント側でClaude 3.7 Sonnetを実行するためのレスポンスを返す
    return {
        "prompt": combined_prompt,
        "instruction": "このプロンプトをClaude 3.7 Sonnetに送信して、グラフィックレコーディング風HTMLをArtifactsで作成してください",
        "status": "success"
    }

if __name__ == "__main__":
    mcp.run() 