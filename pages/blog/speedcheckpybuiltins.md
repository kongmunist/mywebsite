title: Speed checking Python built-in functions
date: 2020-05-25
label: log
tags: [speedcheck]
snippet: Calling str, type, etc. is free... right?

I found this cool [blog post](http://blog.kevmod.com/2020/05/python-performance-its-not-just-the-interpreter) that was trying to show Python's slower execution time does not just come from its interpreter, and instead was more interested in the benchmark that they ran converting ints to strings as a toy example.

They mentioned off-hand that built-in function calls in Python must be traced back to the built-in library by the interpreter, which takes a decent amount of time if most of your code just calls built-in functions. Here's the code: 

<img src={{ url_for("static", filename = 'speedcheckpybuiltinscode.png') }} width="400" class="d-block mx-auto"/>

### Results

All we do is move the str() function into a local variable (allowed since Python is a functional language), but we gain 20-30% speed boost in the total execution times. 

<img src={{ url_for("static", filename = 'speedcheckpybuiltinstimings.png') }} width="400" class="d-block mx-auto"/>

Of course, this is a toy example since we're only calling one function, but it might be worthwhile to precompile code like this if you're not uing Pypi or something. 