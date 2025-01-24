---
statblock: true
name: Vampyr
image: [[Assets/Images/People/vampyr.jpg]]
type: Abberation (Dark Power)
size: large
alignment: Lawful Evil
ac: 19
hp: 300
speed: 30 ft, 60 ft flying
stats: [26, 14, 24, 22, 18, 24]
saves:
  - DEX: 8
  - WIS: 10
  - CHA: 13
skillsaves:
  - Deception: 13
  - Perception: 10
  - Stealth: 8
damage_resistances: bludgeoning, piercing, slashing from non-magical attacks
damage_immunities: necrotic, poison
condition_immunities: charmed, poisoned
senses: true sight 120ft, passive perception 20
languages: Deep Speech, Telepathy
cr: 20
traits:
  - name: Fear Aura
    desc: 20 ft DC 21 WIS save frightened until start of next turn, 24 hour immunity on success
  - name: Magic Resistance
    desc: You have advantage on saving throws against spells and other magical effects.
  - name: Legendary Resistance (3/day)
    desc: If you fail a saving throw, you can choose to succeed instead.
spells:
  - "Innate Spellcasting DC 21"
  - At will: Detect Magic, Fireball*
  - 3/day each: Blight, Greater Invisibility
  - "*(necrotic reskin) Darting imps that siphon life essence."
actions:
  - name: Multiattack
    desc: Vampyr makes four attacks, one with its' bite, two with its' claw, and one with its' tail
  - name: Bite
    desc: "+14 5ft must target grappled creature Hit: 22 (4d6+8) piercing damage. Target must succeed on a DC 21 CON save or become poisoned. While poisoned in this way, the target can't regain HP, and takes 21 (6d6) necrotic damage at the start of each of its' turns. Vampyr regains half the necrotic damage dealt. The poisoned creature can make the save again at the end of each of its' turns."
  - name: Claw
    desc: "+14 5ft 17 (2d8+8) slashing damage and 10 (3d6) necrotic damage. Vampyr can choose to grapple the target instead of dealing the bludgeoning damage (escape DC 22). Vampyr can have two creatures grappled at once, but needs a free hand to make a claw attack."
  - name: Tail
    desc: "+14 10ft 24 (3d10+8) piercing damage"
legendary_actions:
  - name: ''
    desc: Once per round, Vampyr can make a Wing Attack. Each creature within 15ft of Vampyr must succeed on a DC 22 DEX save or take 15 (2d6+8) bludgeoning damage and be knocked prone. Vampyr can then fly up to half its' movement speed without provoking attacks of oppurtunity.

---

```statblock
monster: Vampyr
```