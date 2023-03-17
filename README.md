# Binary Search Algorithm

## Introduction

With only couple weeks before the end of spring break, I am starting this project to refresh myself with some of the compsci algorithms I had come across during class throughout my freshman year. With this motive at hand, I will try attempt to make a recap on what a binary search algorithm is.

## Concept

Simply said, a binary search algorithm will filter out half of a series of numbers in search of a "target" number. A series will have a total of three markers (start, middle, end), and we will compare the "target" number with the middle value until we find the number or the series ends. 

In terms of how the program will work, the value the middle marker is pointing at will be compared with the "target" number. If the middle value is lower, the start marker will move to the value after the middle value. Likewise, if the middle value is higher, the end marker will move to the value before the middle value. Then, a new middle value will be set for the next set of comparison.

## Running
When running the program, you can set the ```searchSeries``` to your liking (as long or as little as you want).
Then, you can re-assign the ```target``` variable and run the program
One you run it, you will either get:

```shell
Element found at index 2
```

or:

```shell
Element not found in series
```