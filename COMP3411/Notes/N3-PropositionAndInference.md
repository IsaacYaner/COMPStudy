# Propositions and Inference

+ Knowledge Representation and Logic
+ Logical Arguments
+ Propositional Logic
  + Syntax
  + Semantics
+ Validity, Equivalence, Satisfiability, Entailment
+ Inference by Natural Deduction

## Knowledge bases

+ Set of sentences in a formal language
+ Declarative approach to build an agent
  + What a system what is needed to know,
    + then it can ask itself what is needed to do
  + Answers should follow from the knowledge based

### Knowledge Based Agent

Be able to:

+ **represent** states, actions, etc.
+ **Incorporate** new percepts
+ **Update** internal representations of the world
+ **Deduce** hidden properties of the world
+ **Determine** appropriate actions

### Formal Languages

+ Natural languages exhibit **ambiguity**
+ Makes it difficult to interpret meaning, inference harder to define and comput
+ Symbolic logic syntactically unambiguous

### Syntax vs Semantics

+ Legal sentences
+ Meaning of sentences
  + Refers to sentences's relationship to world or model
  + Semantic properties of 
    + sentences include truth and falsity
    + names and descriptions include referents
  + Meaning is not intrinsic to the sentence
    + Interpretation is required to determine meaning
    + Iterpretations are agreed amongst a linguistic community

### Propositions

+ Entities can be true or false
+ Use ordinanry declarative sentences
+ In propositional Logic, use single letters to represent propositions: **Scheme of abbreviation**
+ ***Reasoning is independent of propositional substructure***

### Logical Arguments

+ Relates a set of premises to a conclusion
+ What does it mean in the slides by the last question??????

### Propositional Logic

+ Use letters to stand for basic propositions, combine using **operators** not, and or, implies, iff
+ **connectives**
  + negation
  + conjunction
  + disjunction
  + implication
  + bi-implication  

#### Omitting brackets

+ Precedence
  + not->and->or->implies->iff
+ Left associative

**tautology**: always true
**Satisfiable**: may be true
**Equivalent**: Same truth table

### Material Implication

+ P->Q equivalent to not PVQ
+ English often use causal connection between antecedent(P) and consequent(Q)

### Logical Equivalences

+ TBC

### Proof of equivalence

### Interpretations and Models

+ Interpretation: assign values
+ Model: Interpretation that satisfies contraints
  + possible world in which some sentences are true
+ We want to know what is true in all models
+ Proposition is statement that is true or false

### Entailment

+ One sentence follows logically from another set of sentences
+ KB|=a
  + KB entails a
  + iff a is true in all models if KB is true
+ Relationship between sentences based on semantics

### Models

+ One row of the truth table
+ M is a model of a if a is true in M
+ M(a) be the set of all models of a
  + KB|=a iff M(KB) belongs to M(a)

### Entailment

+ S entails P if when all formulae in S are True, P is True
  + Semantic definition - concerns truth(not proof)
+ Compute whether S|=P by calculating a truth table for S and P
  + Syntactic notion - concerns computation/proof
+ When S is empty
  + All rows are True

### Natural deduction proofs

## Question

+ When, where did we constructed a World model? How?
  + Check in slides and find out.
