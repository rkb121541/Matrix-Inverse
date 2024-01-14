# MatrixInverse

Implemented programs to calculate the inverses of 2x2 and 3x3 matrices. The final matrix can be displayed with each entry of the final matrix represented in either decimal or fractional form.

The 2x2 matrix is calculated using the [standard formula for calculating 2x2 matrix inverses](https://www.chilimath.com/lessons/advanced-algebra/inverse-of-a-2x2-matrix/).

<!-- $$ 
\begin{bmatrix} 
    a & b \\ 
    c & d 
    \end{bmatrix} ^{-1} = 
\frac{1}{ad-bc} 
\begin{bmatrix} 
    d & -b \\ 
    -c & a 
    \end{bmatrix}
$$ -->

The 3x3 matrix is calculated using the [Cofactor formula](https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html).

<!-- $$
A^{-1} =
\begin{bmatrix} 
    A_{11} & A_{12} & A_{13} \\ 
    A_{21} & A_{22} & A_{23} \\
    A_{31} & A_{32} & A_{33} \\
    \end{bmatrix} ^{-1} = 
\frac{1}{det(A)} 
\begin{bmatrix} 
    C_{11} & C_{12} & C_{13} \\ 
    C_{21} & C_{22} & C_{23} \\
    C_{31} & C_{32} & C_{33} \\
    \end{bmatrix}
$$ -->

I initially wrote out the formulas that I used to calculate the inverses, but the LaTeX won't render properly on GitHub Markdown files. So, I provided links to them instead.
