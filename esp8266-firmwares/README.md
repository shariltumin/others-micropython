The latest firmware include LittleFS. You can use LittleFS instead of FatFs(default) by doing these in REPL:

```
>>> import os
>>> os.VfsLfs2.mkfs(bdev)

```
