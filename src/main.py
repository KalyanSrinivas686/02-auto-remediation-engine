import asyncio
from watcher import EventWatcher

async def main():
    watcher = EventWatcher()
    await watcher.watch()

if __name__ == "__main__":
    asyncio.run(main())
