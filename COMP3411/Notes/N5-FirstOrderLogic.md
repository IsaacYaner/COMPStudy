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

+ Eliminate implications and bi-implications
+ Move negations invard(!A -> E!)
+ Eliminate double negations
+ Rename deplicated names
+ Use equivalences to move quantifiers to the left
  + ∀xP(x) ∧∃y Q(y) becomes ∀x∃y(P(x) ∧ Q(y))
+ Skolemise
  + Replace quantified variable by a non quantified new variable
  + ∃x P(x) becomes P(a0)
  + ∀x ∃y P(x, y) becomes P(x, f0(x))
+ Deop all remaining universal quantifiers
+ Use distribution laws to get CNF->clausal form

### Unification

+ **Unifier** of two atomic formulae
  + substitution of terms for variables that makes them identical
  + i.e. change the name of same variables to make two formulae looks identical
+ More general unifier if 
  + $\sigma_2=\sigma_1\sigma_3$
  + aka after one substitution, make another substitution can yield third substitution
  + Then the third one is more general
+ If two atomic formulae are unifiable, they have a ***most general unifier***
+ **MGU**

#### Disagreement set

+ ??

### First-Order Resolution

+ AVB  !B'VC
+   (AVC)mgu(B,B')

### Applying Resolution Refutation

+ Negate query
+ Convert KB and Nquery into CNF
+ Apply resolution until
  + empty clause (contradiction) 
  + no more clauses can be derived 
    + Copy of clause is same clause with different variable names
+ If empty, True
+ Otherwise false
+ Infinite, no answer n

### Soundness and Completeness

+ **Sound**: preservers truth
+ **Complete**: Prove all
+ Not **Decidable**: Can not always answer whether

### Undecidability

+ Can't determine when this problem will rise
+ If KB is unsatisfiable, empty clause somewhere
  + But if no empty clause, may go on forever
+ Even for propositional logic, complexity is $O(2^n)$

### Horn Clauses

+ Idea: use less expressive language
+ Definite Clause
+ Negative Clause
+ Horna Clause

## Questions
