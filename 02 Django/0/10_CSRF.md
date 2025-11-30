CSRF, or Cross-Site Request Forgery, is a web security vulnerability where an attacker tricks an authenticated user into
performing unintended actions on a trusted site, such as transferring funds or changing account details, by exploiting
automatic inclusion of session cookies in cross-origin requests.[1][5]

## How It Works

Attackers craft malicious web pages or links that trigger HTTP requests (like forms or images) to the target site while the
user is logged in. The browser attaches valid session cookies, bypassing same-origin policy checks, allowing the server to
process the request as legitimate.[6][1]

## Prevention Methods

- Use unique, unpredictable CSRF tokens in forms and validate them server-side to ensure requests originate from your
  site.[2]
- Set cookies with SameSite=Strict or Lax attributes to block cross-site requests.[1]
- Implement fetch metadata headers like Sec-Fetch-Site for servers to detect and block suspicious cross-origin requests.[6]

[1](https://portswigger.net/web-security/csrf) [2](https://www.fortinet.com/resources/cyberglossary/csrf)
[3](https://www.cloudflare.com/learning/security/threats/cross-site-request-forgery/)
[4](https://en.wikipedia.org/wiki/Cross-site_request_forgery) [5](https://owasp.org/www-community/attacks/csrf)
[6](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF)
[7](https://www.reddit.com/r/webdev/comments/19erjw1/can_someone_explain_to_me_how_csrf_works/)
[8](https://www.geeksforgeeks.org/computer-networks/what-is-cross-site-request-forgery-csrf/)
[9](https://www.youtube.com/watch?v=80S8h5hEwTY)
[10](https://www.imperva.com/learn/application-security/csrf-cross-site-request-forgery/)

To implement CSRF protection in a React and Express.js app, follow these general steps:

1. Generate a CSRF token on the server (Express.js) and send it to the client.
2. Store the token securely in the client (React), often in a meta tag or in-memory.
3. Attach the CSRF token as a custom header or in the request body for state-changing requests (POST, PUT, DELETE).
4. Validate the token on the server with each incoming request.

### Express.js (Server-side)

- Use middleware like `csurf` to generate and validate CSRF tokens.
- Send the token to the React client, for example, via a cookie or an API endpoint.

### React (Client-side)

- Retrieve the CSRF token from the cookie or API response.
- Include it in headers of your fetch or axios requests as `'CSRF-Token': csrfToken`

Example snippet from React to send a CSRF token in fetch request:

```js
const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute("content");

fetch("/api/secure-action", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "CSRF-Token": csrfToken,
  },
  body: JSON.stringify({ key: "value" }),
})
  .then((response) => response.json())
  .then((data) => console.log(data));
```

This setup ensures requests are verified against CSRF attacks by comparing tokens on both client and server sides.[1]

[1](https://www.cybersrely.com/5-ways-for-csrf-prevention-in-react-js/)
[2](https://www.stackhawk.com/blog/react-csrf-protection-guide-examples-and-how-to-enable-it/)
[3](https://codebrahma.com/react-csrf-protection-10-best-practices/)
[4](https://www.reddit.com/r/reactjs/comments/10r0oub/mitigate_xss_and_csrf_attacks_simultaneously/)
[5](https://www.reddit.com/r/reactjs/comments/11kuu21/should_i_deploy_csrf_token_for_react_spa/)
[6](https://symfonycasts.com/screencast/reactjs/csrf-protection)
[7](https://stackoverflow.com/questions/75314240/mitigate-csrf-attacks-in-react-js)
[8](https://www.reddit.com/r/node/comments/11k2jwa/how_to_implement_csrf_protection_perrequest/)
[9](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
[10](https://www.reddit.com/r/reactjs/comments/9cbp7t/noob_confusion_around_expressreact_csrf_protection/)
