# agni

簡易的な検索システム用のバックエンドサーバです．

この API サーバを使用することで，自分自身の検索インタフェースの開発に専念することができます．

## Requirements

- python (^3.6.7)
- docker
- [dbmate](https://github.com/amacneil/dbmate)

## Run

初めて実行する場合は，以下のいずれかのコマンドでコンテナをビルドしてください．

```sh
docker compose build
```

一度実行すれば，以降は以下のコマンドで起動することができます．

```sh
docker compose start
```

`localhost:8888` に API サーバ，`localhost:3336` に MySQL サーバが起動します．

もしも個別にコンテナを起動したい場合は，`app` / `database` ディレクトリに移動し，同様のコマンドを実行してください．


## Develop

`app` ディレクトリには依存パッケージを記載したファイルがあります．(`pyproject.toml`, `requirements.txt`)

[poetry](https://python-poetry.org/) を使用している場合は，以下のコマンドで仮想環境の作成と依存パッケージのインストールができます．

\* **python(3.6.7) の環境があることを確認してください**

```sh
poetry shell
poetry install
```

使用していない場合は `requirements.txt` を使用して依存パッケージをインストールしてください．

```sh
pip install -r requirements.txt
```

3. 自由にカスタマイズを加えてください 🎉
