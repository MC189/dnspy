import dns.message
import dns.name
import dns.query

qname = dns.name.from_text('dns.google.')
q = dns.message.make_query(qname, dns.rdatatype.A)
response = dns.query.tls(q, 'dns.alidns.com')
print(response)

q = dns.message.make_query(qname, dns.rdatatype.A)
r = dns.query.https(q, "https://dns.alidns.com/dns-query")
print(r)