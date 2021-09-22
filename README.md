# DPIAdjust
A simple Python program which allows a user to adjust the DPI of their mouse. 

As I said, it is a very simple program, it does not contain input validation and is not meant for super strenous (misspelled I know) tasks. Takes two inputs, the first for wait time, which is used to calculate the distacne the mouse moves. The next is the modifier, giving any value other than 1 for this inpur will adjust the DPI by that scale. 

Has not been tested with negative inputs

Has not been tested for gaming so it may or may not work for that

The program will close itself if the mouse intercepts the corners of the screen. I plan to try and fix this, and will edit this README once that has been completed

Higher modifiers tend to result in chunkier mouse movement though this can be offset to a degree with lower wait times

Execution can be halted to pressing ctrl + q at anytime (May need to hold the buttons for a bit so the program can register it properly)
