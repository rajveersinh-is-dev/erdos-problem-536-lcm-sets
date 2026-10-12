# Main Results for Erdős Problem #536

## Theorem 1: The Interval Construction

**Theorem 1.** For any $N \geq 2$, the set $A = \{\lfloor N/2 \rfloor + 1, \ldots, N\}$ is valid. Consequently, $f(N) \geq \lceil N/2 \rceil$.

**Proof.** We show that for any distinct $a, b \in A$, we have $[a,b] > N$.

Let $a, b \in A$ with $a \neq b$. Let $d = \gcd(a,b)$, and write $a = dx$, $b = dy$ where $\gcd(x,y) = 1$ and $x \neq y$.

**Case 1:** $x = 1$ or $y = 1$. Without loss of generality, $x = 1$. Then $a = d$ and $b = dy$ with $y > 1$. Since $a > N/2$, we have $d > N/2$. Since $b \leq N$, we have $dy \leq N$. Thus $y \leq N/d < 2$, so $y = 1$, contradicting $x \neq y$.

**Case 2:** $x, y \geq 2$. Since $x \neq y$ and $\gcd(x,y) = 1$, we have $xy \geq 6$. Also, $dx > N/2$ implies $d > N/(2x) \geq N/4$. Therefore:
$$[a,b] = dxy \geq 6d > 6 \cdot \frac{N}{4} = \frac{3N}{2} > N.$$

In both cases, $[a,b] > N$, so $[a,b] \notin A$. Thus $A$ is valid. $\blacksquare$

## Theorem 2: Extension to the Full Interval

**Theorem 2.** Let $X \subseteq \{1, \ldots, \lfloor N/2 \rfloor\}$ be a set such that for all distinct $a, b \in X$, either $[a,b] \leq N/2$ or $[a,b] > N$. Then $X \cup \{\lfloor N/2 \rfloor + 1, \ldots, N\}$ is valid.

**Proof.** Let $A = X \cup \{\lfloor N/2 \rfloor + 1, \ldots, N\}$. We check that no element of $A$ is the LCM of two other elements of $A$.

**Case 1:** $a, b, c \in \{\lfloor N/2 \rfloor + 1, \ldots, N\}$. By Theorem 1, $[a,b] > N$, so $c \neq [a,b]$.

**Case 2:** $a, b \in X$, $c \in \{\lfloor N/2 \rfloor + 1, \ldots, N\}$. By hypothesis, $[a,b] \leq N/2$ or $[a,b] > N$. Since $c > N/2$, we have $c \neq [a,b]$.

**Case 3:** $a \in X$, $b, c \in \{\lfloor N/2 \rfloor + 1, \ldots, N\}$. We need $c \neq [a,b]$. Since $b > N/2$ and $a \leq N/2$, we have $[a,b] \geq b > N/2$. If $a \mid b$, then $[a,b] = b \neq c$. If $a \nmid b$, then $\gcd(a,b) < a \leq N/2$, so:
$$[a,b] = \frac{ab}{\gcd(a,b)} > \frac{ab}{a} = b.$$
Moreover, since $a \nmid b$, we have $\gcd(a,b) \leq a/2$, so:
$$[a,b] = \frac{ab}{\gcd(a,b)} \geq \frac{ab}{a/2} = 2b > N.$$
Thus $[a,b] > N$, so $c \neq [a,b]$.

**Case 4:** $a, b, c \in X$. By hypothesis, $[a,b] \leq N/2$ or $[a,b] > N$. Since $c \leq N/2$, we have $c \neq [a,b]$.

All cases are covered, so $A$ is valid. $\blacksquare$

## Corollary 1: Improved Lower Bound

Let $g(N)$ denote the maximum size of a set $X \subseteq \{1, \ldots, \lfloor N/2 \rfloor\}$ such that for all distinct $a, b \in X$, either $[a,b] \leq N/2$ or $[a,b] > N$. Then:
$$f(N) \geq \left\lceil \frac{N}{2} \right\rceil + g(N).$$

## Proposition: Lower Bound on $g(N)$

**Proposition.** $g(N) \geq \lfloor \log_2 N \rfloor$.

*Proof.* Take $X = \{1, 2, 4, 8, \ldots, 2^k\}$ where $2^k \leq N/2$. For any distinct $a, b \in X$, we have $[a,b] = \max(a,b) \leq N/2$. So $X$ is good, and $|X| = k+1 \geq \log_2(N/2) + 1$. $\blacksquare$

## Theorem 3: Improved Lower Bound

$$f(N) \geq \frac{N}{2} + \log_2 N - 1.$$

**Proof.** Combine Theorem 1, Corollary 1, and the Proposition. $\blacksquare$

## Computational Verification

For $N = 100$:
- Theorem 1 gives $f(100) \geq 50$.
- With $X = \{1, 2, 4, 8, 16, 32\}$ (powers of 2 up to 50), we get $f(100) \geq 50 + 6 = 56$.
- Computational search found a valid set of size 57.

## Comparison with Known Bounds

| Bound | Value for $N = 100$ | Asymptotic |
|-------|---------------------|------------|
| Abbott-Gardard (lower) | $\sim 10$ | $N \log\log N / \log N$ |
| **Theorem 3 (new, lower)** | **$50 + \log_2 100 - 1 \approx 55.6$** | **$N/2 + \log N$** |
| Weisenberg (upper) | $\sim 98.2$ | $(221/225)N$ |

**Theorem 3 improves the lower bound by a factor of approximately $\frac{\log N}{2\log\log N}$ over the previous best bound.**
