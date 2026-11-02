# Coding Constructs (plan)

## ABSTRACTION
In designing my game, abstraction is key to helping me decide which features to include and which to
leave out. It allows me to focus on the core elements that make the game fun and functional, without
getting caught up in unnecessary details that don’t really add much to the gameplay. At the centre of the
game are the fundamental mechanics; things like character movement, jumping, climbing, avoiding
obstacles, collecting power-ups, fighting a final boss, and having clear win or lose screens. These are the
features that shape the player’s experience.
By keeping the focus on these core parts, I can build a game that feels complete and enjoyable, but also
manageable in terms of time and resources. I’ve chosen to leave out more complex features like online
multiplayer, branching storylines, cinematic cutscenes, and advanced graphics because they’re not
essential to how the game plays. While they might make the game more polished or visually impressive,
they’d take a lot more time to develop and don’t impact the core gameplay. This kind of abstraction helps
me stay focused on what really matters to the experience I want to create.

## DECOMPOSITION
Decomposition is all about breaking the project down into smaller, more manageable parts, and it plays a
big role in how I plan to build the game. Rather than trying to create everything all at once, I’m dividing the
game into clear components that I can work on individually. Each part will handle a specific piece of the
gameplay, which makes development a lot more organised and less overwhelming.
Some of the main components I’ll focus on include player control (handling keyboard inputs for
movement, jumping, and climbing), platform generation (making sure platforms appear logically and are
fair to the player), and obstacle behaviour (defining how obstacles move and interact with the player). I’ll
also be working on enemy logic, especially for the boss battle, and the power-up system that gives the
player temporary abilities. Other key areas are scoring, which updates based on the player’s
performance, and UI screens like menus, instructions, game-over, and win screens. Each of these pieces
can be built and tested separately before I bring them all together. This approach makes it easier to find
and fix bugs, test things as I go, and stay on top of the development process.

## THINKING LOGICALLY
Thinking logically is key to making sure the game behaves in a way that makes sense to the player. Every
mechanic needs to follow a clear set of rules, so players can understand how the game works and what
their actions will lead to. For example, if the player hits an obstacle, the game needs to detect that
collision, figure out the result (like ending the game or taking away a life), and then show the right screen.
The same goes for collecting power-ups; there has to be a condition that checks if the player touched the
item, applies its effect, and then removes it after a certain amount of time.
There are also logical decisions built into gameplay itself. Decisions should have meaningful
consequences and affect how the game unfolds, which helps keep it engaging. All of this relies on logical
conditions, rules, and transitions between different game states.

## THINKING CONCURRENTLY
Concurrency is important to my game because a lot of things need to happen at the same time without
interfering with each other. While the player is moving and jumping, enemies need to be moving
independently, obstacles need to appear or disappear, and power-up timers need to count down, all at
the same time. On top of that, background animations or music might be running too. All of these systems
need to stay in sync so the game feels smooth and responsive.
To make that happen, the game has to handle multiple processes at the same time. That might mean
using things like event loops to keep everything running together. If one part of the game slows down or
interrupts another, it can ruin the gameplay experience. So, I’ll need to make sure everything from player
inputs to enemy behaviour can work at the same time without causing problems. Managing concurrency
properly is key to making the game feel polished and fun to play.

## THINKING AHEAD
Players will interact with my game is through the keyboard. I’m keeping the control scheme simple and
easy to use. The arrow keys will control movement and climbing, while the spacebar will be used for
jumping. I might also include extra keys like Shift and Ctrl or Z and X to activate special actions or use
power-ups, depending on how gameplay changes.
Behind the scenes, the game will capture these inputs using an event-handling system that translates
them into actions like moving the character, jumping, or triggering animations. There will also be inputs
that come from inside the game itself. The score, for example, updates as the player collects items or
defeats enemies. A timer might track how long the player has to finish a level, and the overall game state
will change depending on whether the player is playing, has won, or lost. Together, all of these inputs
from the player and from within the game help make the game feel alive and responsive.
