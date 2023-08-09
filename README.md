# Fallout-2d20-Character-Creator

Automate the character creation process for the Fallout Tabletop Roleplaying Game, Fallout 2d20, by Modiphius Entertainment.


## Authors

- [@bledoux2002](https://www.github.com/bledoux2002)


## Roadmap

- Error handling (don't assume everything will go fine), high priority

- Backups folder (both data files and character files), high priority (can't have ppl losing their characters or me losing my code)

- When editting character files, make a copy of the file to be editted, so changes can be undone, and file corruption safeguard, high priority (ben being big brain)

- editChar(str:file) function, allowing the user to change aspects in a character file, high priority

- printChar(str:file) function, which neatly displays the contents of a character file w/o tons of brackets and indentation, medium priority (makes everything look way nicer but not really necessary. should be done for release)

- copyChar(str:file) function, which creates a copy of the given character file, medium priority (QoL, not necessary but could be nice in niche situations)

- Complete Perks list in `data.json`, low priority, (enough already to use for dev purposes)

- Complete Equipment Packs list in `data.json`, low priority (nothing done yet but will be necessary in future as editChar is developed)

- Clean up file structure diagram in Layout, low priority (not super necessary)

- Begin website development and integration, low priority (implement as local program first)

- Begin Unity project for local visual implementation, low priority (implement as local program first)

## Layout

- main, for primary program to be run

- \backup, stores copies of the main JSON files in case of corruption during operation. the data in these shouldn't change much, except for settings.json, so hard-coded backups should be fine, may have \characters subfolder for character backups

- \characters, stores character JSON files