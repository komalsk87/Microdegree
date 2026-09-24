import asyncio
import time

async def call_llm(prompt: str, delay: float) -> str:
    """Pretend to call an LLM API that takes `delay` seconds."""
    print(f"Sending: {prompt}")
    await asyncio.sleep(delay)
    print(f"Received response for: {prompt}")
    return f"Response to: {prompt}"

async def main():
    start = time.perf_counter()

    result1 = await call_llm("What is Python?", 0.2)
    result2 = await call_llm("What is async?", 0.3)
    result3 = await call_llm("What is an LLM?", 0.1)

    elapsed = time.perf_counter() - start
    print(result1)
    print(result2)
    print(result3)
    print(f"Sequential: {elapsed:.1f} seconds")  # ~0.6 seconds

asyncio.run(main())