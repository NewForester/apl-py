# apl-py

An APL interpreter implemented in Python

<!--
Copyright 2017 NewForester

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-->

---

This repository contains a pet project.
It is the journey, not the destination, that provides motivation.
Progress is expected to be very slow.

---

The destination is an APL interpreter implemented in Python.
It is unlikely ever to be complete and very likely will be abandoned.
A command line calculator will be sufficient with other parts of the interpreter as necessary (such as workspace load and save).

Some test framework will be necessary but it is likely to be little more than comparison of the console log output against reference files.

---

The journey is part of an exploration of Functional Programming.
The implementation will look to use the functional programming features of Python.

This is not about reinventing or reimplementing the wheel.
The Python libraries will be used where possible.

---

The spark for this task is a conversation I had with a stranger in 2016.

I said I preferred Object Oriented programming.
This assertion had always been understood as a preference over what had gone before Object Oriented programming
but in 2016 mainstream web development discovered Functional Programming and so did those whose knowledge comes from reading rather than practice.

So the stranger asked if my preference was over Functional Programming.
No, I replied, I have no experience of Functional Programming unless you count APL.

He did.  I said that I had programmed in APL a long time ago.
I think I told him it was 30 years ago but, in truth, it was almost 40.

I said my favourite operations were reduce and scan operators (`/` and `\`).
Except that I could not remember the names and called them reduce and expand.
The stranger, who I don't think knew APL, suggested I meant reduce and map.

Now I was confused.
I have used these in Python and know their equivalents in the STL of C++ 98
so I didn't see these as characteristic of Functional Programming '2016 style' unless everything is now Functional Programming.

Furthermore, I knew that map was nothing like scan or expand or whatever is was called (in the C++ STL it is called partial_sum).

Now we were talking at cross-purposes and I think each sensed that neither of us was really sure of what were talking about.
The conversation ended with each thinking the other a jerk.

As a result of that conversation, I decided I wanted to be able to give, from my own experience, my own answer to the question:

<ul style="list-style-type: none;">
<li><q>How is APL a Functional Programming Language ?</q></li>
</ul>

This meant I would:

  * reacquaint myself with APL and
  * learn the basics of several (other) Functional Programming languages.

Reacquainting myself with APL required more than just doing a tutorial.

This is it.

---

*apl-py* - Copyright 2017 NewForester.
Licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

<!-- EOF -->
