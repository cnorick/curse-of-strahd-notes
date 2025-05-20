# Danger! Big Spoilers! Do Not Read!
[Go here for no-spoiler session notes](https://cos.nathanorick.com/no-spoilers/campaign-notes/index.html)
[Handouts for this Session](https://cos.nathanorick.com/no-spoilers/campaign-notes/new-handouts.html)

Are you a DM running Curse of Strahd? Check out the [[README]] to download a copy of these notes for [Obsidian](https://obsidian.md/)

## Players
```dataviewjs
const table = dv.markdownTable(["PC", "Played By", "Website"], dv.pages('"Characters"').filter(c => c.pc).sort(c => c.name).map(c => [c.file.link, c.player, c.site]));

dv.paragraph(table);
```

## Session Notes
```dataviewjs
dv.list(dv.pages('"Session Notes"').sort().file.link)
```
## Session Prep
```dataviewjs
dv.list(dv.pages('"Session Prep"').sort().file.link)
```
## Locations
```dataviewjs
dv.list(dv.pages('"Locations"').sort(k => k.file.name).file.link)
```
## Characters
### NPCs
```dataviewjs
dv.list(dv.pages('"Characters"').filter(k => !k.pc).sort(k => k.file.name).file.link)
```
### PCs
```dataviewjs
dv.list(dv.pages('"Characters"').filter(k => k.pc).sort(k => k.file.name).file.link)
```
## Handouts
```dataviewjs
dv.list(dv.pages('"Handouts"').sort(k => k.file.name).file.link)
```
## Miscellaneous
```dataviewjs
	dv.list(dv.pages('"Misc"').filter(k => k.file.include_in_index != false).sort(k => k.file.name).file.link)
```
## Reference
```dataviewjs
	dv.list(dv.pages('"reference"').filter(k => k.file.path.split('/').length < 3).filter(k => k.file.include_in_index != false).sort(k => k.file.name).file.link)
```

