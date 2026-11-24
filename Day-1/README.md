# Day 1 – Software Testing Fundamentals & Array Problems (Java)

## 1. Topics Learned – Software Testing Basics / Fundamentals

- Introduction to Software Testing
- Why Software Testing is important
- Objectives of Software Testing
- Difference between Verification and Validation
- Difference between Quality Assurance (QA) and Quality Control (QC)
- Software Testing Life Cycle (STLC)
- Software Development Life Cycle (SDLC)
- Basics of Manual Testing
- Introduction to Test Cases and Test Scenarios
- Principles of Software Testing

## 2. Coding Practice – Arrays (Java)

### Question 1: Sort an Array Containing 0s, 1s and 2s

**Problem Statement:**

Given an array containing only `0`, `1`, and `2`, sort the array in ascending order without using any built-in sorting function.

**Example:**

**Input:**
```text
[2, 0, 1, 2, 1, 0]
```

**Output:**
```text
[0, 0, 1, 1, 2, 2]
```

#### Approach 1: Brute Force – Bubble Sort

**Logic:**

1. Compare two adjacent elements in the array.
2. If the left element is greater than the right element, swap them.
3. Continue comparing and swapping elements in each pass.
4. Repeat until the array is sorted.

**Java Code:**

```java
public class Main {

    static void bubbleSort(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {

                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {2, 0, 1, 2, 1, 0};

        bubbleSort(arr);

        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
```

**Example Output:**

```text
0 0 1 1 2 2
```

**Complexity:**

- Time Complexity: `O(n²)`
- Space Complexity: `O(1)`

#### Approach 2: Optimal – Counting Sort

**Logic:**

1. Initialize three counters to count the occurrences of `0`, `1`, and `2`.
2. Traverse the array and increment the respective counter for each element.
3. Traverse the array again and fill it with zeros, followed by ones and twos according to their counts.
4. The array is now sorted in ascending order.

**Java Code:**

```java
public class Main {

    static void countingSort(int[] arr) {
        int count0 = 0, count1 = 0, count2 = 0;

        for (int num : arr) {
            if (num == 0)
                count0++;
            else if (num == 1)
                count1++;
            else
                count2++;
        }

        int index = 0;

        while (count0-- > 0)
            arr[index++] = 0;

        while (count1-- > 0)
            arr[index++] = 1;

        while (count2-- > 0)
            arr[index++] = 2;
    }

    public static void main(String[] args) {
        int[] arr = {2, 0, 1, 2, 1, 0};

        countingSort(arr);

        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
```

**Example Output:**

```text
0 0 1 1 2 2
```

**Complexity:**

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

---

### Question 2: Rotate an Array to the Right by K Steps

**Problem Statement:**

Given an integer array and an integer `k`, rotate the array to the right by `k` steps efficiently.

**Example:**

**Input:**
```text
Array = [1, 2, 3, 4, 5, 6, 7]
K = 3
```

**Output:**
```text
[5, 6, 7, 1, 2, 3, 4]
```

#### Approach 1: Brute Force 

**Logic:**

1. Store the last element of the array in a temporary variable.
2. Shift all the remaining elements one position to the right.
3. Place the stored element at the first position.
4. Repeat the process `k` times.
5. Use `k % n` to avoid unnecessary rotations.

**Java Code:**

```java
public class Main {

    static void rotate(int[] arr, int k) {
        int n = arr.length;

        if (n == 0)
            return;

        k = k % n;

        for (int i = 0; i < k; i++) {

            int last = arr[n - 1];

            for (int j = n - 1; j > 0; j--) {
                arr[j] = arr[j - 1];
            }

            arr[0] = last;
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;

        rotate(arr, k);

        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
```

**Example Output:**

```text
5 6 7 1 2 3 4
```

**Complexity:**

- Time Complexity: `O(n × k)`
- Space Complexity: `O(1)`

#### Approach 2: Optimal – In-Place Array Reversal Method

**Logic:**

Instead of shifting elements repeatedly, use three reversal operations:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining elements.

**Example Walkthrough:**

Original Array:
```text
[1, 2, 3, 4, 5, 6, 7]
```

Step 1 – Reverse the entire array:
```text
[7, 6, 5, 4, 3, 2, 1]
```

Step 2 – Reverse the first 3 elements:
```text
[5, 6, 7, 4, 3, 2, 1]
```

Step 3 – Reverse the remaining elements:
```text
[5, 6, 7, 1, 2, 3, 4]
```

**Java Code:**

```java
public class Main {

    static void reverse(int[] arr, int start, int end) {

        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            start++;
            end--;
        }
    }

    static void rotate(int[] arr, int k) {
        int n = arr.length;

        if (n == 0)
            return;

        k = k % n;

        reverse(arr, 0, n - 1);
        reverse(arr, 0, k - 1);
        reverse(arr, k, n - 1);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;

        rotate(arr, k);

        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
```

**Example Output:**

```text
5 6 7 1 2 3 4
```

**Complexity:**

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

## 4. Day 1 – Learning Summary

- Learned the basic concepts and fundamentals of Software Testing.
- Practiced array-based coding problems using Java.
