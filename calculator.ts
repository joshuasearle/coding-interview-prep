type operation = '+' | '-' | '*' | '/';

function isNumber(x: string) {
  return x >= '0' && x <= '9';
}

function calculator(expression: string): number {
  // The loop skips the last operation, so we add a dummy operation
  expression += '+0';

  // We want to keep track of our numbers as numbers (not strings)
  const stack: Array<number> = [];

  // Need to build the numbers from the chars
  let currentNumber = 0;

  // We want to add the first number to zero
  let prevOp = '+';

  for (let i = 0; i < expression.length; i++) {
    let char = expression[i];

    // If char is a number, add it to the current number
    if (isNumber(char)) {
      currentNumber = currentNumber * 10 + parseInt(char);
      continue;
    }

    // Add positive or negative to stack
    if (prevOp === '+') stack.push(currentNumber);
    if (prevOp === '-') stack.push(-currentNumber);

    // Apply to number on top of stack
    if (prevOp === '*') stack.push(stack.pop() * currentNumber);
    if (prevOp === '/') stack.push(stack.pop() / currentNumber);

    // Reassign the number to zero, and prevop to the current op
    currentNumber = 0;
    prevOp = char;
  }

  // Return the sum
  return stack.reduce((a, n) => a + n, 0);
}

console.log(calculator('2+2+3/2'));
