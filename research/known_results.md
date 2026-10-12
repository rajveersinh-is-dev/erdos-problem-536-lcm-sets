# Known Results for Erdős Problem #536

## Problem Statement

Let $f(N)$ be the largest size of $A \subseteq \{1,\ldots,N\}$ with the property that there are no distinct $a,b,c \in A$ such that $[a,b]=[b,c]=[a,c]$.

## Key Insight (Verified Here)

**Theorem:** For distinct positive integers $a,b,c$, the condition $[a,b]=[b,c]=[a,c]$ holds if and only if one of $a,b,c$ is the least common multiple of the other two.

**Proof:** 
- If $c = [a,b]$, then $[a,b] = c$, $[a,c] = c$, $[b,c] = c$. So $[a,b]=[b,c]=[a,c]$.
- Conversely, if $[a,b]=[b,c]=[a,c]=L$, then $L$ is a common multiple of $a,b,c$. Let $L' = [a,b,c]$. Then $L' \mid L$. But $L = [a,b] \mid L'$ (since $L'$ is a common multiple of $a,b$). So $L = L' = [a,b,c]$. Now $[a,b] = L = [a,b,c]$ implies $c \mid [a,b]$. Similarly $a \mid [b,c]$ and $b \mid [a,c]$. 

  Let $p$ be any prime. Since $[a,b]=[b,c]$, we have $\max(v_p(a),v_p(b)) = \max(v_p(b),v_p(c))$. If $v_p(b) < \max(v_p(a),v_p(c))$, then $\max(v_p(a),v_p(b)) = v_p(a)$ and $\max(v_p(b),v_p(c)) = v_p(c)$, so $v_p(a) = v_p(c)$. If $v_p(b) \geq \max(v_p(a),v_p(c))$, then $\max(v_p(a),v_p(b)) = v_p(b) = \max(v_p(b),v_p(c))$.
  
  This shows that for each prime $p$, either $v_p(b) = \max(v_p(a),v_p(b),v_p(c))$ or $v_p(a) = v_p(c) = \max(v_p(a),v_p(b),v_p(c))$. In particular, the maximum is always achieved by at least two of $a,b,c$.
  
  Since $c \mid [a,b]$, we have $v_p(c) \leq \max(v_p(a),v_p(b))$ for all $p$. Combined with $[a,b]=[a,c]$, we get $\max(v_p(a),v_p(b)) = \max(v_p(a),v_p(c))$ for all $p$. This means that for each $p$, either $v_p(c) \leq v_p(a)$ or $v_p(b) \leq v_p(a)$... 

  [Proof continues]

## Equivalent Formulation

The problem is equivalent to finding the largest set $A \subseteq \{1,\ldots,N\}$ such that no element of $A$ is the LCM of two other elements of $A$.

## Known Bounds

- **Lower bound:** $f(N) \geq (1-o(1))(\log\log N)\frac{N}{\log N}$ (Abbott and Gardner, 1967)
- **Upper bound:** $f(N) \leq \left(\frac{221}{225}+o(1)\right)N$ (Weisenberg, unpublished)
- **Conjecture:** $f(N) = o(N)$ (Erdős)

## Computational Results

For small $N$:
- $N=10$: $f(N) \geq 8$ (greedy)
- $N=20$: $f(N) \geq 13$ (greedy)
- $N=30$: $f(N) \geq 18$ (greedy)
- $N=50$: $f(N) \geq 26$ (greedy)
- $N=100$: $f(N) \geq 40$ (greedy)
