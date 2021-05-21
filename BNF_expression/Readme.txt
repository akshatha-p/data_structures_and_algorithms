Given BNF 
<expression>  ::=  <factor>  * <expression>   |   <factor>  /  <expression>   |   <factor>
<factor>  :==  <term> + <factor>  |  <term> - <factor>  |  <term>
<term>  ::=  {  <expression>  }  |  <literal>
<literal>  ::=  0|1|2|3|4|5|6|7|8|9

Scanning a numeric expression to build an expression tree using recursive descent. Evaluating the expression represented by the tree to output the resulting integer value.

Input : 
- Numeric expression adhering to the above BNF

Output: 
- Result of the expression 
- Tree representation of the expression

Sample 
Input1: 4+{8/2}-1
Output1: 7.0

Input2: {{5+3}*{6-2}}
Output2: 32



 