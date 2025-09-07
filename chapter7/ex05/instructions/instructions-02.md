Does this function work as expected? Do you see any hidden costs to running it?

<details>
  <summary>Answer</summary>
  
*Before each recursive call, the function creates a slice of its nonempty list argument.  The hidden cost is that each slice produces a copy of the list, less its first item.  This process requires time and memory.*

</details>
