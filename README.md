# mt-docker  
Movable Type構築用のDockerプロジェクト  

## 準備  
1. mt-config.cgiの編集
1. db/initディレクトリ配下に初期投入用のデータを配置（.sh .sql .sql.gzファイル）
1. cgi-bin配下に/mt-static/以外のダウンロードしたMovable Typeを配置
1. mtディレクトリ配下に上記/mt-static/を配置
1. docker-compose.ymlに作成するDB名を記述

docker-compose.ymlの置かれているディレクトリで以下コマンドを実行  
`docker-compose up -d`
