https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis


https://www.rosehosting.com/blog/how-to-install-configure-and-use-redis-on-ubuntu-16-04/


https://redislabs.com/

https://redis.io/commands



Python redis:
https://pypi.org/project/redis/


COMMAND:

 KEYS *

key/string: SET name “vinay”
GET name

Hash map: HMSET vinay   name "vinay Pandey" age "31" city "Bihar"
HGETALL vinay


Find type of kye
Type keyname



"OK"
redis>  LPUSH key2 "value"
(integer) 1
redis>  SADD key3 "value"
(integer) 1
redis>  TYPE key1
"string"
redis>  TYPE key2
"list"
redis>  TYPE key3
"set"
redis>
