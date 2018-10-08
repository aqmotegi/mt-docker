#======== REQUIRED SETTINGS ==========

CGIPath        /cgi-bin/mt/
StaticWebPath /mt-static
StaticFilePath /var/www/html/mt-static

#======== DATABASE SETTINGS ==========

ObjectDriver DBI::mysql
Database #作成するDB名
DBUser root
DBPassword #作成したユーザのパスワード
DBHost db

#======== LAUNGUAGE SETTINGS ==========
DefaultLanguage ja

ImageDriver ImageMagick
