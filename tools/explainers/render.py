import asyncio, subprocess, sys, time
from playwright.async_api import async_playwright
FPS = 30
async def main(src, out, timeline=None):
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await br.new_page(viewport={"width":1920,"height":1080})
        if timeline:  # narrated version: cue times come from the narration
            await pg.add_init_script("window.TIMELINE = " + open(timeline).read() + ";")
        await pg.goto("file://" + src)
        dur = await pg.evaluate("DURATION")
        n = int(dur * FPS)
        ff = subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-",
                               "-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-movflags","+faststart", out], stdin=subprocess.PIPE)
        t0 = time.time()
        for i in range(n):
            await pg.evaluate(f"render({i / FPS})")
            ff.stdin.write(await pg.screenshot(type="jpeg", quality=92))
            if i % 300 == 0: print(i, n, round(time.time()-t0), flush=True)
        ff.stdin.close(); ff.wait()
        await br.close()
args = sys.argv[1:]
tl = args[args.index("--timeline") + 1] if "--timeline" in args else None
asyncio.run(main(args[0], args[1], tl))
