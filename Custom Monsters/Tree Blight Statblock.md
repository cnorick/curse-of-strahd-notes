---
statblock: true
image: ![[Tree Blight.png]]
name: Tree Blight
source:
  - Curse of Strahd
  - The Wild Beyond the Witchlight
type: plant
subtype: ""
size: Huge
alignment: neutral or evil
hp: 92
hit_dice: 8d12 + 40
ac: 15
speed: 30 ft.
stats:
  - 23
  - 10
  - 20
  - 6
  - 10
  - 3
damage_immunities: ""
damage_resistances: ""
damage_vulnerabilities: ""
condition_immunities: blinded, deafened
saves: []
skillsaves: []
senses: blindsight 60 ft. (blind beyond this radius), passive Perception 10
languages: understands Common and Druidic but doesn't speak
cr: "7"
traits:
  - name: False Appearance
    desc: While the blight remains motionless, it is indistinguishable from a dead tree.
  - name: Siege Monster
    desc: The blight deals double damage to objects and structures.
actions:
  - name: Multiattack
    desc: The blight makes one Branch attack and one Grasping Root attack.
  - name: Branch
    desc: Melee Weapon Attack +9 to hit, reach 15 ft., one target. 16 (3d6 + 6)
      bludgeoning damage.
  - name: Grasping Root
    desc: Melee Weapon Attack +9 to hit, reach 15 ft., one creature not grappled by
      the blight. The target is grappled (escape 15). Until the grapple ends,
      the target takes 9 (1d6 + 6) bludgeoning damage at the start of each of
      its turns. The root has AC 15 and can be severed by dealing 6 slashing
      damage or more to it at once. Cutting the root doesn't hurt the blight,
      but ends the grapple.
bonus_actions:
  - name: Bite
    desc: Melee Weapon Attack +9 to hit, reach 5 ft., one creature grappled by the
      blight. 19 (3d8 + 6) piercing damage.
reactions: []
legendary_actions: []
mythic_actions: []
spells: []
spellsNotes: ""
---

```statblock
monster: Tree Blight
```

```dataviewjs
```