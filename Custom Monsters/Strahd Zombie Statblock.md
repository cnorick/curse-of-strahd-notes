---
statblock: true
image: null
name: Strahd Zombie
source:
  - Curse of Strahd
type: undead
size: Medium
alignment: unaligned
hp: 30
hit_dice: 4d8 + 12
ac: 8
speed: 20 ft.
stats:
  - 13
  - 6
  - 16
  - 3
  - 6
  - 5
damage_immunities: poison
damage_resistances: ""
damage_vulnerabilities: ""
condition_immunities: poisoned
saves:
  - wisdom: "0"
skillsaves: []
senses: darkvision 60 ft., passive Perception 8
languages: understands the languages it knew in life but can't speak
cr: "1"
traits:
  - name: Loathsome Limbs
    desc: >-
      Whenever the zombie takes at least 5 bludgeoning or slashing damage at one
      time, roll a d20 to determine what else happens to it:

      1–8: One leg is severed from the zombie if it has any legs left.

      9–16: One arm is severed from the zombie if it has any arms left.

      17–20: The zombie is decapitated.

      If the zombie is reduced to 0 hit points, all parts of it die. Until then, a severed part acts on the zombie's initiative and has its own action and movement. A severed part has AC 8. Any damage it takes is subtracted from the zombie's hit points.

      A severed leg is unable to attack and has a speed of 5 feet.

      A severed arm has a speed of 5 feet and can make one claw attack on its turn, with disadvantage on the attack roll. Each time the zombie loses an arm, it loses a claw attack.

      If its head is severed, the zombie loses its bite attack and its body is blinded unless the head can see it. The severed head has a speed of 0 feet. It can make a bite attack, but only against a target in its space.

      The zombie's speed is halved if it's missing a leg. If it loses both legs, it falls prone. If it has both arms, it can crawl. With only one arm, it can still crawl, but its speed is halved. With no arms or legs, its speed is 0 feet, and it can't benefit from bonuses to speed.
actions:
  - name: Multiattack
    desc: "The zombie makes three attacks: one with its bite and two with its claws."
  - name: Bite
    desc: Melee Weapon Attack +3 to hit, reach 5 ft., one target. 3 (1d4 + 1)
      piercing damage.
  - name: Claw
    desc: Melee Weapon Attack +3 to hit, reach 5 ft., one target. 4 (1d6 + 1)
      slashing damage.
bonus_actions: []
reactions: []
legendary_actions: []
mythic_actions: []
spells: []
spellsNotes: ""
---

```statblock
monster: Strahd Zombie
```