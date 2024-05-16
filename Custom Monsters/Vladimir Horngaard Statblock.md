---
statblock: true
image: null
name: Vladimir Horngaard
source:
  - Curse of Strahd
type: undead
subtype: ""
size: Medium
alignment: lawful or evil
hp: 192
hit_dice: 16d8 + 64
ac: 17
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
languages: Common, Draconic
cr: "7"
traits:
  - name: Regeneration
    desc: Vladimir regains 10 hit points at the start of his turn. If he takes fire
      or radiant damage, this trait doesn't function at the start of his next
      turn. Vladimir's body is destroyed only if he starts his turn with 0 hit
      points and doesn't regenerate.
  - name: Rejuvenation
    desc: When Vladimir's body is destroyed, his soul lingers. After 24 hours, the
      soul inhabits and animates another corpse on the same plane of existence
      and regains all its hit points. While the soul is bodiless, a wish spell
      can be used to force the soul to go to the afterlife and not return.
  - name: Special Equipment
    desc: "Vladimir wields a +2 greatsword with a hilt sculpted to resemble silver
      dragon wings and a pommel shaped like a silver dragon's head clutching a
      black opal between its teeth. "
  - name: Turn Immunity
    desc: Vladimir is immune to effects that turn undead.
  - name: Vengeful Tracker
    desc: Vladimir knows the distance to and direction of Strahd, even if Strahd and
      Vladimir are on different planes of existence. If Strahd is destroyed,
      Vladimir knows.
actions:
  - name: Multiattack
    desc: Vladimir makes two fist attacks or two attacks with his +2 Greatsword.
  - name: Fist
    desc: Melee Weapon Attack +7 to hit, reach 5 ft., one target. 11 (2d6 + 4)
      bludgeoning damage. Strahd, the target of Vladimir's sworn vengeance,
      takes an extra 14 (4d6) bludgeoning damage. Instead of dealing damage,
      Vladimir can grapple the target (escape 14) provided the target is Large
      or smaller.
  - name: Greatsword +2
    desc: Melee Weapon Attack +9 to hit, reach 5 ft., one target. 20 (4d6 + 4)
      slashing damage. Against Strahd, Vladimir deals an extra 14 (4d6) slashing
      damage with this weapon.
  - name: Vengeful Glare
    desc: Vladimir can target Strahd within 30 feet provided he can see Strahd.
      Strahd must make a 15 Wisdom saving throw. One a failure, Strahd is
      paralyzed until Vladimir deals damage to him, or until the end of
      Vladimir's next turn. When the paralysis ends, Strahd is frightened of
      Vladimir for 1 minute. Strahd can repeat the saving throw at the end of
      each of his turns, with disadvantage if he can see Vladimir, ending the
      frightened condition on itself on a success.
bonus_actions: []
reactions: []
legendary_actions: []
mythic_actions: []
spells: []
spellsNotes: ""
---

```statblock
monster: Vladimir Horngaard
```

```dataviewjs
dv.span(dv.current().file.name)
```