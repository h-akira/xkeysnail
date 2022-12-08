# xkeysnail
Mac風のキーマップを実現するために利用．

## 環境構築
```
sudo pip3 install xkeysnail
```
sudoなしで実行できるようにするため，`sudo visudo`でファイルを開いて以下を追記する．
```
${ユーザーネーム} ALL=(ALL) NOPASSWD: /usr/local/bin/xkeysnail
```

## 参考
[GitHub](https://github.com/mooz/xkeysnail)  
[作者のQiita](https://qiita.com/mooz@github/items/c5f25f27847333dd0b37)
