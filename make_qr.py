"""Usage: python3 make_qr.py https://your-live-site-url
Needs: pip3 install segno
"""
import sys
import segno

url = sys.argv[1]
qr = segno.make(url, error="q")
qr.save("qr.png", scale=16, border=4)
qr.save("qr.svg", scale=16, border=4)
print("Saved qr.png and qr.svg for", url)
