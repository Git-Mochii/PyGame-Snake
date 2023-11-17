# PyGame-Snake

This is a game that I made using the "pygame" import, the game is called Snake.

The program is fully inspired by the original classic snake game. The program window is prefixed to a set resolution to enable the grid layout
to work properly, furthermore, there is no start menu or game-over menu due to the fact I felt like it was overrated (although this may be subject
to change in the future).

How To Play
===========

- The game instantly starts upon running the code
- To navigate the snake (Green pixel blob), use the arrow keys
- To gain length and score, collect the red pixel food
- To make the game unique and slightly more difficult compared to regular snake (because of course why should it be easy),
  every 3 red block foods collected makes the game framerate increase + 1 (Default at 5)
- The snake dies by reversing into itself or by hitting the edge of the window, this does not make the game end but does reset
  the length of the snake however it keeps the framerate speed (meaning if a user were to reach 15fps and die, the snake length
  resets to two blocks length however the framerate remains at 15fps thus making it gradually more difficult to gain length as the
  snake continues to accelerate)
- There is a scoring system to indicate how many red-block foods have been collected in that specific run of the game
  
[Why add this difficulty feature? Because it makes the game a little more fun and unpredictable]

Known Bugs
==========
I invite anyone to fix these issues and submit a request to create and upload a "bugless" program.

1. The two-long block snake is able to reverse using the back arrow key

Potential Future Features
=========================

1. Adding a start screen and game-over screen

(All things considered, I want that program to remain a bit silly - specifically the difficulty feature)

---------
[Imported repo from old account]
---------
