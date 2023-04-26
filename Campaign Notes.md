Get the [pdf version](https://cos.nathanorick.com/no-spoilers/Campaign%20Notes.pdf)

## Handouts
```dataviewjs
dv.list(dv.pages('"Items/Handouts"').sort(k => k.file.name).file.link)
```

```dataviewjs
dv.pages('"Session Notes"').forEach(p => {
	dv.header(2, p.file.name);
	const fullText = dv.fileLink(p.file.path, true);
	dv.paragraph(fullText);
})
```
