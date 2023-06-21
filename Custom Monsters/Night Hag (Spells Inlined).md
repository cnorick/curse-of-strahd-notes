---
statblock: true
name: Night Hag with Spells Inlined
extends: Night Hag
spells:
- Shared Spellcasting: While all three members of a hag coven are within 30 feet of one another, they can each cast the following spells from the wizard's spell list but must share the spell slots among themselves. For casting these spells, each hag is a 12th-level spellcaster that uses Intelligence as her spellcasting ability. The spell save DC is 12+the hag's Intelligence modifier, and the spell attack bonus is 4+the hag's Intelligence modifier.
- 1st level (4 slots): identify, ray of sickness
- 2nd level (3 slots): hold person, locate object
- 3rd level (3 slots): bestow curse, counterspell, lightning bolt
- 4th level (3 slots): phantasmal killer, polymorph
- 5th level (2 slots): contact other plane, scrying
- 6th level (1 slot): eye bite
- Innate Spellcasting: The hag's innate spellcasting ability is Charisma (spell save DC 14, +6 to hit with spell attacks). She can innately cast the following spells, requiring no material components:
- At will: detect magic, magic missile
- 2/day each: plane shift (self only), ray of enfeeblement, sleep

    attack_bonus: 0
  - name: Hag Eye (Coven Only)
    desc: >-
      A hag coven can craft a magic item called a hag eye, which is made from a
      real eye coated in varnish and often fitted to a pendant or other wearable
      item. The hag eye is usually entrusted to a minion for safekeeping and
      transport. A hag in the coven can take an action to see what the hag eye
      sees if the hag eye is on the same plane of existence. A hag eye has AC
      10, 1 hit point, and darkvision with a radius of 60 feet. If it is
      destroyed, each coven member takes 3d10 psychic damage and is blinded for
      24 hours.

      A hag coven can have only one hag eye at a time, and creating a new one requires all three members of the coven to perform a ritual. The ritual takes 1 hour, and the hags can't perform it while blinded. During the ritual, if the hags take any action other than performing the ritual, they must start over.
    attack_bonus: 0
actions:
  - name: Claws (Hag Form Only)
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 +
      4) slashing damage."
    attack_bonus: 7
    damage_dice: 2d8
    damage_bonus: 4
  - name: Change Shape
    desc: The hag magically polymorphs into a Small or Medium female humanoid, or
      back into her true form. Her statistics are the same in each form. Any
      equipment she is wearing or carrying isn't transformed. She reverts to her
      true form if she dies.
    attack_bonus: 0
  - name: Etherealness
    desc: The hag magically enters the Ethereal Plane from the Material Plane, or
      vice versa. To do so, the hag must have a heartstone in her possession.
    attack_bonus: 0
  - name: Nightmare Haunting (1/Day)
    desc: While on the Ethereal Plane, the hag magically touches a sleeping humanoid
      on the Material Plane. A protection from evil and good spell cast on the
      target prevents this contact, as does a magic circle. As long as the
      contact persists, the target has dreadful visions. If these visions last
      for at least 1 hour, the target gains no benefit from its rest, and its
      hit point maximum is reduced by 5 (1d10). If this effect reduces the
      target's hit point maximum to 0, the target dies, and if the target was
      evil, its soul is trapped in the hag's soul bag. The reduction to the
      target's hit point maximum lasts until removed by the greater restoration
      spell or similar magic.
    attack_bonus: 0
monster: Night Hag


---

```statblock
monster: Dog
```

```dataviewjs
```