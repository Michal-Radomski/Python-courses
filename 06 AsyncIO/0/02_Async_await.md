Async/await simplifies asynchronous code in both JavaScript/TypeScript (JS/TS) and Python, making it read like synchronous
code while handling promises/coroutines effectively.

## JS/TS Use Cases

Use async/await for I/O-bound operations where blocking would hurt performance.

- API calls: `const data = await fetch(url).then(r => r.json());` for cleaner HTTP requests.[1]
- File operations: Reading/writing files in Node.js with `fs.promises`.
- Database queries: Async MongoDB/PostgreSQL interactions.
- Timers/intervals: `await new Promise(resolve => setTimeout(resolve, 1000));`.

Avoid in CPU-intensive tasks (use Web Workers) or fire-and-forget scenarios (prefer Promises).

## Python Use Cases

Apply async/await with `asyncio` for concurrent I/O, not parallel CPU work.

- Network requests: `data = await aiohttp.get(url)` or `await httpx.get(url)`.
- Database access: Async drivers like `asyncpg` or `databases`.
- Web servers: FastAPI/Starlette endpoints with `async def`.
- Concurrent tasks: `results = await asyncio.gather(*tasks)` for parallel I/O [ from prior].

Skip for sync libraries (use `asyncio.to_thread()`) or simple scripts without concurrency needs.

[1](https://blog.logrocket.com/async-await-typescript/)
[2](https://www.metered.ca/blog/async-await-in-typescript-a-step-by-step-guide/)
[3](https://www.freecodecamp.org/news/learn-async-programming-in-typescript-promises-asyncawait-and-callbacks/)
[4](https://dev.to/clifftech123/mastering-async-programming-in-typescript-promises-asyncawait-and-callbacks-148b)
[5](https://www.typescriptlang.org/play/javascript/modern-javascript/async-await.ts.html)
[6](https://www.w3schools.com/typescript/typescript_async.php) [7](https://www.youtube.com/watch?v=_zwNvruI6ds)
[8](https://basarat.gitbook.io/typescript/future-javascript/async-await) [9](https://www.youtube.com/watch?v=VcOMq3LQtBU)
[10](https://stackoverflow.com/questions/73437979/best-practice-for-async-await-in-typescript)
