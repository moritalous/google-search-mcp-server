# Google Search MCP サーバー

このプロジェクトは、AI アシスタントに Google 検索 API 機能を提供する Model Context Protocol (MCP) サーバーです。

## 概要

Google Search MCP サーバーは、AI アシスタントが Google 検索 API を使用してウェブ検索を実行できるようにするツールです。Gradio と MCP を使用して、AI アシスタントと Google 検索 API の間のインターフェースを提供します。

## 機能

- Google 検索 API を使用したウェブ検索
- 検索結果の JSON 形式での返却
- 最大 20 件の検索結果の取得

## 必要条件

- Python 3.12 以上
- Google Custom Search Engine ID
- Google API キー

## インストール

1. リポジトリをクローンします：

```bash
git clone https://github.com/yourusername/google-search-mcp-server.git
cd google-search-mcp-server
```

2. 依存関係をインストールします：

```bash
pip install -e .
```

3. 環境変数を設定します：

`.env.sample` ファイルを `.env` にコピーし、必要な API キーを追加します：

```bash
cp .env.sample .env
```

`.env` ファイルを編集して、以下の値を設定します：

```
GOOGLE_CSE_ID=あなたのGoogleカスタム検索エンジンID
GOOGLE_API_KEY=あなたのGoogleAPIキー
```

## 使用方法

サーバーを起動するには：

```bash
python app.py
```

これにより、Gradio インターフェースが起動し、MCP サーバーとして機能します。

## MCP との統合

このサーバーは、Model Context Protocol (MCP) を使用して AI アシスタントと統合されます。AI アシスタントは、このサーバーを通じて Google 検索機能にアクセスできます。

## API リファレンス

### perform_web_search

```python
perform_web_search(query: str, num_results: int = 10)
```

**パラメータ**:
- `query` (str): 検索クエリ（最大 400 文字、50 単語）
- `num_results` (int): 結果の数（1〜20、デフォルト 10）

**戻り値**:
- `str`: JSON 形式の検索結果
