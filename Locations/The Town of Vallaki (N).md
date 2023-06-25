---
aliases: [Vallaki, The Town of Vallaki]
---

## Laws
- No one shall speak Strahd's name out loud or carry written documents with his name on them
- No one shall speak poorly of the Baron or the festivals nor hold any documents that present either in an ill light
- Everyone shall take part in preparing the festivals
	- The Vallakians treat this sort of like Jury Duty
- Everyone shall attend the festivals
	- Every festival, guards go door to door and patrol the streets to make sure no one is missing out
	- Of course, they can't actually check everywhere, so hiding isn't impossible
	- But getting caught avoiding a festival is grounds for a steep punishment
- Regular laws apply
	- e.g. murdering a civilian would result in incarceration, but murdering a guard would mean execution
 
### Punishments
- Time in stocks between a day to a few weeks
- Seizure of assets
- Imprisonment at Vallaki's Reformation House
- Personal reformation conducted by [[Vargas Vallakovich|The Baron]]
	- He chooses a random dissenter and takes them to his mansion for hands-on torture
- public hanging
	- doesn't happen often, and reserved for severe dissenters that repeat offense

## Locations
### The Gates
>The Old Svalich Road meanders into a valley watched over by dark, brooding mountains to the north and south. The woods recede, revealing a sullen mountain burg surrounded by a wooden palisade. Thick fog presses up against this wall, as though looking for a way inside, hoping to catch the town aslumber.
>
>The dirt road ends at a set of sturdy iron gates with a pair of shadowy figures standing behind them. Planted in the ground and flanking the road outside the gates are a half-dozen pikes with wolves' heads impaled on them.

- A 15-foot-high wall encloses the town, its vertical logs held together with thick ropes and mortar. The top of each log has been sharpened to a point. Wooden scaffolding hugs the inside of the palisade twelve feet off the ground, enabling guards to peer over the wall there

- Three tall gates made of iron bars lead into town:
	- The north gate is sometimes called the Zarovich Gate, or "the gate to the lake," because it leads to Lake Zarovich (chapter 2, area L).
	- The west gate is referred to as the Sunset Gate, even though no living person in Vallaki has seen an undimmed sunset. A few abandoned cottages line the road outside this gate.
	- The east gate is also known as the Morning Gate, or, as some locals like to call it, the Mourning Gate.
- Heavy iron chains with iron padlocks keep the gates shut at night
	- During the day, the gates are closed but not typically locked
- Two town [[#Statblocks|wall guards]] stand just inside each gate
	- The guards greet all visitors with suspicion, particularly those who arrive at night
	- If the characters arrive at night, one or more of them must succeed on a DC 20 Charisma (Persuasion) check to convince the guards to unlock the gate and let them enter
- If trouble breaks out at one of the gates, the guards there cry out, "To arms!"
	- Their shouts are echoed across Vallaki, putting the entire town on alert within minutes
	- Vallaki has twenty-four human [[guard|guards]], half of whom are on duty at any given time
		- (six stand watch at the gates, six patrol the walls)
		- The town can also muster a militia of fifty able-bodied human [commoners]] armed with clubs, daggers, and torches.

## Maps
![[DM Map - Vallaki.jpg]]


## Statblocks
```statblock
extends: Guard
name: Wall Guard
actions:
  - name: Pike
    desc: "Melee or Ranged Weapon Attack: +3 to hit, reach 10 ft. or range 20/60 ft.,
      one target. Hit: 1d10+1 piercing damage. These weapons are long enough to stab creatures through the bars of the gate."
    attack_bonus: 3
    damage_dice: 1d10
    damage_bonus: 1
```
