## Instructions

Conversations often shift focus to earlier topics. Modify the therapist program in the file **doctor.py** to support this capability. Add each patient input to a history list. Then occasionally choose an element at random from this list, change persons, and prepend (add at the beginning) the qualifier “Earlier you said that” to this reply. Make sure that this option is triggered only after several exchanges have occurred. (LO: 5.1, 5.2)

An example of the program is shown below:

```
Good morning, I hope you are well today.
What can I do for you?

>> I wanted to talk about my day
You seem to think that you wanted to talk about your day

>> I do want to talk about my day
Why do you say that you do want to talk about your day

>> because that is what I want to talk about
You seem to think that because that is what you want to talk about

>> it is what I want to talk about
Why do you say that it is what you want to talk about

>> because I want to talk about it
Earlier you said that you do want to talk about your day

>> yes, I do
Why do you say that yes, you do

>> you are not a very good therapist
Please continue.

...
```

<!--
{
    "CopyExercise": {
        "name": "doctor.py",
        "copyTarget": "/chapter5/ex09/student/doctor.py",
        "pasteTarget": "/doctor.py"
    }
}
-->

## Your Tasks
