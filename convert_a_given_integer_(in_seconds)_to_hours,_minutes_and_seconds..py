s=int(input())
hr=s//3600
mn=(s-(3600*hr))//60
sec=(s-(3600*hr)-(mn*60))
print(f"H:M:S-{hr}:{mn}:{sec}")