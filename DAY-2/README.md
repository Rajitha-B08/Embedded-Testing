# Day 2 – Selenium Locators, Stacks & Queues (Java)

## 1. Topics Learned – Selenium WebDriver (Python)

### Introduction to Locators

Locators are used in Selenium to identify and locate web elements on a webpage. They help us interact with elements such as buttons, text fields, links, checkboxes, and dropdowns.

### Types of Selenium Locators

 ID                 Locates an element using its ID               `By.ID`                
 Name               Locates an element using its name attribute   `By.NAME`              
 Class Name         Locates an element using its class attribute  `By.CLASS_NAME`        
 Tag Name           Locates an element using its HTML tag         `By.TAG_NAME`          
 Link Text          Locates a link using its complete text        `By.LINK_TEXT`         
 Partial Link Text  Locates a link using a part of its text       `By.PARTIAL_LINK_TEXT` 
 CSS Selector       Locates elements using CSS selector syntax    `By.CSS_SELECTOR`      
 XPath              Locates elements using XML path expressions   `By.XPATH`             

### Syntax – Using Locators in Python

```
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")

# Locating elements
driver.find_element(By.ID, "username")
driver.find_element(By.NAME, "password")
driver.find_element(By.CLASS_NAME, "login")
driver.find_element(By.TAG_NAME, "input")
driver.find_element(By.LINK_TEXT, "Home")
driver.find_element(By.PARTIAL_LINK_TEXT, "Hom")
driver.find_element(By.CSS_SELECTOR, "#username")
driver.find_element(By.XPATH, "//input[@id='username']")

driver.quit()
```

### Important Points

- `find_element()` returns the first matching element.
- `find_elements()` returns a list of all matching elements.
- `By` is imported from `selenium.webdriver.common.by`.
- XPath and CSS Selectors are useful when elements do not have unique IDs or names.
- Locators are essential for interacting with web elements during automation testing.

## 2. Coding Practice – Stacks & Queues (Java)

### Question 1: Balanced Brackets Using Stack

**Problem Statement:**

Given a string containing brackets like `({[]})`, use a stack to determine whether the brackets are balanced.

#### Approach 1: Using ArrayList

**Logic:**

1. Create an ArrayList to use as a stack.
2. Traverse the string character by character.
3. If an opening bracket is found, push it using `add()`.
4. If a closing bracket is found, check the top element.
5. If the brackets match, remove the top element using `remove()`.
6. If the stack is empty after traversal, the brackets are balanced.

**Java Code:**

```
import java.util.ArrayList;

public class Main {

    static boolean isBalanced(String str) {

        ArrayList<Character> stack = new ArrayList<>();

        for (int i = 0; i < str.length(); i++) {

            char ch = str.charAt(i);

            if (ch == '(' || ch == '{' || ch == '[') {
                stack.add(ch);
            }

            else {
                if (stack.isEmpty())
                    return false;

                char top = stack.get(stack.size() - 1);

                if ((ch == ')' && top == '(') ||
                    (ch == '}' && top == '{') ||
                    (ch == ']' && top == '[')) {

                    stack.remove(stack.size() - 1);
                }
                else {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {

        String str = "({[]})";

        if (isBalanced(str))
            System.out.println("Balanced");
        else
            System.out.println("Not Balanced");
    }
}
```

**Example Output:**

```
Balanced
```

**Complexity:**

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

#### Approach 2: Using Java Stack Class

**Logic:**

1. Create a Stack to store opening brackets.
2. Push opening brackets using `push()`.
3. When a closing bracket appears, check the top element using `peek()`.
4. If it matches, remove it using `pop()`.
5. If the stack is empty after traversal, the brackets are balanced.

**Java Code:**

```
import java.util.Stack;

public class Main {

    static boolean isBalanced(String str) {

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < str.length(); i++) {

            char ch = str.charAt(i);

            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }

            else {
                if (stack.empty())
                    return false;

                char top = stack.peek();

                if ((ch == ')' && top == '(') ||
                    (ch == '}' && top == '{') ||
                    (ch == ']' && top == '[')) {

                    stack.pop();
                }
                else {
                    return false;
                }
            }
        }

        return stack.empty();
    }

    public static void main(String[] args) {

        String str = "({[]})";

        if (isBalanced(str))
            System.out.println("Balanced");
        else
            System.out.println("Not Balanced");
    }
}
```

**Example Output:**

```
Balanced
```

**Complexity:**

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

### Question 2: Evaluate an RPN Expression Using Stack

**Problem Statement:**

Given tokens of an RPN (Reverse Polish Notation) expression, use a list as a stack to compute the result.

#### Approach: Using ArrayList 

**Logic:**

1. Create an ArrayList to use as a stack.
2. Traverse the tokens from left to right.
3. If the token is a number, convert it into an integer and push it into the stack.
4. If the token is an operator:
   - Remove the top two elements from the stack.
   - Perform the corresponding arithmetic operation.
   - Push the result back into the stack.
5. After processing all tokens, the remaining element in the stack is the final result.

Example:

```
Stack: [10, 2]

First pop  = 2
Second pop = 10

10 - 2 = 8
```

**Java Code:**

```
import java.util.ArrayList;

public class Main {

    static int evaluate(String[] tokens) {

        ArrayList<Integer> stack = new ArrayList<>();

        for (String token : tokens) {

            if (token.equals("+") ||
                token.equals("-") ||
                token.equals("*") ||
                token.equals("/")) {

                int b = stack.remove(stack.size() - 1);
                int a = stack.remove(stack.size() - 1);

                int result = 0;

                switch (token) {
                    case "+":
                        result = a + b;
                        break;

                    case "-":
                        result = a - b;
                        break;

                    case "*":
                        result = a * b;
                        break;

                    case "/":
                        result = a / b;
                        break;
                }

                stack.add(result);
            }

            else {
                stack.add(Integer.parseInt(token));
            }
        }

        return stack.get(stack.size() - 1);
    }

    public static void main(String[] args) {

        String[] tokens = {"2", "1", "+", "3", "*"};

        int result = evaluate(tokens);

        System.out.println("Result: " + result);
    }
}
```

**Example Output:**

```
Result: 9
```

**Complexity:**

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

## Day 2 – Learning Summary

**Selenium:**

- Learned the concept of Selenium locators.
- Practiced locating web elements using Python.

**Data Structures:**

- Understood the LIFO (Last In, First Out) principle.
- Practiced stack implementation using ArrayList and Java Stack Class.



**One small correction to keep in mind:** Your RPN implementation uses Java integer division, which truncates towards zero. This is appropriate for the usual RPN coding problem constraints.

Also, since your training covers both Selenium and Java coding, keeping these as separate sections in the same daily README will make your learning progress easier to track.
