import asyncio
from async_dns.core import types
from async_dns.resolver import ProxyResolver

resolver = ProxyResolver(proxies=['https://www.ruangguru.com/dns-query'])
res, cached = asyncio.run(resolver.query('www.baidu.com', types.A))
print(res)