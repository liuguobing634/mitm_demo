from urllib import request

with request.urlopen('http://v3-dy-y.ixigua.com/441e1244f8b69301d55da15dccd4aa9b/5e20932e/video/m'
                     '/220464edbd70239465698911cc78e8f70251163197de0000b007e0dddc33/?a=1128&br=998&bt=499&cr=3&cs=2'
                     '&dr=0&ds=3&er=&l=2020011623452401000806203320568BED&lr=&qs=11&rc'
                     '=amhlNDc6aTd3bzMzOWkzM0ApZGg8PGQ7Z2U0NzdpODlnZmdgMzBuNGNjajJfLS01LS9zczViNjA0MGE2M2I0NjItLWM6Yw'
                     '%3D%3D') as resp:
    print(resp.info())
    print(resp.getheader(name="Content-Type"))
