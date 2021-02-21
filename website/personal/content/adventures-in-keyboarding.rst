Adventures in Keyboarding
#########################
:date: 2015-07-24 13:56
:status: published
:category: Misc.

`Part II <https://patricksanan.com/personal/adventures-in-keyboarding-part-ii/>`__
`Part III <https://patricksanan.com/personal/adventures-in-keyboarding-part-iii/>`__

I never learned to touch type.

I spend most of my day at the computer, and my job involves writing a lot of code. I could actually type very quickly, using a technique which evolved out of hunt-and-peck to a free-wheeling 6-fingered style that somehow wore out the letters on the A, S, and C keys on my laptop (computer nerds seemed impressed, but I don't think they knew my shame). If unable to look at the keyboard periodically, my accuracy suffered massively.

I realized that not looking at what I was typing on screen was wasting my time as I sent typo-riddled C source to my compiler, and irritating my girlfriend as her chat messages floated away, unread, while I looked down at my hands like a caveman. Enough was finally enough.

Down with QWERTY
---------------------------

 |Sholes_typewriter|

 `The first QWERTY typewriter <https://en.wikipedia.org/wiki/Typewriter#Sholes_and_Glidden_Type-writer>`__, from 1873

I decided almost immediately that I would learn an alternate keyboard layout. The first reason was simply that I have always been interested; the idea that everyone uses an inefficient layout annoys me. The second reason was that I had spent well over a decade using a completely non-standard way of typing, and burning that out of my brain seemed harder than learning a new layout, never looking down. Finally, since I intend to be typing for several hours a day for the rest of my life, it wouldn't hurt to start now with a layout which many claim is less stressful on the body. The major downside to using a nonstandard layout is that it is not the universal default, and in practice there are situations in which you can't use it (someone else's machine where you can't mess with the settings, logging into your own machine in root mode, etc.)

Attempt 1: Dvorak
-------------------------------

 |2000px-KB_United_States_Dvorak.svg|

 The (simplified) Dvorak layout

Dvorak is the most popular alternative to QWERTY. It has been around since the 1930s and is supported out-of-the-box by most operating systems, so it seemed a natural thing to try first. I spent many hours practicing on the excellent `keybr.com <http://www.keybr.com>`__ (which lets you use alternate layouts without changing your system settings), but my fingers never stopped hurting. The big killers are the letters I and L. I is extremely common, yet it is located in the middle column of the keyboard. It is on the home row, yes, but in a place which is harder to reach than many keys on the top and bottom rows, in my opinion. L is strangely placed on the top row for the right pinky. This is a very common letter and this movement never stopped feeling awkward. Further, most of the symbols move and shortcuts like QWASZXCV, all on the left with the QWERTY layout, hence convenient to use with a mouse, are scattered. I never had the confidence to go cold turkey and switch my computers to permanently use this layout.

Attempt 2: Workman
----------------------------------

 |Workman_keyboard_layout|

 The Workman layout

I noticed Workman as a layout option on keybr.com and read about it on the `Workman website <http://www.workmanlayout.com/blog>`__ (which is the place to go to learn more, including how to use the layout on your computer). I think that it was designed on some very solid principles, and is a layout I would recommend (for writing in English, coming from QWERTY). Most importantly, it recognizes that the easiest keys to reach are the 8 under your fingers in the home position, but after that it's less strain to push the keys on the top row above your middle and ring fingers, and the keys on the bottom row below your index fingers. These positions hold ASHTNEOIDRUPCL, the most common letters. The middle column home row keys hold GY, as opposer to ID with Dvorak. Important shortcuts are preserved on the left side of the keyboard, and many are even in the exact same place: QASZX. C and V are shifted over by one, which takes some getting used to. Finally, the rest of the keyboard is left alone - all the non-letter characters remain in the same positions.

The learning curve for this layout is much gentler than Dvorak, my hands feel comfortable using it, and after a couple of weeks of training with keybr.com, I changed my computers to use the layout and haven't looked back.

Vim and Workman
----------------------------
| I use Vim as a text editor, and a big problem for me was that the HJKL keys, which are used in vim as the arrow keys, are scattered. Unlike other commands, these are burned into my brain by *position*, not mnemonic. That is, the fact that W moved is okay, because I think of it as 'next **w**\ ord', but this does not hold for the movement keys. So, I modified `another key mapping developed to solve this problem <https://axiomatic.neophilus.net/posts/2013-08-13-workman-layout-for-vim.html>`__ and added the following to my ``~/.vimrc``. This is arguably better than standard vim because now the movement keys are under the home positions of the fingers, NEOI, not shifted over, so ones hand can remain in the home position.
| ``" [Workman] " neoi under the right hand is mapped to hjkl " for easy navigation without shifting the hand " " n --> h " e --> j " o --> k " i --> l " " The displaced commands are remapped as follows " " h --> i (insert "here") " j --> n ("jump" to next) " k --> e " l --> o (open "line") " " relevant keys are also remapped in visual mode nnoremap n h vnoremap n h nnoremap N H``

| nnoremap e j
| vnoremap e j
| nnoremap E J

| nnoremap o k
| vnoremap o k
| nnoremap O K

| nnoremap i l
| vnoremap i l
| nnoremap I L

| nnoremap h i
| nnoremap H I
| vnoremap H I

| nnoremap j n
| nnoremap J N

| nnoremap k e
| nnoremap K E

| nnoremap l o
| nnoremap L O

Advice
----------------------
| I am still in the process of getting fully up to speed, but I am already as fast with Workman as I was with QWERTY, and am able to touch-type now. I will add more tips here as I become more expert.

-  Use a training program (I used `keybr.com <http://keybr.com>`__ and `Peter's tutorial <http://www.typing-lessons.org/>`__, but there are many to choose from). I personally find that while I improve by simply working with the layout, I am not disciplined enough to practice the correct technique and focus on accuracy. Practice using a program where you must delete incorrect characters yourself, and also do some "sudden death" training, where any mistake triggers a restart.
-  Never. Look. Down. This is difficult sometimes (especially with keys far from the home row), but is the only way to obtain the real benefits of touch typing.
-  Go. Slowly. If you are making errors, you are going too fast. The tradeoff between speed and accuracy is a false one: if you want to go really quickly, having to stop and delete slows you down.
-  Use a regular pace - "bursts" lead to errors in my experience.
-  Use only the new layout as soon as possible. Once you know where all the keys are without looking, just go for it!
-  Keep your wrists off the table, and don't mash the keys: "float"
-  For more, see `these useful guidelines from Peter's tutorial <http://www.typing-lessons.org/preliminaries_2.html>`__.

.. |Sholes_typewriter| image:: images/old_posts/2015/07/sholes_typewriter.jpg?w=265
   :width: 265px
   :height: 300px
   :target: images/old_posts/2015/07/sholes_typewriter.jpg
.. |2000px-KB_United_States_Dvorak.svg| image:: images/old_posts/2015/07/2000px-kb_united_states_dvorak-svg.png?w=300
   :width: 500px
   :height: 167px
   :target: images/old_posts/2015/07/2000px-kb_united_states_dvorak-svg.png
.. |Workman_keyboard_layout| image:: images/old_posts/2015/07/workman_keyboard_layout.png?w=300
   :width: 500px
   :height: 167px
   :target: images/old_posts/2015/07/workman_keyboard_layout.png
