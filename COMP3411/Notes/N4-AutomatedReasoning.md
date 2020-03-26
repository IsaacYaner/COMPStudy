# Automated Reasoning

+ Proof systems
  + Soundness, completeness, decidability
+ Resolution and Refutation
+ Horn caluses and SLD resolutaion
+ Prolog
+ Tableau method

## Mechanising Proof

+ **Proof**
  + A set of premises **S** in a sequence of lines, any line is
    +  An axiom or premise from S
    +  A fromula deduced using rule of inference.
    +  Last line is P
+ Symbol: |-, P follows from S, S proves P

## Soundness and COmpleteness

+ **Sound**: This proof system preserves truth
  + if S is all true, P is true
  + IF S|-P, S|=P
  + Start from true, conclusion with true
+ **Complete**: all consequences is capable to be proved.
  + S|=P, S|-P
+ **Decidable** if there is a mechanical procedure which when asked whether S|-P, can always answer correctly

## Resolution

+ Proof system based on refutation
+ Better for computer implementation than axioms and rules
  + can give correct false answers
+ Decidable in propositional Logic
+ Generalises to First-Order Logic
+ All formulae in clausal form

### Normal Forms

+ **literal**: propositional variable
+ **clause**: disjunction of literals
+ Conjunctive Normal From: Conjunction of clauses or just one clause
+ Disjunctive Normal Form: Disjunction of conjuections or just one conjunction
+ Every formula can be converted to CNF and DNF

### Clausal From

+ A set converted from CNF
+ Convert each conjunction to a comma
+ A set of V

### Resolution Rule of Inference

$A_n V B$ then $!B V C_n$
Get $A_n V C_n$

#### Key Idea

+ If B is True, !B is false then C is True
+ vice versa
+ Hence AVC is always true
+ This rule is **sound**
  + Starting with true, conclude with true.

### Applying resolution

+ Convert knowledge base into clausal form
+ Repeatedly apply resolution rule
+ P follows from KB iff each clause in the CNF of P can be derived using resolution

### Refutation systems

+ To show P follows from S
  + Start with S and !P in clausal form
  + Derive a contradiction using resolution
+ **Contradiction**: empty clause
  + Unsatisfiable

#### Applying

+ Negate query to be proven
+ Convert KB and negated query into CNF
+ Apply resolution
+ If empty, query is true

#### Soundness and Completeness

+ **Sound**: preserves truth
+ **Complete**: Capable of proving all consequences
+ **Decidable**: There is an algorithm can always answer

### Heuristics

+ Can disregard certain types of clauses
  + Pure clauses: contain L where !L can't be found elsewhere
  + Tautologies: clause containing both L and !L
  + Subsumed: another clause is a subset of the literals
+ Ordering strategirs
  + Resolve unit clauses first
  + Start with query clauses
  + Aim to shorten clauses

### Horn Clauses

+ Definite Clause: has exactly one positive literal
+ Negative Clause: No positive literal
+ Horn Clause: At most one positive literal

### SLD Resolution

+ Selected literals Linear form Definite clauses resolution
+ For a definite KB and negative clause query Q:
  + KB V Q|-□
  + iff
  + KB V Q|-SLD□

## Prolog

+ Prolog is based on resolution refutation relying on the programmer to exploit search control rules

## Tableau Method

+ Alph Rule
  + A N B
  + ------
  + A  B
+ Beta Rule
  + A V B
  + ------
  + A | B
+ ??? Dont understand!

## Question

+ Relationship btw |- and |=?
+ Watch lecture for Tableau!!
+ What is cannot express ontology???
  + AfPak ontology??
