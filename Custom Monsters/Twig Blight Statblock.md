---
statblock: true
image: [[twigblight.png]]
name: Twig Blight
source:
  - Monster Manual
  - Curse of Strahd
  - Lost Mine of Phandelver
  - Tales from the Yawning Portal
  - Ghosts of Saltmarsh
type: plant
subtype: ""
size: Small
alignment: neutral or evil
hp: 4
hit_dice: 1d6 + 1
ac: 13
speed: 20 ft.
stats:
  - 6
  - 13
  - 12
  - 4
  - 8
  - 3
damage_immunities: ""
damage_resistances: ""
damage_vulnerabilities: fire
condition_immunities: blinded, deafened
saves: []
skillsaves:
  - stealth: "3"
senses: blindsight 60 ft. (blind beyond this radius), passive Perception 9
languages: understands Common but can't speak
cr: 1/8
traits:
  - name: False Appearance
    desc: While the blight remains motionless, it is indistinguishable from a dead
      shrub.
actions:
  - name: Claws
    desc: Melee Weapon Attack +3 to hit, reach 5 ft., one target. 3 (1d4 + 1)
      piercing damage.
bonus_actions: []
reactions: []
legendary_actions: []
mythic_actions: []
spells: []

---

```statblock
monster: Twig Blight
```

```dataviewjs
dv.span(dv.current().file.name)
```