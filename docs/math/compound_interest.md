Interest calculation methods are diverse and can be understood through their mathematical formulations and distinct principles. The underlying concept for all types of interest is the relationship between **principal** (*P*), **interest rate** (*r*), **time** (*t*), and the resulting **future value** (*A*). Each approach has its unique formula, providing varying perspectives on how interest accumulates over time.

---

### Simple Interest

Simple interest is calculated by applying the rate of interest only to the original **principal**. The formula for simple interest is expressed as:

\[
A = P \cdot (1 + r \cdot t),
\]

where **\(P\)** represents the *principal amount*, **\(r\)** is the *annual interest rate* (expressed as a decimal), and **\(t\)** signifies the *time duration in years*. This method assumes that the interest does not compound and remains proportional to both the rate and the time.

For instance, an investment of $1,000 at an annual rate of 5% for three years would yield a **future value** of:

\[
A = 1000 \cdot (1 + 0.05 \cdot 3) = 1150.
\]

---

### Periodic Compounding

Periodic compounding calculates interest by applying it to both the **principal** and any previously earned **interest**, repeated at regular intervals. The **future value** in this method is governed by the formula:

\[
A = P \cdot \left(1 + \frac{r}{n}\right)^{n \cdot t},
\]

where **\(n\)** is the *number of compounding intervals per year*. Different frequencies of compounding, such as *annual* (**\(n = 1\)**), *quarterly* (**\(n = 4\)**), *monthly* (**\(n = 12\)**), or *daily* (**\(n = 365\)**), produce varying results.

For example, an investment of $1,000 at 5% annual interest compounded quarterly for three years results in:

\[
A = 1000 \cdot \left(1 + \frac{0.05}{4}\right)^{4 \cdot 3} \approx 1161.84.
\]

---

### Continuous Compounding

Continuous compounding represents the theoretical scenario where compounding occurs at every instant. The mathematical model relies on **Euler’s number** (*e \approx 2.718*), and the **future value** is expressed as:

\[
A = P \cdot e^{r \cdot t}.
\]

In this method, \(e^{r \cdot t}\) captures the *infinite frequency* of compounding. For an initial **principal** of $1,000 at an annual rate of 5% over three years, the **future value** becomes:

\[
A = 1000 \cdot e^{0.05 \cdot 3} \approx 1161.83.
\]

---

### Effective Annual Rate

The **effective annual rate** (*EAR*) converts periodic compounding into an equivalent single annual rate. The relationship is described by:

\[
EAR = \left(1 + \frac{r}{n}\right)^n - 1.
\]

This formula allows comparison of investments or loans with differing compounding frequencies. For instance, an annual nominal interest rate of 5% compounded monthly would yield an **effective annual rate** of:

\[
EAR = \left(1 + \frac{0.05}{12}\right)^{12} - 1 \approx 0.0512 \text{ or } 5.12\%.
\]

---

### Discounted Present Value

The concept of **discounted present value** is used to determine the *present worth* of a future sum of money. The formula employed is:

\[
PV = \frac{FV}{(1 + r)^t},
\]

where **\(FV\)** is the *future value*, and **\(r\)** represents the *discount rate*. This approach is critical in evaluating investments, as it accounts for the *time value of money*.

---

### Real vs. Nominal Interest Rates

Inflation is incorporated into interest rate calculations by distinguishing between **nominal** and **real rates**. The **real interest rate** is derived through the formula:

\[
r_{\text{real}} = \frac{1 + r_{\text{nominal}}}{1 + i} - 1,
\]

where **\(i\)** denotes the *inflation rate*. This formula adjusts the **nominal rate** (**\(r_{\text{nominal}}\)**) to reflect the actual purchasing power of the returns.

---

These formulations illustrate how **interest** can be conceptualized and calculated under various conditions, ranging from simple linear growth to complex exponential models involving compounding and inflation adjustments. Each approach highlights a specific perspective on **financial growth**, tailored to particular use cases and temporal considerations.
