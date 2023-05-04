```dataviewjs
dv.list(dv.pages('"Handouts"').sort(k => k.file.name).filter(k => k.protected).file.link)
```
