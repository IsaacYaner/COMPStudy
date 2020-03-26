# First Order Logic

+ FOL
  + Syntax
  + Semantics
+ Automated Reasoning
  + CNF
  + FO resolution and unification
  + Soundness, completeness, decidability
+ Applications
  + Ontologies
  + Reasoning About Action

## Syntax

+ Constant symbols
+ Variables
+ Function symbols
+ Predicate symbols
+ Quantifiers
  + A and E

## Language

+ Terms
  + Constants, variables, functions
+ Atomic formulae
  + Predicates applied to tuples of terms
+ Quantified formulae
  + for all sth, formulae

### Universal Quantifiers

+ All
+ Ax P
+ Conjunction of instantiations of P

### Existential Quantifiers

+ Some
+ Ex P
+ Disjunction

### Nested Quantifiers

+ Order is important

### Scope Ambiguity

+ A match with ->
+ E match with N

### Scope of Quantifiers

+ **Scope** of **quantifier** in a formula A is that **subformula** B of A.
  + Main logical operator is quantifier
+ Variables belongs to the innermost quantifier that mention them
  + ∀zP(z) → ¬Q(z) — scope of ∀z is ∀zP(z) but not Q(z)

### Semantics of First-Order Logic

+ Interpretation is required to give semantics
  + non-empty **domain of discourse**(set of objects).
  + Truth of any formula depends on the interpretation
+ It defines
  + Constant symbol
  + function symbol
  + predicate symbol
+ Then
  + universal quantifier
  + existential quantifier

### Resolution for First-Order Logic

+ Based on resolutiohn for Propositional Logic
+ Extended syntax
  + Variables and quantifiers
+ Define clausal form for FOL formulae
+ Eliminate quantifiers from clausal forms
+ Adapt procedure to cpoe with variables (unification)

### Conversion to Conjunctive Normal Form



## Questions
