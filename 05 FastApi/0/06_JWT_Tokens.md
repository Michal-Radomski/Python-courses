JWT tokens, or JSON Web Tokens, are structured as compact, URL-safe tokens used for secure data transmission, commonly in
authentication and authorization. They come in various types tailored to specific use cases like access control, session
refresh, or user verification. Common types include access, refresh, ID, and others like confirmation or email verification
tokens.

## Core Types

Access tokens grant short-lived permissions to protected resources, often valid for minutes or hours.[3][4] Refresh tokens
are long-lived credentials used to obtain new access tokens without re-authentication.[4][3] ID tokens convey user identity
information, typically in OpenID Connect flows, and are always JWTs.[7][4]

## Specialized Types

Confirmation tokens verify actions like email or account setup, often single-use with expiration.[1] Sliding tokens extend
expiration dynamically upon use, as in some Django Simple JWT implementations.[3] Opaque tokens contrast with self-contained
JWTs by being undecodable strings requiring server validation.[5][1]

[1](https://help.salesforce.com/s/articleView?id=xcloud.jwt_access_tokens.htm&language=en_US&type=5)
[2](https://docs.secureauth.com/ciam/en/json-web-tokens.html)
[3](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/token_types.html)
[4](https://dev.to/oneadvanced/different-types-of-security-token-4on)
[5](https://www.permit.io/blog/a-guide-to-bearer-tokens-jwt-vs-opaque-tokens)
[6](https://curity.io/blog/how-should-you-serve-your-access-tokens-jwts-phantom-or-split/)
[7](https://curity.io/resources/learn/jwt-best-practices/)
[8](https://auth0.com/docs/secure/tokens/json-web-tokens/json-web-token-structure) [9](https://jwt.io/introduction)
[10](https://jwt.io)
