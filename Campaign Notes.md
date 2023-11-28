## Quests
- [[Quests|List of Ongoing Quests]]

## Session Notes
```dataviewjs
dv.list(dv.pages('"Session Notes"').sort().file.link)
//dv.pages('"Session Notes"').forEach(p => {
//	dv.header(2, p.file.name);
//	const fullText = dv.fileLink(p.file.path, true);
//	dv.paragraph(fullText);
//})
```
## Handouts

### People
```dataviewjs
dv.list(dv.pages('"Handouts/Images/Portraits"').sort(k => k.file.name).filter(k => k.public).file.link)
```
### Places
```dataviewjs
dv.list(dv.pages('"Handouts/Images/Places"').sort(k => k.file.name).filter(k => k.public).file.link)
```
### Items
```dataviewjs
dv.list(dv.pages('"Handouts/Items"').sort(k => k.file.name).filter(k => k.public).file.link)
```
### Letters
```dataviewjs
dv.list(dv.pages('"Handouts/Letters"').sort(k => k.file.name).filter(k => k.public).file.link)
```
### Maps
```dataviewjs
dv.list(dv.pages('"Handouts/Maps"').sort(k => k.file.name).filter(k => k.public).file.link)
```
### Miscellaneous
```dataviewjs
dv.list(dv.pages('"Handouts/Misc"').sort(k => k.file.name).filter(k => k.public).file.link)
```
### Stat Blocks
```dataviewjs
dv.list(dv.pages('"Handouts/Stat Blocks"').sort(k => k.file.name).filter(k => k.public).file.link)
```

[[Unlisted Handouts|.]]
