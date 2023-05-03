Get the [pdf version](https://cos.nathanorick.com/no-spoilers/Campaign%20Notes.pdf)

## Handouts
### Images
```dataviewjs
dv.list(dv.pages('"Handouts/Images"').sort(k => k.file.name).filter(k => k.public).file.link)
```
```dataviewjs
dv.list(dv.pages('"Handouts/Items"').sort(k => k.file.name).filter(k => k.public).file.link)
```

```dataviewjs
dv.list(dv.pages('"Handouts/Items"').sort(k => k.file.name).filter(k => k.public).file.link)
```

```dataviewjs
dv.pages('"Session Notes"').forEach(p => {
	dv.header(2, p.file.name);
	const fullText = dv.fileLink(p.file.path, true);
	dv.paragraph(fullText);
})
```
