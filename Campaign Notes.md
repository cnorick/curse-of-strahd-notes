```dataviewjs
dv.pages('"Session Notes"').forEach(p => {
	dv.header(2, p.file.name);
	const fullText = dv.fileLink(p.file.path, true);
	dv.paragraph(fullText);
})
```