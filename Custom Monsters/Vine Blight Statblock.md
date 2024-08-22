---
statblock: true
image: [[vineblight.png]]
name: Vine Blight
source:
  - Monster Manual
  - Curse of Strahd
  - Ghosts of Saltmarsh
type: plant
subtype: ""
size: Medium
alignment: neutral or evil
hp: 26
hit_dice: 4d8 + 4
ac: 12
speed: 10 ft.
stats:
  - 15
  - 8
  - 14
  - 5
  - 10
  - 3
damage_immunities: ""
damage_resistances: ""
damage_vulnerabilities: ""
condition_immunities: blinded, deafened
saves: []
skillsaves:
  - stealth: "1"
senses: blindsight 60 ft. (blind beyond this radius), passive Perception 10
languages: Common
cr: 1/2
traits:
  - name: False Appearance
    desc: While the blight remains motionless, it is indistinguishable from a tangle
      of vines.
actions:
  - name: Constrict
    desc: Melee Weapon Attack +4 to hit, reach 10 ft., one target. 9 (2d6 + 2)
      bludgeoning damage, and a Large or smaller target is grappled (escape 12).
      Until this grapple ends, the target is restrained, and the blight can't
      constrict another target.
  - name: Entangling Plants (Recharge 5-6)
    desc: Grasping roots and vines sprout in a 15-foot radius centered on the
      blight, withering away after 1 minute. For the duration, that area is
      difficult terrain for nonplant creatures. In addition, each creature of
      the blight's choice in that area when the plants appear must succeed on a
      12 Strength saving throw or become restrained. A creature can use its
      action to make a 12 Strength check, freeing it self or another entangled
      creature within reach on a success.
bonus_actions: []
reactions: []
legendary_actions: []
mythic_actions: []
spells: []
spellsNotes: ""
---

```statblock
monster: Vine Blight
```

```dataviewjs
dv.span(dv.current().file.name)
```