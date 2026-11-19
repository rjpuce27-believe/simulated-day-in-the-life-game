# Simulated Day in the Life Game

## How to Play

This is a text-based Python game where you make decisions throughout a typical day and see how productive you are. To start, run the Python program and enter your name. The game will guide you through waking up, your morning routine, classes, an unexpected challenge, and your afternoon.

Read each question and type the requested answer or menu number, then press Enter. Some choices earn productivity points, while others subtract points. During the morning and afternoon, you can complete several activities, but you cannot choose the same activity twice within that routine. After each activity, you can choose whether to do something else or move on. If you choose to study in the afternoon, you will answer additional questions about your study session. Some events are randomly selected, so the game may be a little different each time.

At the end, the game displays your total productivity score. A score of 20 or more means you had a productive day and win; a lower score means you lose, with feedback about how the day went.

## How Player State Is Represented

I represent the player's state mainly with a variable called score, which starts at 0 and changes based on the player's decisions. Each part of the day is handled by a function that receives the current score, updates it, and returns it. This allows the score to carry over from one part of the game to the next.

I also use a completed_activities list in the morning and afternoon functions to remember which activities the player has already chosen. This prevents players from repeating the same activity to collect extra points. I chose a numerical score because it is a simple way to measure productivity across the whole day, and a list makes it easy to track completed activities.