# import paramiko

# ssh_key_private = "-----BEGIN RSA PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCp+yzDsvC77fAv\nVGOZZ2x0WrWX9XXukx/n387rTBegm+kDXkwj6NJ1tSk3XuMo7xDfCuAHv406iYwj\n2SaQraKDKP4rJi5/QeIn8hkBooRGQuc88LhTun3LhoJhtZK4rUfKK7rbZJQZ3qQ8\n+tON248E/OZYG4lEBA9beKLmc71Mmy6kRaZP53FK8NI8ruEA5YFqccX7SEfWx3Nq\n11NPLfPNN+PZM8qdSzo9r6z7Snw/RfyguKNH7SlpizcgnLIoXcbyGwvH1k6wXK6V\nxwJt7dh0ZQh+sSf20QV5xjRsalG4xUmw4HTOJkwTPfEvCB9OURclQX2+C/H3nJu/\nigBp/207AgMBAAECggEAFJb+yKPLwk/jmLAVsnbTLdLxDTun8eKzajBzjY/1irho\nBMbu3SiuGaD8oZ7mUEaJGiNkmLusvUr9BTigEcVempmkFBD3b+XIocMTIV4QvLwM\n65ZTFZ1Q8I7WC0TlxWYD/KrIYxvvTqTn6xUM/DF8xQNnWYPYYDtHqvJVdSnO49Dz\nxCOH/u3dWJbejgX/7MfOnCLquLRQAFSJ8ZtacdgdutP0B/mr0kXzTnBX340Ly+PE\n36tvQcIDGdqj3nX+QVlmEWv6nnZebJDGgltDA2Ls+6ev+xewRtA/DBYx4JLOaBks\nmPFmHmttxrZsu+I1z4wvmmUgEoynIZA8cCWcPutOuQKBgQDZgajjbyV8OpJ5prmd\n+KszR9BQPrgvrRYe+IRyDOx9og18sdfQWwo2WTtT4WnWh506CiB0GDn+PLhszt8n\nbiKvTe5149jlOa6iiv8CehseEbge95ThdCSq1t5yosGy+jPcUXVxXbb+mCzpU7b8\nIYNYMO0GfjeFbETnG04XZM1ucwKBgQDIEFWV9Tkzf1OedE48SIXI9AgX7GrsCwou\nHYCOsqNAQH3hldFmFNs0vETN+I1KmmBCIXXLVzHkL4ZCQxqy+lnPp1U7kOtv+tNK\nfGXjx3O2vSQ1fqwStEDw1htvd19J+95ljIAupCBq/8a7tZ72IeuN4vkkC0ppy9e6\n0h8JI2TMGQKBgAzhYcf+KAEgUtZDalCRjkneIdbur+ea32l8HBPI8iRKeXP98CLV\nkVhAloPUIHlk1InAWcWmPaDxpZZD9fEW05UAD3QJxylj7hSQGKPj6UExmW60CKwF\nPbqkOM4fF0trB7EvXb4V56VSC67Rl099CJMrao3s4YrUK4xoEIrQHF5DAoGBAKsp\n/m9L3GKIvvvEOeMtkPh6gConpNrKHy2RJBnyD+W6x3gm+35AvcKCiMNHsWpwZYZu\nph8QPKkjV9R9IOybcBdO7IcH18Z4bClAANQ+ImvnqoDyHTnradwi8loNYUMk8AMl\nj81XsjyZFGgoXRXrs2IzHECQQFv/gFRfzRm+ZFCRAoGAIBfEYB2ZcaUz7FWIQ4Ux\n5NLmz7nMtBzBS4KyNjHYNa3HOCcPGU1mhFwq44mg9YCLFW+FPShFyTbqYgxykpa4\nYb2Tjc8CCPt1HNf5UHTnK7y1iBH/juub4t7HzsCNF6Cor+RHpA/yjdnvbf/1spJ9\nl/Vdu951i2H35z7rvaceB6Q=\n-----END RSA KEY-----\n"

# import io
# pkey = paramiko.RSAKey.from_private_key(io.StringIO(ssh_key_private))

# print(pkey)



from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

key = rsa.generate_private_key(
            backend=crypto_default_backend(),
            public_exponent=65537,
            key_size=2048
        )

private_key = key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.OpenSSH,
            crypto_serialization.NoEncryption()
        )


ssh_key_private = private_key.decode('utf-8')
print(ssh_key_private)

import io
import paramiko
pkey = paramiko.RSAKey.from_private_key(io.StringIO(ssh_key_private))

print(pkey)