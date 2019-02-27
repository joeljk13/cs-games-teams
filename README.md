# A series of scripts for generating CS Games teams using ILP

## Dependencies

- zsh
- glpsol (the actual ILP solver)
  - Likely any ILA solver that can read MPS format should work, although you
    may need to modify ./run to handle other output formats then
  - I know this is in the arch linux repositories; other linux distributions
    will probably have it too

## How to set up for a new CS Games

1. Get a table of people and preferences for categories. Preferences should be
   positive integers, lower means more preferred. Put some number <0 (e.g. -1)
   if someone cannot make a category, or isn't willing to do it. Duplicating
   numbers (e.g. having 2 first choices) is fine, and so is skipping numbers (e.g.
   putting 999 for a category that you'll do only if it's the only way to get the
   ILP to be solvable).
2. Make sure dependencies are installed.
3. Update the people and categories in ./run. Make sure to use a single, unique
   name for each person; use nicknames if you have to. Make sure to keep the
   ALL category.
4. Update the people and categories in ./cs.py. Make sure to use the same
   names here. The most involved part here is getting people's preferences in.
   I downloaded the google sheet we used and ran it through the ./format script
   to do this (maybe after some cleaning up of the spreadsheet). Updating the
   categories is a little tedious but straightforward.
5. Run the script! It should print out who is on each team, which categories
   each person is in, and for each category who is in that category for each
   team. Despite being an NP-complete problem, ILP solvers are really good, so
   it should only take a few seconds (if even) to run.
6. Try modifying the get_weight() function in ./cs.py, and re-running the
   script. This is the function that converts a person's preference for a given
   category to an weight for the ILP objective function. A linear function will
   work, but may not be optimal since people's preferences aren't usually
   linear. I've left the function that I think we ended up using for the 2018
   CS Games (IIRC I actually generated several options and let whoever was
   in the major's lab at the time vote, and it was unanimous that this was
   best)

If you want to add more conditions (e.g. person X and person Y shouldn't be on
the same team), that should be fairly easy to do in ./cs.py following the
logic of the other equations.
