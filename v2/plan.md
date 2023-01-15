# Parser combinators plan

foo = bar to baz + 1 to 5

Use...

- 'lazyContext(parser)'

  - pushes a new 'lazy context' into the 'lazy context stack'
    - any 'lazy' calls add references to themselves to the current lazy context
    - other things might also add themselves to the context (e.g. assignments)
  - get the result of the passed-in parser
  - compute all lazy results

```
program = oneOrMore(any(assignments(), statement()))

assignemnts = lazyContext(oneOrMore(assignemnt()))

assignment = triple(addAssignment(words()), string('='), lazy(upToNewline(), expression()))

expression = oneOf(
    term()
    triple(term(), mulOp(), term()),
    triple(term(), addOp(), term()),
)

term = oneOf(
    bracketed(expression),
    assignment()
    number(),
    tryInterpret(...)
)
```
