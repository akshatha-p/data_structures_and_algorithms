




"""
<expression>  ::=  <factor>  * <expression>   |   <factor>  /  <expression>   |   <factor>
<factor>  :==  <term> + <factor>  |  <term> - <factor>  |  <term>
<term>  ::=  {  <expression>  }  |  <literal>
<literal>  ::=  0|1|2|3|4|5|6|7|8|9
"""

#class tree used to create a binary tree   
class Tree:
    def __init__(self):
        self.left  = None
        self.data  = None
        self.right = None
#class for creating an expression tree        
class ExpressionTree(Tree):
    def __init__(self):
        self.left  = None
        self.data  = None
        self.right = None
#class for creating a Factor tree
class FactorTree(Tree):
    def __init__(self):
        self.left  = None
        self.data  = None
        self.right = None
#class for creating a Term tree
class TermTree(Tree):
    def __init__(self):
        self.left  = None
        self.data  = None
        self.right = None

# class to handle tokens
class Token():
    def __init__(self):
        self.token = None #holds the value of the token
        self.next = 0 # object to hold index of the next token
        self.input_exp = None #expression obtained from the userf
        
        #gives the current token        
    def TokenValue(self):
        return self.token

    #returns the next token 
    def NextToken(self):
        #checking if the index of expression > length of given input expression
        if self.next + 1 >= self.input_exp.__len__():
            self.token = None
            
    #getting the next token from the input expression        
        else:      
            self.next = self.next + 1
            self.token = self.input_exp[self.next]

    #setting the input expression and token value    
    def setToken(self, expression):
        self.input_exp = expression
        self.token = self.input_exp[self.next]
    
    ## Standard python class functions
    # method to set current token is a string
    def __repr__(self):
        return self.token
    # python's builtin function to comare two values that are of the same type
    def __eq__(self, some_token):
        return self.token == some_token


############################################################################
############################################################################
############################################################################
########################## expression #######################################

#<expression>  ::=  <factor>*<expression> | <factor>/<expression> | <factor> 
#defining an expression as per the given bnf        


def expression(): 
    #creating an expression result tree and a factor tree   
    EresultTree = ExpressionTree()
    EfactorTree = factor()

    #checking if token value is *, / or none of these

    #<expression>  ::=  <factor>*<expression> 
    #result expression tree  root--> *, leftchild --> factortree, rightchild -->expression tree
    if Etoken == '*' : 
        EresultTree.data  = Etoken.TokenValue()
        Etoken.NextToken()
        EresultTree.left  = EfactorTree 
        EresultTree.right = expression()  

    #<expression>  ::=  <factor>/<expression> 
    #result expression tree  root--> /, leftchild --> factortree, rightchild -->expression tree
    elif Etoken == '/' :
        EresultTree.data  = Etoken.TokenValue()
        Etoken.NextToken()
        EresultTree.left  = EfactorTree 
        EresultTree.right = expression()

    #<expression>  ::=  <factor> 
    #result expression tree --> factor tree
    else:
        EresultTree = EfactorTree
    
    return EresultTree



############################################################################
############################################################################
############################################################################
######################## factor #############################################
#<factor>  :==  <term> + <factor>  |  <term> - <factor>  |  <term>
#defining a factor as per the given bnf 
          

def factor():
    #creating factor result tree and a term tree
    FresultTree = FactorTree()
    FtermTree = term()
    

    #checking if token value is +, - or none of these - 3 cases

    #<factor>  :==  <term> + <factor> 
    #result factor tree  root--> +, leftchild --> termtree, rightchild -->factor tree
    if Etoken.token == '+':
        FresultTree.data  = Etoken.TokenValue()
        Etoken.NextToken()
        FresultTree.left  = FtermTree
        FresultTree.right = factor()
        
    #<factor>  :==  <term> - <factor> 
    #result factor tree  root--> -, leftchild --> termtree, rightchild -->factor tree
    elif Etoken.token == '-':
        FresultTree.data  = Etoken.TokenValue()
        Etoken.NextToken()
        FresultTree.left  = FtermTree
        FresultTree.right = factor()    

    #<factor>  :==  <term>  
    #result factor tree  root--> Term tree
    else:
        FresultTree = FtermTree

    return FresultTree


############################################################################
############################################################################
############################################################################
######################## term ##############################################
#<term>  ::=  {  <expression>  }  |  <literal>
#defining a term as per the given bnf  

      
def term():
    #creating a term result tree    
    TresultTree = TermTree()
    
    #<term>  ::=  {  <expression>  } 
    if Etoken.token == '{':
        Etoken.NextToken()
        TresultTree = expression()
        if Etoken.token != '}':
            print("paranthesis missing")   
        Etoken.NextToken() 
        #<term>  ::= <literal>          
    elif Etoken.TokenValue() in Literal_list:
        TresultTree.data = Etoken.TokenValue()
        Etoken.NextToken()
    return TresultTree

#evaluating the expression tree created for the given input expression
#returns the value of the given expression

def evaluate_tree(Finaltree): 
    result = 0
    #base case
    if Finaltree.left is None or Finaltree.right is None:
        return int(Finaltree.data)
    #calling the function recursively 
    else : 
        if Finaltree.data == "+":
            result = evaluate_tree(Finaltree.left) + evaluate_tree(Finaltree.right)
        if Finaltree.data == "-":
            result = evaluate_tree(Finaltree.left) - evaluate_tree(Finaltree.right)
        if Finaltree.data == "*":
            result = evaluate_tree(Finaltree.left) * evaluate_tree(Finaltree.right)
        if Finaltree.data == "/":
            result = evaluate_tree(Finaltree.left) / evaluate_tree(Finaltree.right)
    return result

#displaying the expression tree created 

def display_tree(tree, level = 0): 
    ## Recursive function to print the final tree
    if tree.data is None:
        return None
    if tree.left is None and tree.right is None:
        print('    ' * (level - 1) + '####  ' * (level > 0) + tree.data)
    else:
        print('    ' * (level - 1) + '####  ' * (level > 0) + tree.data)
        display_tree(tree.left, level+1)
        display_tree(tree.right, level+1)

      
############################################################################
############################################################################
############################################################################


if __name__ == "__main__":
 
    #creating a global variable Etoken used for being able to use in other functions 
    global Etoken
    #creating the Token 
    Etoken = Token()
    
    
    #list of literal values given in the bnf
    Literal_list = ['0','1','2','3','4','5','6','7','8','9']
    #taking input expression from the user
    expr = input("Input an expression: ")
    expr_len = len(expr)
    #removing the extra white spaces if any from the input expression
    expr = expr.replace(' ', '')


    #setting the token value and expression with the given input expression
    Etoken.setToken(expr)

    #creating the expression tree 
    tree = expression()
    
    print('\n\nEvaluating BNF Expression.....')
    final_value = evaluate_tree(tree)
    
    print(f'Expression value = {final_value}')
    print('\n\n\n Tree Structure----')
    display_tree(tree)


    
    
    
    
    
