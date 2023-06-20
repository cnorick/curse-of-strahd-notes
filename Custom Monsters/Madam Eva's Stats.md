---
statblock: true
name: Madam Eva
size: medium
type:
  type: humanoid
  tags:
  - human
source: CoS
alignment:
- C
- N
ac: 10
hp: 88
speed: 20
stats: [8,
dex: 11
con: 12
int: 17
wis: 20
cha: 18
save:
  con: "+5"
skill:
  arcana: "+7"
  deception: "+8"
  insight: "+13"
  intimidation: "+8"
  perception: "+9"
  religion: "+7"
passive: 19
languages:
- Abyssal
- Common
- Elvish
- Infernal
cr: '10'
spellcasting:
- name: Spellcasting
  headerEntries:
  - 'Madam Eva is a 16th-level spellcaster. Her spellcasting ability is Wisdom (spell
    save {@dc 17}, {@hit 9} to hit with spell attacks). Madam Eva has the following
    cleric spells prepared:'
  spells:
    '0':
      spells:
      - "{@spell light}"
      - "{@spell mending}"
      - "{@spell sacred flame}"
      - "{@spell thaumaturgy}"
    '1':
      slots: 4
      spells:
      - "{@spell bane}"
      - "{@spell command}"
      - "{@spell detect evil and good}"
      - "{@spell protection from evil and good}"
    '2':
      slots: 3
      spells:
      - "{@spell lesser restoration}"
      - "{@spell protection from poison}"
      - "{@spell spiritual weapon}"
    '3':
      slots: 3
      spells:
      - "{@spell create food and water}"
      - "{@spell speak with dead}"
      - "{@spell spirit guardians}"
    '4':
      slots: 3
      spells:
      - "{@spell divination}"
      - "{@spell freedom of movement}"
      - "{@spell guardian of faith}"
    '5':
      slots: 2
      spells:
      - "{@spell greater restoration}"
      - "{@spell raise dead}"
    '6':
      slots: 1
      spells:
      - "{@spell find the path}"
      - "{@spell harm}"
      - "{@spell true seeing}"
    '7':
      slots: 1
      spells:
      - "{@spell fire storm}"
      - "{@spell regenerate}"
    '8':
      slots: 1
      spells:
      - "{@spell earthquake}"
  ability: wis
  type: spellcasting
action:
- name: Dagger
  entries:
  - "{@atk mw} {@hit 4} to hit, reach 5 ft., one target. {@h}2 ({@damage 1d4}) piercing
    damage."
- name: Curse (Recharges after a Long Rest)
  entries:
  - Madam Eva targets one creature that she can see within 30 feet of her. The target
    must succeed on a {@dc 17} Wisdom saving throw or be cursed. While cursed, the
    target is {@condition blinded} and {@condition deafened}. The curse lasts until
    ended with a greater restoration spell, a {@spell remove curse} spell, or similar
    magic. When the curse ends, Madam Eva takes {@dice 5d6} psychic damage.
- name: Evil Eye (Recharges after a Short or Long Rest)
  entries:
  - 'Madam Eva targets one creature that she can see within 10 feet of her and casts
    one of the following spells on the target (save {@dc 17}), requiring neither somatic
    nor material components to do so: {@spell animal friendship}, {@spell charm person},
    or {@spell hold person}. If the target succeeds on the initial saving throw, Madam
    Eva is {@condition blinded} until the end of her next turn. Once a target succeeds
    on a saving throw against this effect, it is immune to the Evil Eye power of all
    Vistani for 24 hours.'
page: 233
languageTags:
- AB
- C
- E
- I
spellcastingTags:
- CC
damageTags:
- P
miscTags:
- MW
---

```statblock
monster: Madam Eva
```
