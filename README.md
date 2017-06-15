Cashier
-
_Persistent caching for python functions_


Simply add a decorator to a python function and cache the results for future use. Extremely handy when you are dealing with I/O heavy operations which seldom changes or CPU intensive functions as well.

Anatomically, once a function is called, result from the function is cached into an SQLite3 database locally, with an expiry time. There is a maximum length for the cache to prevent cache flooding the file system.


Installation
-

```pip install cashier```

Or you can clone the source and run setup.py

```bash
git clone git@github.com:atmb4u/cashier.git
cd cashier
python setup.py install
```


Usage
-



```python
from cashier import cache

@cache()
def complex_function(a,b,c,d):
    return complex_calculation(a,b,c,d)
```

If you go ahead on the above configuration, following are the default values

* cache_file :  `.cache`

* cache_time : `84600`
* cache_length : `10000`
* retry_if_blank : `False`


Advanced Usage
-


```python
from cashier import cache

@cache(cache_file="sample.db", cache_time=7200, cache_length=1000, 
       retry_if_blank=True)
def complex_function(a, b, c, d):
    return complex_calculation(a, b, c, d)
```


`cache_file` : SQLite3 file name to which cached data should be written into (defaults to .cache)

`cache_time` : how long should the data be cached in seconds (defaults to 1 day)

`cache_length` : how many different arguments and corresponding data should be cached (defaults to 10000)

`retry_if_blank` : If True, will retry for the data if blank data is cached ( default is `False`)


Performance Benchmark
-

For reproducing results, run `python test.py` from the project root.

No Cache Run: **9.932126 seconds**

First Caching Run: **9.484081 seconds**

Cached Run: **0.606016 seconds (16 x faster)**
