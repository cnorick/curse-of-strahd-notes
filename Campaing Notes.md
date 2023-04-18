```dataviewjs
dv.pages('"Session Notes"').forEach(p => {
	dv.header(2, p.file.name);
	dv.paragraph(dv.fileLink(p.file.path, true));
})
```

