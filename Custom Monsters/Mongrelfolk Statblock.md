---
statblock: true
image: 
bestiary: true
name: Mongrelfolk
source:
  - Curse of Strahd
type: humanoid
subtype: mongrelfolk
size: Medium
alignment: any alignment
hp: 26
hit_dice: 4d8 + 8
ac: 11 (natural armor)
speed: 20 ft.
stats:
  - 12
  - 9
  - 15
  - 9
  - 10
  - 6
damage_immunities: ""
damage_resistances: ""
damage_vulnerabilities: ""
condition_immunities: ""
saves: []
skillsaves:
  - deception: "2"
  - perception: "2"
  - stealth: "3"
senses: passive Perception 12
languages: Common
cr: 1/4
traits:
  - name: Extraordinary Feature
    desc: |-
      The mongrelfolk has one of the following extraordinary features, determined randomly by rolling a d20 or chosen by the DM:
      1–3: Amphibious. The mongrelfolk can breathe air and water.
      4–9: Darkvision. The mongrelfolk has darkvision out to a range of 60 feet.
      10: Flight. The mongrelfolk has leathery wings and a flying speed of 40 feet.
      11–15: Keen Hearing and Smell. The mongrelfolk has advantage on Wisdom (Perception) checks that rely on hearing or smell.
      16–17: Spider Climb. The mongrelfolk can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.
      18–19: Standing Leap. The mongrelfolk's long jump is up to 20 feet and its high jump up to 10 feet, with or without a running start.
      20: Two-Headed. The mongrelfolk has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious.
  - name: Mimicry
    desc: The mongrelfolk can mimic any sounds it has heard, including voices. A creature that hears the sounds can tell they are imitations with a successful 12 Wisdom (Insight) check.
actions:
  - name: Multiattack
    desc: "The mongrelfolk makes two attacks: one with its bite and one with its claw or dagger."
  - name: Bite
    desc: Melee Weapon Attack +3 to hit, reach 5 ft., one target. 3 (1d4 + 1) piercing damage.
  - name: Claw
    desc: Melee Weapon Attack +3 to hit, reach 5 ft., one target. 3 (1d4 + 1) slashing damage.
  - name: Dagger
    desc: Melee / Ranged Weapon Attack +3 to hit, reach 5 ft. or range 20/60 ft., one target. 3 (1d4 + 1) piercing damage.
bonus_actions: []
reactions: []
legendary_actions: []
mythic_actions: []
spells: []
spellsNotes: ""
---

```statblock
creature: Mongrelfolk
```

```dataviewjs
dv.span(dv.current().file.name)
```