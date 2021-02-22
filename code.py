server.modules = ("mod_fastcgi", "mod_rewrite")
 server.document-root = "/path/to/root/"
 fastcgi.server = ( "/code.py" =>
 (( "socket" => "/tmp/fastcgi.socket",
    "bin-path" => "/path/to/root/code.py",
    "max-procs" => 1
 ))
 )

 url.rewrite-once = (
   "^/favicon.ico$" => "/static/favicon.ico",
   "^/static/(.*)$" => "/static/$1",
   "^/(.*)$" => "/code.py/$1"
 )