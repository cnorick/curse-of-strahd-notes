# Danger! Big Spoilers! Do Not Read
[Go here for no-spoiler session notes](https://cos.nathanorick.com/no-spoilers/campaign-notes/index.html)

## Session Notes
```dataviewjs
dv.list(dv.pages('"Session Notes"').file.link)
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
- [[Music Compiled]]
- [[Guest as Granny]]