 # Fallout-2d20-Character-Creator

A program to automate character creation and management the Fallout Tabletop Roleplaying Game (Fallout 2d20) by Modiphius Entertainment. Started as a passion project for making my life as a Fallout 2d20 GM easier, now intended to be an (open-source?) tool for the Fallout 2d20 community.


## Authors

- [@bledoux2002](https://www.github.com/bledoux2002)


## Roadmap

- Error handling (don't assume everything will go fine), high priority

- When editting character files, make a copy of the file to be editted, so changes can be undone, and file corruption safeguard, high priority (began implementation, need to reincorporate as a temporary duplicate file)

- editChar(str:file) function, allowing the user to change aspects in a character file, high priority (basic funcitonality done, perk/skill/invetory mgmt still in development)

- printChar(str:file) function, which neatly displays the contents of a character file w/o tons of brackets and indentation, medium priority (basic features done, SPECIAL still ugly and perks/skills/invetory not implemented yet)

- Complete Perks list in `data.json`, low priority, (partially done, enough already to use for dev purposes)

- Complete Equipment Packs list in `data.json`, low priority (nothing done yet but will be necessary in future as editChar is developed)

- Clean up file structure diagram in README Layout, low priority (not super necessary)

- Begin website development and integration, low priority (implement as terminal program first)

- Begin Unity project for local visual implementation, low priority (implement as terminal program first, website is more ideal implementation for community)

## Layout

- main, for primary program to be run

- \backup, stores copies of the main JSON files in case of corruption during operation. the data in these shouldn't change much, except for settings.json, so hard-coded backups should be fine, may include \characters subfolder for future character backups

- \characters, stores character JSON files