# Definitions and Basic Properties

## Definitions

Let $A \subseteq \mathbb{Z}^+$ be a set of positive integers.

**Definition 1 (Bad triple):** A triple $(a,b,c)$ of distinct elements of $A$ is *bad* if $[a,b] = [b,c] = [a,c]$.

**Definition 2 (LCM-triple):** A triple $(a,b,c)$ of distinct elements of $A$ is an *LCM-triple* if one element is the LCM of the other two, i.e., $c = [a,b]$ or $a = [b,c]$ or $b = [a,c]$.

**Definition 3 (Valid set):** $A$ is *valid* if it contains no bad triples.

**Definition 4 ($f(N)$):** $f(N) = \max\{|A| : A \subseteq \{1,\ldots,N\}, A \text{ is valid}\}$.

## Theorem 1 (Equivalence)

For distinct positive integers $a,b,c$, the following are equivalent:
1. $(a,b,c)$ is a bad triple
2. $(a,b,c)$ is an LCM-triple

**Proof:** 
- (2) $\Rightarrow$($1)$: If $c = [a,b]$, then $[a,b] = c$, $[a,c] = c$, $[b,c] = c$.
- (1) $\Rightarrow$ (2): See [detailed proof in known_results.md].

## Corollary 1

$A$ is valid if and only if no element of $A$ is the LCM of two other elements of $A$.

## Structural Observations

### Prime Powers

**Proposition 1:** Any set of powers of a single prime is valid.

*Proof:* If $A = \{p^i : i \in I\}$, then for distinct $p^i, p^j, p^k$ with $i < j < k$, we have $[p^i, p^j] = p^j \neq p^k = [p^j, p^k]$. So no LCM-triple exists.

### Antichains

**Proposition 2:** Any antichain in the divisibility order is valid.

*Proof:* If $A$ is an antichain, then no element divides another. If $c = [a,b]$, then $a \mid c$, contradicting the antichain property. So $A$ is valid.

### Characterization of LCM-triples

**Proposition 3:** For distinct $a,b,c$, the following are equivalent:
1. $c = [a,b]$
2. $a \mid c$, $b \mid c$, and for every prime $p$, $v_p(c) = \max(v_p(a), v_p(b))$

*Proof:* Direct from the definition of LCM.
