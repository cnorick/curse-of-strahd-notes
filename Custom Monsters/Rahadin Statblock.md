---
statblock: true
image: [[rahadin.jpeg]]
bestiary: true
name: Rahadin
source:
  - Curse of Strahd
type: humanoid
subtype: elf
size: Medium
alignment: lawful evil
hp: 135
hit_dice: 18d8 + 54
ac: 18 (studded leather armor)
speed: 35 ft.
stats:
  - 14
  - 22
  - 17
  - 15
  - 16
  - 18
damage_immunities: ""
damage_resistances: ""
damage_vulnerabilities: ""
condition_immunities: ""
saves:
  - constitution: "7"
  - wisdom: "7"
skillsaves:
  - deception: "8"
  - insight: "7"
  - intimidation: "12"
  - perception: "11"
  - stealth: "14"
senses: darkvision 60 ft., passive Perception 21
languages: Common, Elvish
cr: "10"
traits:
  - name: Deathly Choir
    desc: Any creature within 10 feet of Rahadin that isn't protected by a mind blank spell hears in its mind the screams of the thousands of people Rahadin has killed. As a bonus action, Rahadin can force all creatures that can hear the screams to make a 16 Wisdom saving throw. Each creature takes 16 (3d10) psychic damage on a failed save, or half as much damage on a successful one.
  - name: Fey Ancestry
    desc: Rahadin has advantage on saving throws against being charmed, and magic can't put him to sleep.
  - name: Mask of the Wild
    desc: Rahadin can attempt to hide even when he is only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.
actions:
  - name: Multiattack
    desc: Rahadin attacks three times with his scimitar, or twice with his poisoned darts.
  - name: Scimitar
    desc: Melee Weapon Attack +10 to hit, reach 5 ft., one target. 9 (1d6 + 6) slashing damage.
  - name: Poisoned Dart
    desc: Ranged Weapon Attack +10 to hit, range 20/60 ft., one target. 8 (1d4 + 6) piercing damage plus 5 (2d4) poison damage.
bonus_actions: []
reactions: []
legendary_actions: []
mythic_actions: []
spells:
  - "Rahadin's innate spellcasting ability is Intelligence. He can innately cast the following spells, requiring no components:"
  - 3/day each: misty step, phantom steed
  - 1/day each: magic weapon, nondetection
spellsNotes: ""
---

```statblock
creature: Rahadin
```

```dataviewjs
dv.span(dv.current().file.name)
```