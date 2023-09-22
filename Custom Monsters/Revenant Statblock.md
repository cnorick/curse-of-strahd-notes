---
statblock: true
name: Revenant
image: null
source:
  - Monster Manual
  - Curse of Strahd
  - Princes of the Apocalypse
  - Tomb of Annihilation
  - "Waterdeep: Dungeon of the Mad Mage"
type: undead
subtype: ""
size: Medium
alignment: neutral
hp: 136
hit_dice: 16d8 + 64
ac: 13
speed: 30 ft.
stats:
  - 18
  - 14
  - 18
  - 13
  - 16
  - 18
damage_immunities: poison
damage_resistances: necrotic, psychic
damage_vulnerabilities: ""
condition_immunities: charmed, exhaustion, frightened, paralyzed, poisoned, stunned
saves:
  - strength: "7"
  - constitution: "7"
  - wisdom: "6"
  - charisma: "7"
skillsaves: []
senses: darkvision 60 ft., passive Perception 13
languages: the languages it knew in life
cr: "5"
traits:
  - name: Regeneration
    desc: The revenant regains 10 hit points at the start of its turn. If the
      revenant takes fire or radiant damage, this trait doesn't function at the
      start of the revenant's next turn. The revenant's body is destroyed only
      if it starts its turn with 0 hit points and doesn't regenerate.
  - name: Rejuvenation
    desc: When the revenant's body is destroyed, its soul lingers. After 24 hours,
      the soul inhabits and animates another humanoid corpse on the same plane
      of existence and regains all its hit points. While the soul is bodiless, a
      wish spell can be used to force the soul to go to the afterlife and not
      return.
  - name: Turn Immunity
    desc: The revenant is immune to effects that turn undead.
  - name: Vengeful Tracker
    desc: The revenant knows the distance to and direction of any creature against
      which it seeks revenge, even if the creature and the revenant are on
      different planes of existence. If the creature being tracked by the
      revenant dies, the revenant knows.
actions:
  - name: Multiattack
    desc: The revenant makes two fist attacks.
  - name: Fist
    desc: Melee Weapon Attack +7 to hit, reach 5 ft., one target. 11 (2d6 + 4)
      bludgeoning damage. If the target is a creature against which the revenant
      has sworn vengeance, the target takes an extra 14 (4d6) bludgeoning
      damage. Instead of dealing damage, the revenant can grapple the target
      (escape 14) provided the target is Large or smaller.
  - name: Vengeful Glare
    desc: The revenant targets one creature it can see within 30 feet of it and
      against which it has sworn vengeance. The target must make a 15 Wisdom
      saving throw. On a failure, the target is paralyzed until the revenant
      deals damage to it, or until the end of the revenant's next turn. When the
      paralysis ends, the target is frightened of the revenant for 1 minute. The
      frightened target can repeat the saving throw at the end of each of its
      turns, with disadvantage if it can see the revenant, ending the frightened
      condition on itself on a success.
bonus_actions: []
reactions: []
legendary_actions: []
mythic_actions: []
spells: []
spellsNotes: ""
---

```statblock
monster: Revenant
```

```dataviewjs
```