## People
```dataviewjs
dv.list(dv.pages('"Handouts/Images/Portraits"').sort(k => k.file.name).filter(k => k.new_handout).file.link)
```

## Places
```dataviewjs
dv.list(dv.pages('"Handouts/Images/Places"').sort(k => k.file.name).filter(k => k.new_handout).file.link)
```

## Items
```dataviewjs
dv.list(dv.pages('"Handouts/Images/Things"').sort(k => k.file.name).filter(k => k.new_handout).file.link)
dv.list(dv.pages('"Handouts/Items"').sort(k => k.file.name).filter(k => k.new_handout).file.link)
```

## Letters
```dataviewjs
dv.list(dv.pages('"Handouts/Letters"').sort(k => k.file.name).filter(k => k.new_handout).file.link)
```

## Maps
```dataviewjs
dv.list(dv.pages('"Handouts/Maps"').sort(k => k.file.name).filter(k => k.new_handout).file.link)
```




