```dataviewjs
const files = dv.pages('"Session Notes"').file;
let text = '';
for(let i = 0; i < dvLinks.length; i++) {
	text = text + '!' + dvLinks[i] + '\n\n';
}
dv.paragraph(text)
```

