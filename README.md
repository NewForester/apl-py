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

This repository contains a pet project of mine.
In some respects, it is the journey, not the destination, that provides motivation.
Progress may be slow given that this is a solo project.

---

The destination is an APL interpreter implemented in Python 3.
A command line calculator will be sufficient with other parts of the interpreter as necessary (such as workspace load and save).

A test framework will be necessary but it will be simple.
It may never be more than comparison of the console log output against reference files wrapped up in simple bash scripts.

---

The journey is part of an exploration of Functional Programming.
The implementation will look to use the functional programming features of Python.

This is not about reinventing or reimplementing the wheel.
The Python libraries will be used where possible.

For the vector calculator, it was decided to exploit the lazy evaluation of Python iterables.
See below.

---

This release (0.17.09) represents 6 months development starting from scratch.
What is and what is not implemented:

  - real numbers but not complex numbers;
  - Unicode characters/strings;
  - scalars and vectors but not arrays;
  - mixed and nested vectors;
  - all monadic and dyadic mathematical functions save ⌹;
  - all monadic and dyadic non-mathematical functions save ⍎, ⍕ and ⍺;
  - no operators are implemented;
  - system variables: ⎕IO, ⎕CT and ⎕EE (see eager/lazy evaluation below);
  - system commands: only )OFF;
  - workspace variables but not workspace functions
  - scripting and logging

---

## Eager/Lazy Evaluation

In Python 3, lazy evaluation is explicit in generators and implicit in iterables.
APL is not a language that uses 'lazy evaluation' (as far as I can tell).

That some of Python 3 is implicitly lazy is potentially a problem.
When APL expression evaluation fails, a ^ or two are used to indicate where.
If the interpreter turns an APL expression into a sequence of Python iterables
that are evaluated only after parsing the entire expression
then, should their evaluation fail, working out where to place the ^ is non-trivial.

The approach adopted here may be termed 'lazy design':
implement an interpreter that embraces lazy evaluation and provide the means to disable it.
To disable lazy evaluation, set the system variable ⎕EE (for eager evaluation) to 1.
This may also be done on invocation from the command line using -ee=1 as a flag.

Enabling eager evaluation means that the result of every APL operation is converted to a Python _tuple_,
which forces the immediate evaluation of any Python iterable produced by the operation.

Embracing lazy evaluation involved the (re) implementation of vector operations to return iterables.
The iterables themselves are the most 'imperative' Python I have ever written.
The alternative would have been to use generators.
I suspect generator implementations would look a lot more like mainstream Python.

The current implementation does a very reasonable job of placing ^ to indicate where in an APL expression an error occurred.
If in doubt, switch to eager evaluation and try again.

Embracing lazy evaluation also means printing the result of an expression one element at a time.
When an error occurs, the current implementation backtracks to erase the good results printed so far in an effort to emulate
the output that would have occurred under eager evaluation.

Expect this to change:  not erasing the good results so far is potentially a very useful debugging aid.

---

## The Original Spark

The spark for this project is a conversation I had with a stranger in 2016.

I said I preferred Object Oriented programming.
This assertion had always been understood as a preference over what had gone before Object Oriented programming
but in 2016 mainstream web development discovered Functional Programming and so did those whose knowledge comes from reading rather than practice.

So the stranger asked if my preference was over Functional Programming.
No, I replied, I have no experience of Functional Programming unless you count APL.

He did.  I said that I had programmed in APL a long time ago.
I think I told him it was 30 years ago but, in truth, it was almost 40.

I said my favourite operators were _reduce_ and _scan_ (`/` and `\`).
Except I could not remember the names and called them _reduce_ and _expand_.
The stranger, who I don't think knew APL, suggested I meant _reduce_ and _map_.

Now I was confused.
I have used these in Python and know their equivalents in the STL of C++ 98
so I didn't see these as characteristic of Functional Programming '2016 style' unless everything was now Functional Programming.

Furthermore, I knew that _map_ was nothing like the _scan_ of APL (which is named _partial_sum_ in the C++ STL).

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
