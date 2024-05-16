---
statblock: true
image: null
name: Phantom Warrior
source:
  - Curse of Strahd
type: undead
subtype: ""
size: Medium
alignment: any alignment
hp: 45
hit_dice: 6d8 + 18
ac: 16
speed: 30 ft.
stats:
  - 16
  - 11
  - 16
  - 8
  - 10
  - 15
damage_immunities: cold, necrotic, poison
damage_resistances: bludgeoning, piercing, slashing from nonmagical attacks
damage_vulnerabilities: ""
condition_immunities: charmed, exhaustion, frightened, grappled, paralyzed,
  petrified, poisoned, prone, restrained
saves: []
skillsaves:
  - perception: "2"
  - stealth: "4"
senses: darkvision 60 ft., passive Perception 12
languages: any languages it knew in life
cr: "3"
traits:
  - name: Ethereal Sight
    desc: The phantom warrior can see 60 feet into the Ethereal Plane when it is on
      the Material Plane, and vice versa.
  - name: Incorporeal Movement
    desc: The phantom warrior can move through other creatures and objects as if
      they were difficult terrain. It takes 5 (1d10) force damage if it ends its
      turn inside an object.
  - name: Spectral Armor and Shield
    desc: The phantom warrior's AC accounts for its spectral armor and shield.
actions:
  - name: Multiattack
    desc: The phantom warrior makes two attacks with its spectral longsword.
  - name: Spectral Longsword
    desc: Melee Weapon Attack +5 to hit, reach 5 ft., one target. 7 (1d8 + 3) force
      damage.
  - name: Etherealness
    desc: The phantom warrior enters the Ethereal Plane from the Material Plane, or
      vice versa. It is visible on the Material Plane while it is in the Border
      Ethereal, and vice versa, yet it can't affect or be affected by anything
      on the other plane.
bonus_actions: []
reactions: []
legendary_actions: []
mythic_actions: []
spells: []
spellsNotes: ""
---

```statblock
monster: Phantom Warrior
```

```dataviewjs
dv.span(dv.current().file.name)
```