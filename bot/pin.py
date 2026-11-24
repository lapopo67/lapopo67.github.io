import sys, textwrap
from PIL import Image, ImageDraw, ImageFont
W,H=1000,1500
F="/usr/share/fonts/opentype/inter/"
def font(n,s): return ImageFont.truetype(F+n,s)
def make(out, kicker, title, items, accent):
    im=Image.new("RGB",(W,H),"#fafbfc"); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,470],fill=accent)
    d.text((70,80),kicker.upper(),font=font("Inter-Bold.otf",34),fill="#ffffff")
    y=150
    for line in textwrap.wrap(title,16):
        d.text((70,y),line,font=font("InterDisplay-ExtraBold.otf",92),fill="#ffffff"); y+=104
    y=530
    for i,it in enumerate(items,1):
        d.rounded_rectangle([60,y,W-60,y+130],radius=24,fill="#ffffff",outline="#e4e7ec",width=3)
        d.ellipse([90,y+33,154,y+97],fill=accent)
        n=str(i); tw=d.textlength(n,font=font("Inter-Bold.otf",36))
        d.text((122-tw/2,y+42),n,font=font("Inter-Bold.otf",36),fill="#ffffff")
        d.text((185,y+38),it,font=font("Inter-SemiBold.otf",44),fill="#1d2433")
        y+=145
    d.rounded_rectangle([60,H-190,W-60,H-90],radius=50,fill="#f59e0b")
    t="Read the full guide  →"; tw=d.textlength(t,font=font("Inter-Bold.otf",42))
    d.text(((W-tw)/2,H-168),t,font=font("Inter-Bold.otf",42),fill="#1d1300")
    t="SmartPick Guide"; tw=d.textlength(t,font=font("Inter-Bold.otf",30))
    d.text(((W-tw)/2,H-70),t,font=font("Inter-Bold.otf",30),fill="#5b6475")
    im.save(out,optimize=True)
